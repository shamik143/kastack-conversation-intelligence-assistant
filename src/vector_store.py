import chromadb

client = chromadb.PersistentClient(
    path="storage/chroma"
)

topic_collection = client.get_or_create_collection(
    name="topics"
)

checkpoint_collection = client.get_or_create_collection(
    name="checkpoints"
)

message_collection = client.get_or_create_collection(
    name="messages"
)