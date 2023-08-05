from functools import partial

import pandas as pd

from .base_generators import NLPEmbeddingGenerator, logger
from .usecases import UseCases

try:
    import torch
    from datasets import Dataset
except ImportError:
    raise ImportError(
        "To enable embedding generation, "
        "the arize module must be installed with the EmbeddingGeneration option: "
        "pip install 'arize[EmbeddingGeneration]'."
    )


class EmbeddingGeneratorForNLPSequenceClassification(NLPEmbeddingGenerator):
    def __repr__(self):
        uc = self.use_case.split(".")
        return (
            f"This is EmbeddingGenerator for {uc[0]} {uc[1]} with model = "
            f"{self.model_name}, and max_length = {self.max_length}"
        )

    def __init__(self, model_name="xlm-roberta-large", **kwargs):
        super(EmbeddingGeneratorForNLPSequenceClassification, self).__init__(
            model_name, **kwargs
        )
        self.__use_case = self._parse_use_case(UseCases.NLP.SEQUENCE_CLASSIFICATION)

    @property
    def use_case(self) -> str:
        return self.__use_case

    def tokenize(self, batch, text_col):
        return {
            k: v.to(self.device)
            for k, v in self.tokenizer(
                batch[text_col],
                padding=True,
                truncation=True,
                max_length=self.max_length,
                return_tensors="pt",
            ).items()
        }

    def generate_embeddings(self, text_col: pd.Series):
        if type(text_col) != pd.Series:
            raise TypeError(
                "text_col must be a pandas Series, i.e, a column from a dataframe: "
                "df[text_col]"
            )
        ds = Dataset.from_pandas(pd.DataFrame(text_col))
        ds.set_transform(partial(self.tokenize, text_col=text_col.name))
        logger.info("Generating embedding vectors")
        ds = ds.map(
            lambda batch: self.__get_embedding_vector(batch),
            batched=True,
            batch_size=self.batch_size,
        )
        return ds.to_pandas()["embedding_vector"]

    def __get_embedding_vector(
        self,
        batch,
    ):
        with torch.no_grad():
            out = self.model(**batch)
            # (layer_#, batch_size, seq_length/or/num_tokens, hidden_size)
            # Select last layer, then CLS token vector
            embeddings = out.last_hidden_state[:, 0, :]

        return {"embedding_vector": embeddings.cpu().numpy()}
