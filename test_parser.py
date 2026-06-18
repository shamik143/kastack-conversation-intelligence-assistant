from src.parser import parse_conversations

conversations = parse_conversations(
    "data/conversations.csv"
)

print("Total conversations:",
      len(conversations))

print()

print("Conversation 1:")
print(conversations[0])