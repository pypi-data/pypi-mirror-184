from enum import Enum, auto, unique


@unique
class NLPUseCases(Enum):
    SEQUENCE_CLASSIFICATION = auto()


@unique
class CVUseCases(Enum):
    IMAGE_CLASSIFICATION = auto()


@unique
class TabularUseCases(Enum):
    FEATURE_EMBEDDING = auto()


class UseCases:
    NLP = NLPUseCases
    CV = CVUseCases
    # TABULAR = TabularUseCases
