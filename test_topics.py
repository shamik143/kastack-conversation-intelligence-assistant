from src.parser import parse_conversations
from src.topic_segmenter import segment_conversation

conversations = parse_conversations(
    "data/conversations.csv"
)

conv = conversations[0]

topics = segment_conversation(
    conv["messages"]
)

print(topics)