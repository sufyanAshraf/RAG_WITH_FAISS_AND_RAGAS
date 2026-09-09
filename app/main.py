from fastapi import FastAPI
from pydantic import BaseModel 
import configparser 
from .logger import logger  
from .models import GroqModel
from .embeddingsModel import EmbeddingsModel  
# from langchain_community.vectorstores import FAISS
from .readData import readData
from .embeddingsCreator import create_embeddings
from .dataBase import dataBase
from .queryModel import queryVectors
from .evalDataPrepration import create_evaluation_dataset
from .eval import evaluateWithRagas 
from .prompt import getPrompt
def read_api_key_from_config() -> str:
    """Read the API key from the config.ini file."""
    logger.info("Reading API key from config file")
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config.get("KEYS", "groq_api_key") , config.get("KEYS", "huggingface_api_key")

app = FastAPI(title="Ingession API", version="0.1.0") 

class chatRequest(BaseModel):
    query: str

class chatResponse(BaseModel):
    response: str


@app.post("/", response_model=chatResponse)
async def chat(request: chatRequest) -> chatResponse:
    groq_api_key, huggingface_api_key = read_api_key_from_config()

    model = GroqModel(groq_api_key)
    # docs = read_documents_from_file()
    embeddings_model = EmbeddingsModel()
    embedder = embeddings_model.get_model()  

    # logger.info(f"Embedder type: {type(embedder)}")
    # logger.info(f"Has embed_documents: {hasattr(embedder, 'embed_documents')}")
    # logger.info(f"Has embed_query: {hasattr(embedder, 'embed_query')}")
 
    # # -------------------------
    # # 5. Search relevant documents
    # # -------------------------
    # relevant_docs = vector_store.similarity_search(
    #     request.query,
    #     k=3
    # )

    
    read_data = readData()
    data = read_data.readjson()

    # Create embeddings for the data
    embedding_records, vectors = create_embeddings(data, embedder)

    # Store the vectors in the database
    db = dataBase()
    index = db.store_vectors(vectors)

    # query model
    query = request.query
    result = queryVectors(query, embedder, index, embedding_records)

    logger.info("Successfull query database")

    full_prompt =getPrompt(query=query, relevant_docs=result)
    

    # -------------------------
    # 8. Call Groq
    # -------------------------
        
    response = model.invoke(
        full_prompt=full_prompt
    )
    logger.info(response) 

    # # run evals
    # EvalData = create_evaluation_dataset(embedder, index, model, embedding_records)
    # result = evaluateWithRagas(EvalData, model, embedder)
    # print(result.to_pandas)
    # logger.info(result.to_pandas)
 
    return chatResponse(response=response) 





 
@app.get("/health")
def health_check() -> dict[str, str]: 
    """Health check endpoint to verify that the API is running.
        returns
            A dictionary indicating the health status of the API.
    """
    logger.info("Health check requested")
    return {"status": "ok"}
