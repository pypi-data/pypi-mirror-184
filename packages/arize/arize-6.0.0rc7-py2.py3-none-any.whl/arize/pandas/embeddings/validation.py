# from typing import Dict, List
#
# from . import errors as err
# from .base_generators import BaseEmbeddingGenerator
#
#
# @staticmethod
# def _check_embedding_generators_configs(
#     embedding_generators: Dict[str, BaseEmbeddingGenerator],
# ) -> List[err.InvalidEmbeddingGeneratorConfig]:
#     # Only continue if there are embedding generators
#     if embedding_generators is None:
#         return []
#
#     errors = []
#     for embedding_name, embedding_generator in embedding_generators.items():
#         uc_area = embedding_generator.use_case.split('.')[0]  # NLP, CV, or TABULAR
#         if uc_area == "NLP":
#             # Check that the model is supported
#             if embedding_generator.model not in NLP_PRETRAINED_MODELS:
#                 errors.append(err.InvalidEmbeddingGeneratorConfig(
#                     embedding_name,
#                     wrong_model=embedding_generator.model
#                 ))
#         elif uc_area == "CV":
#             # TODO(KIKO)
#             pass
#         elif uc_area == "TABULAR":
#             # TODO(KIKO)
#             pass
#
#     return errors
