import numpy as np

def search(query, vector_store):
    relevant_docs = vector_store.similarity_search(
        query,
        k=3
    )
    return relevant_docs


def queryVectors(query, model, index, embedding_records):

    # db_result = search(query, index)
    

    query_embedding = model.embed_query(query)
    query_embedding = np.array(query_embedding).astype("float32")

    # Reshape the query_embedding to be a 2D array (1, dimension)
    query_embedding = query_embedding.reshape(1, -1)

    scores, indexes = index.search(query_embedding, 5)

    b = []
    for score, idx in zip(scores[0], indexes[0]):
        # Retrieve the full record from embedding_records using the index
        record = embedding_records[idx]

        # Assign the metadata dictionary to 'place'
        place = record['metadata']
 
        b.append(place)
    return b

