from src.parser import parse_conversations
from src.checkpoint_builder import build_100_message_checkpoints

conversations = parse_conversations(
    "data/conversations.csv"
)

all_messages = []

for conv in conversations:
    all_messages.extend(
        conv["messages"]
    )

checkpoints = build_100_message_checkpoints(
    all_messages
)

print("Total checkpoints:",
      len(checkpoints))

print()

print(checkpoints[0])