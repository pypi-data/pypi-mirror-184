# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Pipeline for performing PyTorch-based Quantization-Aware Training (QAT)."""

import copy
from typing import Any, Dict, Optional

import torch
import transformers

from archai.nlp.quantization.modules import (
    FakeDynamicQuantConv1d,
    FakeDynamicQuantConv1dForOnnx,
    FakeDynamicQuantHFConv1D,
    FakeDynamicQuantHFConv1DForOnnx,
    FakeDynamicQuantLinear,
    FakeDynamicQuantLinearForOnnx,
    FakeQuantEmbedding,
    FakeQuantEmbeddingForOnnx,
)

DYNAMIC_QAT_MODULE_MAP = {
    torch.nn.Embedding: FakeQuantEmbedding,
    torch.nn.Linear: FakeDynamicQuantLinear,
    torch.nn.Conv1d: FakeDynamicQuantConv1d,
    transformers.modeling_utils.Conv1D: FakeDynamicQuantHFConv1D,
}
ONNX_DYNAMIC_QAT_MODULE_MAP = {
    torch.nn.Embedding: FakeQuantEmbeddingForOnnx,
    torch.nn.Linear: FakeDynamicQuantLinearForOnnx,
    torch.nn.Conv1d: FakeDynamicQuantConv1dForOnnx,
    transformers.modeling_utils.Conv1D: FakeDynamicQuantHFConv1DForOnnx,
}
from archai.nlp import logging_utils

logger = logging_utils.get_logger(__name__)


def qat_to_float_modules(model: torch.nn.Module) -> None:
    """Convert QAT-ready modules to float-based modules.

    This function converts all QAT-ready modules in the input model to float-based modules.
    It does this recursively, so all sub-modules within the input model will also be
    converted if applicable.

    Args:
        model: QAT-ready module to be converted.

    """

    for name in list(model._modules):
        module = model._modules[name]

        if hasattr(module, "to_float"):
            model._modules[name] = module.to_float()
        else:
            qat_to_float_modules(module)


def float_to_qat_modules(
    model: torch.nn.Module,
    module_mapping: Optional[Dict[torch.nn.Module, torch.nn.Module]] = DYNAMIC_QAT_MODULE_MAP,
    qconfig: Optional[Dict[torch.nn.Module, Any]] = None,
    **kwargs
) -> None:
    """Convert float-based modules to QAT-ready modules.

    This function converts all float-based modules in the input model to QAT-ready
    modules using the provided module mapping. It does this recursively, so all sub-modules
    within the input model will also be converted if applicable.

    A quantization configuration can also be supplied.

    Args:
        model: Float-based module to be converted.
        module_mapping: Maps between float and QAT-ready modules.
        qconfig: Quantization configuration to be used for the conversion.

    """

    for name in list(model._modules):
        module = model._modules[name]

        if type(module) in module_mapping:
            if not hasattr(module, "qconfig"):
                module.qconfig = qconfig

            model._modules[name] = module_mapping[type(module)].from_float(module, qconfig, **kwargs)

        else:
            float_to_qat_modules(module, module_mapping=module_mapping, qconfig=qconfig, **kwargs)


def prepare_with_qat(
    model: torch.nn.Module,
    inplace: Optional[bool] = True,
    onnx_compatible: Optional[bool] = False,
    backend: Optional[str] = "qnnpack",
    **kwargs
) -> torch.nn.Module:
    """Prepare a float-based PyTorch model for quantization-aware training (QAT).

    This function modifies the input model in place by inserting
    QAT-based modules and configurations.

    Args:
        model: Float-based PyTorch module to be prepared for QAT.
        inplace: Whether the prepared QAT model should replace the original model.
        onnx_compatible: Whether the prepared QAT model should be compatible with ONNX.
        backend: Quantization backend to be used.

    Returns:
        The input model, modified in place (or not) to be ready for QAT.

    """

    logger.info("Preparing model with QAT ...")

    prepared_model = model
    if not inplace:
        prepared_model = copy.deepcopy(model)

    qconfig = torch.quantization.get_default_qat_qconfig(backend)
    module_mapping = ONNX_DYNAMIC_QAT_MODULE_MAP if onnx_compatible else DYNAMIC_QAT_MODULE_MAP

    float_to_qat_modules(prepared_model, module_mapping=module_mapping, qconfig=qconfig, **kwargs)

    return prepared_model
