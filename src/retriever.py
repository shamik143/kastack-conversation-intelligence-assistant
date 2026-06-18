import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


print("Loading topic summaries...")

with open(
    "outputs/topic_summaries.json",
    "r",
    encoding="utf-8"
) as f:

    TOPICS = json.load(f)

print("Loading embedding model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = [
    t["summary"]
    for t in TOPICS
]

embeddings = model.encode(
    documents,
    show_progress_bar=False
)


def retrieve(
    query,
    top_k=5
):

    query_embedding = model.encode(
        [query]
    )

    scores = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    ranked = sorted(
        zip(
            documents,
            scores
        ),
        key=lambda x: x[1],
        reverse=True
    )

    return {
        "topics": [
            doc
            for doc, _
            in ranked[:top_k]
        ]
    }
