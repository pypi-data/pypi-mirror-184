from collections import OrderedDict
from typing import Tuple

import numpy as np
import torch
import torch.nn as nn

from analogvnn.utils.is_cpu_cuda import is_cpu_cuda

__all__ = ['summary']


def summary(model: nn.Module, input_size: Tuple, include_self: bool = False):
    """Print a summary of the model.

    Args:
        model (nn.Module): the model to print the summary of.
        input_size (tuple): the input size.
        include_self (bool): include itself in the summary of the model.

    Returns:
        str: the summary of the model.
    """

    # training_status = model.training
    # model.train(True)
    result = ""
    device = is_cpu_cuda.get_module_device(model)

    def register_hook(module):
        def hook(module, inputs, output):
            class_name = str(module.__class__).split(".")[-1].split("'")[0]

            m_key = f"{class_name}-{len(summary) + 1:d}"
            summary[m_key] = OrderedDict()
            summary[m_key]["input_shape"] = list(inputs[0].size())
            summary[m_key]["input_shape"][0] = -1
            if isinstance(output, (list, tuple)):
                summary[m_key]["output_shape"] = [
                    [-1] + list(o.size())[1:] for o in output
                ]
            else:
                summary[m_key]["output_shape"] = list(output.size())
                summary[m_key]["output_shape"][0] = -1

            summary[m_key]["nb_params"] = 0
            summary[m_key]["nb_params_trainable"] = 0
            for parameter in module.parameters():
                params = torch.prod(torch.LongTensor(list(parameter.size())))
                summary[m_key]["nb_params"] += params
                if parameter.requires_grad:
                    summary[m_key]["nb_params_trainable"] += params

        if (
                not isinstance(module, nn.Sequential)
                and not isinstance(module, nn.ModuleList)
                and (module != model or include_self)
        ):
            hooks.append(module.register_forward_hook(hook))

    # multiple inputs to the network
    if isinstance(input_size, tuple):
        input_size = [input_size]

    # batch_size of 2 for batchnorm
    x = [torch.rand(2, *in_size).to(device) for in_size in input_size]

    # create properties
    summary = OrderedDict()
    hooks = []

    # register hook
    model.apply(register_hook)

    # make a forward pass
    model(*x)

    # remove these hooks
    for h in hooks:
        h.remove()

    rows = [["Layer (type)", "Input Shape", "Output Shape", "Trainable Param #", "Param #"]]
    total_params = 0
    total_output = 0
    trainable_params = 0
    for layer in summary:
        rows.append([
            layer,
            str(summary[layer]["input_shape"]),
            str(summary[layer]["output_shape"]),
            f"{summary[layer]['nb_params_trainable']:,}",
            f"{summary[layer]['nb_params']:,}"
        ])

        total_params += summary[layer]["nb_params"]
        total_output += np.prod(summary[layer]["output_shape"])
        trainable_params += summary[layer]["nb_params_trainable"]

    # assume 4 bytes/number (float on cuda).
    total_input_size = abs(np.prod(input_size) * 4. / 1024.)
    total_output_size = abs(2. * total_output * 4. / 1024.)  # x2 for gradients
    total_params_size = abs(total_params * 4. / 1024.)
    total_size = total_params_size + total_output_size + total_input_size

    col_size = [0] * len(rows[0])
    for row in rows:
        for i, v in enumerate(row):
            col_size[i] = max(len(v) + 4, col_size[i])

    line_size = np.sum(col_size)
    result += ("-" * line_size) + "\n"
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            result += ("{:>" + str(col_size[j]) + "}").format(col)
        result += "\n"
        if i == 0:
            result += ("=" * line_size) + "\n"

    result += ("=" * line_size) + "\n"
    result += f"Total params: {total_params:,}\n"
    result += f"Trainable params: {trainable_params:,}\n"
    result += f"Non-trainable params: {total_params - trainable_params:,}\n"
    result += ("-" * line_size) + "\n"
    result += f"Input size (KB): {total_input_size:0.2f}\n"
    result += f"Forward/backward pass size (KB): {total_output_size:0.2f}\n"
    result += f"Params size (KB): {total_params_size:0.2f}\n"
    result += f"Estimated Total Size (KB): {total_size:0.2f}\n"
    result += ("-" * line_size) + "\n"

    # model.train(training_status)
    return result
