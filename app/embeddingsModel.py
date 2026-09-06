from langchain_huggingface import HuggingFaceEmbeddings
from .logger import logger

class EmbeddingsModel:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        """Initializes the EmbeddingsModel with the specified model name.
        Args:
            model_name (str): The name of the HuggingFace model to use for embeddings. Defaults to "sentence-transformers/all-MiniLM-L6-v2".
        """
        self.model_name = model_name

        self.embedder = self.intlize_model() 

    def get_model(self):
        """Returns a HuggingFaceEmbeddings instance with the specified model name.
        Returns:
            HuggingFaceEmbeddings: An instance of the HuggingFaceEmbeddings class configured with the model name.
        """
        if not self.embedder:
            raise ValueError("Embeddings model is not initialized.")

        return self.embedder
    
    def intlize_model(self):
        """Initializes the model with a new model name.
        Args:
            model_name (str): The name of the HuggingFace model to use for embeddings.
        """
        try:
            return HuggingFaceEmbeddings(model_name=self.model_name)
        except Exception as e:
            logger.error(f"Error initializing HuggingFaceEmbeddings: {e}")
            raise Exception(f"Failed to initialize HuggingFaceEmbeddings: {e}") 