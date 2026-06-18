from src.parser import parse_conversations
from src.build_topics import build_topic_checkpoints

conversations = parse_conversations(
    "data/conversations.csv"
)

results = build_topic_checkpoints(
    conversations[0]
)

for topic in results:

    print("\n----------------")
    print(topic)