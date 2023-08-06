import logging
import sys
from abc import ABC, abstractmethod
from enum import Enum

try:
    import torch
    from transformers import AutoTokenizer, AutoModel, AutoFeatureExtractor
except ImportError:
    raise ImportError(
        "To enable embedding generation, "
        "the arize module must be installed with the EmbeddingGeneration option: "
        "pip install 'arize[EmbeddingGeneration]'."
    )

logger = logging.getLogger(__name__)
if hasattr(sys, "ps1"):
    # for python interactive mode
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setLevel(logging.INFO)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)


class BaseEmbeddingGenerator(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    def __init__(self, model_name, batch_size=100):
        self.__model_name = model_name
        self.__device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.__batch_size = batch_size

    @property
    def model_name(self):
        return self.__model_name

    @property
    def device(self):
        return self.__device

    @property
    def batch_size(self):
        return self.__batch_size

    @batch_size.setter
    def batch_size(self, new_batch_size):
        err_message = "New batch size should be an integer greater than 0."
        if not isinstance(new_batch_size, int):
            raise TypeError(err_message)
        elif new_batch_size <= 0:
            raise ValueError(err_message)
        else:
            self.__batch_size = new_batch_size
            logger.info(f"Batch size has been set to {new_batch_size}.")

    @staticmethod
    def _parse_use_case(use_case: Enum) -> str:
        uc_area = use_case.__class__.__name__.strip("UseCases")
        uc_task = use_case.name
        return f"{uc_area}.{uc_task}"

    @abstractmethod
    def model(self):
        pass

    @abstractmethod
    def use_case(self) -> str:
        pass

    @abstractmethod
    def generate_embeddings(self, df_col):
        pass


class NLPEmbeddingGenerator(BaseEmbeddingGenerator, ABC):
    def __init__(self, model_name, max_length=512, **kwargs):
        super(NLPEmbeddingGenerator, self).__init__(model_name, **kwargs)
        self.__max_length = max_length
        logger.info("Downloading tokenizer")
        self.__tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        logger.info(f"Downloading pre-trained large language model {self.model_name}")
        self.__model = AutoModel.from_pretrained(self.model_name).to(self.device)

    @property
    def tokenizer(self):
        return self.__tokenizer

    @property
    def model(self):
        return self.__model

    @property
    def max_length(self):
        return self.__max_length

    @abstractmethod
    def tokenize(self, batch, text_col):
        pass


class CVEmbeddingGenerator(BaseEmbeddingGenerator, ABC):
    def __init__(self, model_name, **kwargs):
        super(CVEmbeddingGenerator, self).__init__(model_name, **kwargs)
        logger.info("Downloading feature extractor")
        self.__feature_extractor = AutoFeatureExtractor.from_pretrained(self.model_name)
        logger.info(f"Downloading pre-trained model {self.model_name}")
        self.__model = AutoModel.from_pretrained(self.model_name).to(self.device)

    @property
    def feature_extractor(self):
        return self.__feature_extractor

    @property
    def model(self):
        return self.__model

    @abstractmethod
    def process_image(self, batch, image_path_col):
        pass
