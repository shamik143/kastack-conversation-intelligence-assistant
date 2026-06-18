from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

MIN_TOPIC_SIZE = 5
TOPIC_THRESHOLD = 0.40


def segment_conversation(messages):

    texts = [m["text"] for m in messages]

    if len(texts) <= MIN_TOPIC_SIZE:
        return [{
            "topic_id": 1,
            "start_msg": 1,
            "end_msg": len(texts)
        }]

    embeddings = model.encode(texts)

    topics = []

    start = 0
    topic_id = 1

    for i in range(3, len(texts)-1):

        previous_block = np.mean(
            embeddings[start:i],
            axis=0
        )

        next_block = np.mean(
            embeddings[i:i+3],
            axis=0
        )

        sim = cosine_similarity(
            [previous_block],
            [next_block]
        )[0][0]

        if sim < TOPIC_THRESHOLD:

            if (i - start) >= MIN_TOPIC_SIZE:

                topics.append({
                    "topic_id": topic_id,
                    "start_msg": start + 1,
                    "end_msg": i
                })

                topic_id += 1
                start = i

    topics.append({
        "topic_id": topic_id,
        "start_msg": start + 1,
        "end_msg": len(texts)
    })

    return topics