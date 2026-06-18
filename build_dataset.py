import json
import os

from src.parser import parse_conversations
from src.build_topics import build_topic_checkpoints

os.makedirs("outputs", exist_ok=True)

print("Loading conversations...")

conversations = parse_conversations(
    "data/conversations.csv"
)

print("Total conversations:", len(conversations))

all_topics = []

for idx, conversation in enumerate(conversations):

    topics = build_topic_checkpoints(
        conversation
    )

    all_topics.extend(topics)

    if idx % 500 == 0:
        print(
            f"Processed {idx}/{len(conversations)} conversations"
        )

print(
    "Total Topics:",
    len(all_topics)
)

with open(
    "outputs/topic_summaries.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_topics,
        f,
        indent=2,
        ensure_ascii=False
    )

print(
    "Saved outputs/topic_summaries.json"
)