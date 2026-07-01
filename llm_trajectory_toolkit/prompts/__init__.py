"""Prompt generation and dataset loading."""

from .generator import (
    PairedPromptGenerator,
    InstructionPair,
    extract_pairs_for_analysis,
    INSTRUCTION_TEMPLATES,
    FACTUAL_QUESTIONS,
)
from .loaders import DatasetLoader, load_anthropic_evals

__all__ = [
    'PairedPromptGenerator',
    'InstructionPair',
    'extract_pairs_for_analysis',
    'INSTRUCTION_TEMPLATES',
    'FACTUAL_QUESTIONS',
    'DatasetLoader',
    'load_anthropic_evals',
]
