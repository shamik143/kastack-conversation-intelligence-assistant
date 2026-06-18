import json
from sentence_transformers import SentenceTransformer
from src.vector_store import topic_collection

# Load once
model = SentenceTransformer("all-MiniLM-L6-v2")


def index_topics(json_file):

    print("Loading topic summaries...")

    with open(
        json_file,
        "r",
        encoding="utf-8"
    ) as f:

        topics = json.load(f)

    print(f"Total topics found: {len(topics)}")

    # For assignment demo
    topics = topics[:5000]

    print(f"Indexing first {len(topics)} topics")

    ids = []
    documents = []
    metadatas = []

    for topic in topics:

        ids.append(
            f"conv_{topic['conversation_id']}_topic_{topic['topic_id']}"
        )

        documents.append(
            topic["summary"]
        )

        metadatas.append({
            "conversation_id":
            topic["conversation_id"],

            "topic_id":
            topic["topic_id"],

            "start_msg":
            topic["start_msg"],

            "end_msg":
            topic["end_msg"]
        })

    print("Generating embeddings...")

    embeddings = model.encode(
        documents,
        batch_size=64,
        show_progress_bar=True
    ).tolist()

    print("Embeddings generated.")

    BATCH_SIZE = 1000

    for i in range(0, len(ids), BATCH_SIZE):

        topic_collection.add(
            ids=ids[i:i+BATCH_SIZE],
            documents=documents[i:i+BATCH_SIZE],
            metadatas=metadatas[i:i+BATCH_SIZE],
            embeddings=embeddings[i:i+BATCH_SIZE]
        )

        print(
            f"Indexed {min(i+BATCH_SIZE, len(ids))}/{len(ids)}"
        )

    print("Indexing completed.")