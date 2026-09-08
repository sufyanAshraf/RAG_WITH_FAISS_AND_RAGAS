import faiss
import numpy as np

from .logger import logger


class DataBase:
    # _instance = None

    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self):
        # if not hasattr(self, "index"):
        #     self.index = None
        self.index = None

    def store_vectors(self, vectors):
        vectors_array = np.array(
            vectors,
            dtype="float32"
        )

        dimension = vectors_array.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(vectors_array)

        logger.info("Vectors stored: %d", self.index.ntotal)
        return self.index