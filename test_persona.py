import json

from src.parser import parse_conversations
from src.persona_extractor import extract_persona

conversations = parse_conversations(
    "data/conversations.csv"
)

all_messages = []

for conv in conversations:
    all_messages.extend(
        conv["messages"]
    )

persona = extract_persona(
    all_messages
)

print(
    json.dumps(
        persona,
        indent=2
    )
)