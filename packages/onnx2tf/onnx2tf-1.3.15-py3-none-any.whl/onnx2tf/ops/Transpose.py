import random
random.seed(0)
import numpy as np
np.random.seed(0)
import tensorflow as tf
import onnx_graphsurgeon as gs
from onnx2tf.utils.common_functions import (
    get_replacement_parameter,
    replace_parameter,
    get_constant_or_variable,
    convert_axis,
    print_node_info,
    inverted_operation_enable_disable,
    make_tf_node_info,
)


@print_node_info
@inverted_operation_enable_disable
@get_replacement_parameter
def make_node(
    *,
    graph_node: gs.Node,
    tf_layers_dict: dict,
    **kwargs: dict,
):
    """Transpose

    Parameters
    ----------
    graph_node: gs.Node
        graph_surgeon Node

    tf_layers_dict: dict
        optype, shape, dtype, tensorflow graph
    """
    before_op_output_shape_trans_1 = \
        tf_layers_dict.get(graph_node.inputs[0].name, {}).get('before_op_output_shape_trans', True)
    before_op_output_shape_trans = \
        before_op_output_shape_trans_1

    graph_node_input = get_constant_or_variable(
        graph_node.inputs[0],
        before_op_output_shape_trans,
    )
    graph_node_output: gs.Variable = graph_node.outputs[0]
    output_shape = graph_node_output.shape
    dtype = graph_node_output.dtype

    input_tensor = tf_layers_dict[graph_node_input.name]['tf_node'] \
        if isinstance(graph_node_input, gs.Variable) else graph_node_input
    input_tensor_shape = input_tensor.shape
    tensor_rank = len(input_tensor_shape)

    perm = graph_node.attrs.get('perm', [idx for idx in reversed(range(tensor_rank))])
    if 'nwc_nhwc_ndhwc_keep' in tf_layers_dict[graph_node_input.name] \
        and tf_layers_dict[graph_node_input.name]['nwc_nhwc_ndhwc_keep'] == True:
        perm = [i for i in range(tensor_rank)]

    if isinstance(perm, list) or (isinstance(perm, np.ndarray) and len(perm.shape) > 0):
        if perm[0] == 0:
            try:
                if graph_node.o().op == 'Softmax' \
                    and graph_node.o().inputs[0].shape == input_tensor_shape:
                    perm = [idx for idx in range(tensor_rank)]
                else:
                    perm = [
                        convert_axis(
                            axis=idx,
                            tensor_rank=tensor_rank,
                            before_op_output_shape_trans=before_op_output_shape_trans,
                        ) for idx in perm
                    ]
            except:
                perm = [
                    convert_axis(
                        axis=idx,
                        tensor_rank=tensor_rank,
                        before_op_output_shape_trans=before_op_output_shape_trans,
                    ) for idx in perm
                ]
        else:
            # When a zero-dimensional transposition occurs, compare the shape
            # of the final output tensor of ONNX with the shape
            # of the input tensor of TF and transpose to match the shape
            # of the final output tensor on the ONNX side
            onnx_output_shape = [s if not isinstance(s, str) else None for s in output_shape]
            onnx_output_shape_none_count = onnx_output_shape.count(None)
            tf_input_shape = input_tensor_shape
            new_perm = [-1] * len(onnx_output_shape)
            for tf_shape_idx, tf_shape_value in enumerate(tf_input_shape):
                matched_idxs = [
                    idx for idx, onnx_shape_value in enumerate(onnx_output_shape) \
                        if onnx_shape_value == tf_shape_value
                ]
                if len(matched_idxs) == 0 and onnx_output_shape_none_count <= 1:
                    new_perm[tf_shape_idx] = onnx_output_shape.index(tf_shape_value)
                elif len(matched_idxs) == 0 and onnx_output_shape_none_count > 1:
                    new_perm = perm
                elif len(matched_idxs) == 1:
                    new_perm[matched_idxs[0]] = tf_shape_idx
                else:
                    for matched_idx in matched_idxs:
                        if new_perm[matched_idx] == -1:
                            new_perm[matched_idx] = tf_shape_idx
                            break
            perm = new_perm

    elif perm is not None and isinstance(perm, np.ndarray) and len(perm.shape) == 0:
        if perm[0] == 0:
            perm = convert_axis(
                axis=perm,
                tensor_rank=tensor_rank,
                before_op_output_shape_trans=before_op_output_shape_trans,
            )
        else:
            # When a zero-dimensional transposition occurs, compare the shape
            # of the final output tensor of ONNX with the shape of the input tensor
            # of TF and transpose to match the shape of the final output tensor on the ONNX side
            onnx_output_shape = [s if not isinstance(s, str) else None for s in output_shape]
            onnx_output_shape_none_count = onnx_output_shape.count(None)
            tf_input_shape = input_tensor_shape
            new_perm = [-1] * len(onnx_output_shape)
            for tf_shape_idx, tf_shape_value in enumerate(tf_input_shape):
                matched_idxs = [
                    idx for idx, onnx_shape_value in enumerate(onnx_output_shape) \
                        if onnx_shape_value == tf_shape_value
                ]
                if len(matched_idxs) == 0 and onnx_output_shape_none_count <= 1:
                    new_perm[tf_shape_idx] = onnx_output_shape.index(tf_shape_value)
                elif len(matched_idxs) == 0 and onnx_output_shape_none_count > 1:
                    new_perm = perm
                elif len(matched_idxs) == 1:
                    new_perm[matched_idxs[0]] = tf_shape_idx
                else:
                    for matched_idx in matched_idxs:
                        if new_perm[matched_idx] == -1:
                            new_perm[matched_idx] = tf_shape_idx
                            break
            perm = new_perm

    # Preserving Graph Structure (Dict)
    tf_layers_dict[graph_node_output.name] = {
        'optype': graph_node.op,
        'shape': output_shape,
        'dtype': dtype,
    }

    perm = list(perm) if perm is not None else None

    # Param replacement
    input_tensor = replace_parameter(
        value_before_replacement=input_tensor,
        param_target='inputs',
        param_name=graph_node.inputs[0].name,
        **kwargs,
    )
    perm = replace_parameter(
        value_before_replacement=perm,
        param_target='attributes',
        param_name='perm',
        **kwargs,
    )

    # Special Transpose
    # https://zenn.dev/pinto0309/scraps/cfb59856ac0453
    # Get dimension with 1 element
    x_shape_one_dims = [
        idx for idx in range(len(input_tensor_shape)) \
            if isinstance(input_tensor_shape[idx], int) and input_tensor_shape[idx]==1
    ]
    x_shape_none_dims_count = len(
        [dim for dim in input_tensor_shape if not isinstance(dim, int) or dim < 1]
    )
    # Delete dimension with 1 element
    squeezed_original_x = tf.squeeze(input_tensor, x_shape_one_dims)
    # Obtain a shape with the dimension with 1 element removed
    squeezed_original_shapes = squeezed_original_x.shape

    # Generation of TF OP
    if tensor_rank >= 6 and len(squeezed_original_shapes) <= 5 and x_shape_none_dims_count < 2:
        # Special Transpose
        # Suppresses as much as possible the conversion of transposes
        # of 6 or more dimensions into FlexTransposes
        remove_one_target_perm = [
            idx for idx in perm if idx not in x_shape_one_dims
        ]
        sorted_remove_one_target_perm = sorted(remove_one_target_perm)
        replaced_remove_one_target_perm = [
            sorted_remove_one_target_perm.index(idx) \
                for idx in remove_one_target_perm
        ]
        transposed_no_one_data = \
            tf.transpose(
                a=squeezed_original_x,
                perm=replaced_remove_one_target_perm,
            )
        tf_layers_dict[graph_node_output.name]['tf_node'] = \
            tf.reshape(
                tensor=transposed_no_one_data,
                shape=[
                    dim if not isinstance(dim, str) else -1 for dim in output_shape
                ],
            )
    else:
        # Normal Transpose
        tf_layers_dict[graph_node_output.name]['tf_node'] = \
            tf.transpose(
                a=input_tensor,
                perm=perm,
                name=graph_node.name,
            )

    # Generation of Debug Info
    tf_layers_dict[graph_node_output.name]['tf_node_info'] = \
        make_tf_node_info(
            node_info={
                'tf_op_type': tf.transpose,
                'tf_inputs': {
                    'a': input_tensor,
                    'perm': perm,
                },
                'tf_outputs': {
                    'output': tf_layers_dict[graph_node_output.name]['tf_node'],
                },
            }
        )
