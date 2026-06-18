import json

from src.parser import parse_conversations
from src.persona_extractor import extract_persona

print("Loading conversations...")

conversations = parse_conversations(
    "data/conversations.csv"
)

all_messages = []

for conv in conversations:

    all_messages.extend(
        conv["messages"]
    )

print(
    f"Messages loaded: {len(all_messages)}"
)

persona = extract_persona(
    all_messages
)

with open(
    "outputs/persona.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        persona,
        f,
        indent=2
    )

print("Persona saved.")
print(persona)