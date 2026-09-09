from langchain_huggingface import HuggingFaceEmbeddings
from .logger import logger

class EmbeddingsModel:
    def __init__(self, local_model= False, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        """Initializes the EmbeddingsModel with the specified model name.
        Args:
            model_name (str): The name of the HuggingFace model to use for embeddings. Defaults to "sentence-transformers/all-MiniLM-L6-v2".
        """
        self.model_name = model_name

        if local_model:
            self.embedder = self.load_local_model()
        else:
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

    def load_local_model(self):
        

        # Define the name of the zip file and the directory where it was saved
        zip_file_name = 'saved_embedding_model.zip'
        extraction_path = 'extracted_embedding_model'

        # import zipfile
        # import os

        # # Create the extraction directory if it doesn't exist
        # os.makedirs(extraction_path, exist_ok=True)

        # # Unzip the file
        # with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        #     zip_ref.extractall(extraction_path)

        # Load the model from the extracted local path
        loaded_model_from_zip = HuggingFaceEmbeddings(model_name=extraction_path)

        return loaded_model_from_zip