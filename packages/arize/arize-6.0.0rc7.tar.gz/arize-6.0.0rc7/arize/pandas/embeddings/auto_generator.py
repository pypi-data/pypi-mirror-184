from .cv_generators import EmbeddingGeneratorForCVImageClassification
from .nlp_generators import EmbeddingGeneratorForNLPSequenceClassification
from .usecases import UseCases


class AutoEmbeddingGenerator:
    def __init__(self, **kwargs):
        raise EnvironmentError(
            f"{self.__class__.__name__} is designed to be instantiated "
            f"using the `{self.__class__.__name__}.from_use_case(use_case, **kwargs)`."
        )

    @staticmethod
    def from_use_case(use_case, **kwargs):
        print(use_case)
        if use_case == UseCases.NLP.SEQUENCE_CLASSIFICATION:
            return EmbeddingGeneratorForNLPSequenceClassification(**kwargs)
        elif use_case == UseCases.CV.IMAGE_CLASSIFICATION:
            return EmbeddingGeneratorForCVImageClassification(**kwargs)
        else:
            raise ValueError(f"Invalid use case {use_case}")
