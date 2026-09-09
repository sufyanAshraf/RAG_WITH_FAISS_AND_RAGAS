# from langchain_core.documents import Document

# from .model import Model


# def read_documents_from_file():
#     file_name = "docs_output.txt"
#     # Read from the text file
#     with open(file_name, "r", encoding="utf-8") as f:
#         read_content = f.read()

#     # Split the read_content by the separator to get individual document contents
#     doc_contents = read_content.split('\n---\n')

#     # Filter out any empty strings that might result from splitting (e.g., if file ends with separator)
#     doc_contents = [content.strip() for content in doc_contents if content.strip()]

#     # Reconstruct a list of Document objects. We'll use the same metadata structure as the original docs.
#     # Note: If original docs had varied metadata, this reconstruction would need to store/retrieve that metadata.
#     reconstructed_docs = []
#     for content in doc_contents:
#         # Assuming all original documents had the same source metadata as the first one for simplicity
#         # In a real scenario, if metadata varied, it would need to be saved/parsed from the file as well.
#         metadata = {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
#         reconstructed_docs.append(Document(page_content=content, metadata=metadata))

#     return reconstructed_docs


# __all__ = ["Model", "read_documents_from_file"]


# from pathlib import Path


# def read_documents_from_file(
#     file_name="docs_output.txt",
#     category_name="agents",
#     additional_tags=None,
# ):
#     """Load text chunks with searchable and filterable document tags."""
#     additional_tags = additional_tags or []
#     if isinstance(additional_tags, str):
#         additional_tags = [additional_tags]

#     file_name_tag = Path(file_name).name
#     tags = [file_name_tag, category_name, *additional_tags]
#     tag_header = "Tags: " + ", ".join(tag for tag in tags if tag)

#     # Read from the text file
#     with open(file_name, "r", encoding="utf-8") as f:
#         read_content = f.read()

#     # Split the read_content by the separator to get individual document contents
#     doc_contents = read_content.split('\n---\n')

#     # Filter out any empty strings that might result from splitting (e.g., if file ends with separator)
#     doc_contents = [content.strip() for content in doc_contents if content.strip()]

#     # Store tags as metadata for filtering and include them in page_content so
#     # the embedding model can use them during similarity search.
#     reconstructed_docs = []
#     for content in doc_contents:
#         metadata = {
#             "source": "https://lilianweng.github.io/posts/2023-06-23-agent/",
#             "file_name": file_name_tag,
#             "category": category_name,
#             "tags": list(additional_tags),
#         }
#         reconstructed_docs.append(
#             Document(
#                 page_content=f"{tag_header}\n\n{content}",
#                 metadata=metadata,
#             )
#         )

#     return reconstructed_docs