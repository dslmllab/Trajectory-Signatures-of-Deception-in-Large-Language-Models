"""Statistical analysis and classification modules"""

from .statistical import (
    StatisticalAnalyzer,
    PairedTestResult,
    PermutationResult,
    PerLayerResult,
    PartialCorrelationResult,
    VarianceComparisonResult,
    compare_truthful_deceptive
)
from .classification import (
    DeceptionClassifier,
    ClassificationResult,
    ThreeWayResult,
    train_deception_classifier,
    train_binary_deception_classifier,
    train_three_way_classifier,
    split_by_entropy,
    compare_binary_vs_three_way
)
from .early_warning import (
    EarlyWarningAnalyzer,
    EarlyWarningResult,
    plot_early_warning_curve
)
from .cross_model import (
    CrossModelValidator,
    CrossModelResult,
    ModelResult,
    TransferResult,
    compare_models_quick
)
from .interpretability_baselines import (
    mass_mean_probe,
    ccs_probe,
    repe_probe,
    lr_probe_auroc,
    run_all_baselines,
)
from .temporal_dynamics import (
    TemporalDynamicsAnalyzer,
    TemporalDynamicsResult,
    TemporalFeatures,
    TokenTrajectory,
    OnsetAnalysis,
    plot_temporal_evolution
)

__all__ = [
    # Statistical
    'StatisticalAnalyzer',
    'PairedTestResult',
    'PermutationResult',
    'PerLayerResult',
    'PartialCorrelationResult',
    'VarianceComparisonResult',
    'compare_truthful_deceptive',
    # Classification
    'DeceptionClassifier',
    'ClassificationResult',
    'ThreeWayResult',
    'train_deception_classifier',
    'train_binary_deception_classifier',
    'train_three_way_classifier',
    'split_by_entropy',
    'compare_binary_vs_three_way',
    # Early Warning
    'EarlyWarningAnalyzer',
    'EarlyWarningResult',
    'plot_early_warning_curve',
    # Cross-Model Validation
    'CrossModelValidator',
    'CrossModelResult',
    'ModelResult',
    'TransferResult',
    'compare_models_quick',
    # Interpretability Baselines
    'mass_mean_probe',
    'ccs_probe',
    'repe_probe',
    'lr_probe_auroc',
    'run_all_baselines',
    # Temporal Dynamics
    'TemporalDynamicsAnalyzer',
    'TemporalDynamicsResult',
    'TemporalFeatures',
    'TokenTrajectory',
    'OnsetAnalysis',
    'plot_temporal_evolution'
]
