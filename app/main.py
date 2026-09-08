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

    # -------------------------
    # 4. Create FAISS vector store
    # -------------------------
    
    # vector_store = FAISS.from_documents(
    #     documents=docs,
    #     embedding=embedder, 
    # )
    # logger.info("FAISS vector store created successfully")
    # # -------------------------
    # # 5. Search relevant documents
    # # -------------------------
    # relevant_docs = vector_store.similarity_search(
    #     request.query,
    #     k=3
    # )

    # # -------------------------
    # # 6. Build context
    # # -------------------------
    # context = "\n\n".join(
    #     doc.page_content
    #     for doc in relevant_docs
    # )

    # # -------------------------
    # # 7. Create prompt
    # # -------------------------
    # full_prompt = f"""
    #     You are a helpful AI assistant.

    #     Answer the user's question using the provided context.

    #     Context:
    #     {context}

    #     Question:
    #     {request.query}

    #     Answer:
    # """

    # # -------------------------
    # # 8. Call Groq
    # # -------------------------
     
    # response = model.invoke(
    #     full_prompt=full_prompt
    # )
 
    read_data = readData()
    data = read_data.readjson()

    # Create embeddings for the data
    embedding_records, vectors = create_embeddings(data, embedder)

    # Store the vectors in the database
    db = dataBase()
    index = db.store_vectors(vectors)

    # query model
    query = "best burger under 5 km"
    result = queryVectors(query, embedder, index, embedding_records)
    logger.info(result)


    response = {"message": "all ok"}
    return chatResponse(response=response) 





 
@app.get("/health")
def health_check() -> dict[str, str]: 
    """Health check endpoint to verify that the API is running.
        returns
            A dictionary indicating the health status of the API.
    """
    logger.info("Health check requested")
    return {"status": "ok"}
