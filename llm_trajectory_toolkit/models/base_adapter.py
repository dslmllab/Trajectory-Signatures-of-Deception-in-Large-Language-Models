"""
Base Model Adapter Interface

Abstract base class for supporting different LLM architectures.
"""

from abc import ABC, abstractmethod
from typing import Optional, List
import torch


class BaseModelAdapter(ABC):
    """
    Abstract interface for LLM trajectory capture.

    Subclass this to add support for new model architectures.

    Example:
        >>> class MyModelAdapter(BaseModelAdapter):
        ...     def load_model(self):
        ...         return MyModel.from_pretrained(self.model_name)
        ...
        ...     def get_layer_modules(self):
        ...         return self.model.my_custom_layers
    """

    def __init__(self, model_name: str, device: Optional[str] = None):
        """
        Args:
            model_name: HuggingFace model identifier or path
            device: Device to load model on ('cuda', 'cpu', or None for auto)
        """
        self.model_name = model_name
        if device:
            self.device = device
        elif torch.cuda.is_available():
            self.device = 'cuda'
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            self.device = 'mps'
        else:
            self.device = 'cpu'
        self.model = None
        self.tokenizer = None

    @abstractmethod
    def load_model(self):
        """
        Load model and tokenizer.

        Must set:
        - self.model: The loaded model
        - self.tokenizer: The loaded tokenizer

        Returns:
            Tuple of (model, tokenizer)
        """
        pass

    @abstractmethod
    def get_layer_modules(self) -> List:
        """
        Get list of transformer layer modules for hook registration.

        Returns:
            List of nn.Module objects representing transformer blocks
        """
        pass

    def get_num_layers(self) -> int:
        """
        Get total number of transformer layers.

        Returns:
            Number of layers
        """
        layers = self.get_layer_modules()
        return len(layers)

    def prepare_for_generation(self):
        """
        Optional: Prepare model for generation (set to eval mode, etc.)
        """
        if self.model is not None:
            self.model.eval()

    def cleanup(self):
        """
        Optional: Cleanup resources (clear GPU memory, etc.)
        """
        if self.device == 'cuda' and torch.cuda.is_available():
            torch.cuda.empty_cache()
        elif self.device == 'mps' and hasattr(torch, 'mps') and hasattr(torch.mps, 'empty_cache'):
            torch.mps.empty_cache()
