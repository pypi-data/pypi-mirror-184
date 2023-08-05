from functools import partial

import pandas as pd
import requests

from .base_generators import CVEmbeddingGenerator, logger
from .usecases import UseCases

try:
    import torch
    from datasets import Dataset
    from PIL import Image
except ImportError:
    raise ImportError(
        "To enable embedding generation, "
        "the arize module must be installed with the EmbeddingGeneration option: "
        "pip install 'arize[EmbeddingGeneration]'."
    )


class EmbeddingGeneratorForCVImageClassification(CVEmbeddingGenerator):
    def __repr__(self):
        uc = self.use_case.split(".")
        return (
            f"This is EmbeddingGenerator for {uc[0]} {uc[1]} with model = "
            f"{self.model_name}"
        )

    def __init__(self, model_name="google/vit-base-patch32-224-in21k", **kwargs):
        super(EmbeddingGeneratorForCVImageClassification, self).__init__(
            model_name, **kwargs
        )
        self.__use_case = self._parse_use_case(UseCases.CV.IMAGE_CLASSIFICATION)

    @property
    def use_case(self) -> str:
        return self.__use_case

    def process_image(self, batch, image_path_col):
        if self.src_type == "url":

            def f(url: str) -> Image:
                return Image.open(requests.get(url, stream=True).raw)

        elif self.src_type == "local":

            def f(local_path: str) -> Image:
                return Image.open(local_path)

        else:
            raise ValueError("src_type must be 'local' or 'url'")

        return self.feature_extractor(
            [f(x) for x in batch[image_path_col]], return_tensors="pt"
        ).to(self.device)

    def generate_embeddings(self, image_path_col: pd.Series):
        if type(image_path_col) != pd.Series:
            raise TypeError(
                "image_path_col must be a pandas Series, i.e, a column from a dataframe: "
                "df[image_path_col]"
            )
        ds = Dataset.from_pandas(pd.DataFrame(image_path_col))
        ds.set_transform(
            partial(self.process_image, image_path_col=image_path_col.name)
        )
        logger.info("Generating embedding vectors")
        ds = ds.map(
            lambda batch: self.__get_embedding_vector(batch),
            batched=True,
            batch_size=self.batch_size,
        )
        return ds.to_pandas()["embedding_vector"]

    def __get_embedding_vector(self, batch):
        with torch.no_grad():
            outputs = self.model(**batch)
        embeddings = torch.mean(outputs.last_hidden_state, 1).cpu().numpy()
        return {"image_vector": embeddings}
