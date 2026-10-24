"""
This file registers the model with the Python SDK.
"""

from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.services.vision import Vision

from .qwen import qwen

Registry.register_resource_creator(
    Vision.API,
    qwen.MODEL,
    ResourceCreatorRegistration(qwen.new, qwen.validate),
)
