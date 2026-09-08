import numpy as np

def create_embeddings(data, model):
    """
    Create embeddings for a list of texts using the specified model.

    Args:
        texts (list): A list of strings to create embeddings for.
        model (str): The name of the embedding model to use."""

    embedding_records = []
    cat = ["spa","hotel", "restaurant" ]
    vectors = []
    count = 1
    for j in range(len(data)):

        for i, place in enumerate(data[j]):

            # --------------------------------------------------------
            # Create content that will be embedded
            # --------------------------------------------------------

            content = (
                f"Name: {place['name']}, "
                f"City: {place['city']} "
                f"Region: {place['region']} "
                f"Services: {', '.join(place['services'])}. "
                f"Rating: {place['rating']} "
                f"Distance: {place['distance']} "
                f"Description: {place['description']}"
            )

            # --------------------------------------------------------
            # Create embedding
            # --------------------------------------------------------

            vector = model.embed_query(
                content
            )

            # Convert to float32 because FAISS expects float32
            vector = np.array(vector).astype("float32")

            vectors.append(vector)

            # --------------------------------------------------------
            # Create record
            # --------------------------------------------------------

            record = {
                "id": str(count),

                "vector": vector.tolist(),

                "metadata": {
                    "Category": cat[j],
                    "name": place["name"],
                    "city": place["city"],
                    "region": place["region"],
                    "services": place["services"],
                    "rating": str(place["rating"]),
                    "distance": place["distance"],
                    "description": place["description"],
                    "content": content
                }
            }

            embedding_records.append(record)

            count = count + 1

    return embedding_records, vectors