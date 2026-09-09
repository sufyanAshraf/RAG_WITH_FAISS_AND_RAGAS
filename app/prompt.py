import json
def buildContext(relevant_docs):  
    context = json.dumps(relevant_docs, indent=2)
    return context


def getPrompt(query, relevant_docs):
    context = buildContext(relevant_docs)
    full_prompt = f"""
        You are a helpful AI assistant.

        Answer the user's question using the provided context.

        Context:
        {context}

        Question:
        {query}

        Answer:


        Do not:
        - Wrap the response in single or double quotes.
        - Return escaped characters such as \n or \u202f.
        - Include unnecessary introductory or closing remarks.
        - Use Unicode spaces.

        Use normal spaces and newlines.
        """
    return full_prompt