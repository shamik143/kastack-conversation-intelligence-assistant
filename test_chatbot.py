from src.chatbot import PersonaChatbot

bot = PersonaChatbot()

queries = [

    "What kind of person is this user?",

    "What are their habits?",

    "How do they talk?",

    "Tell me about music",

    "Tell me about cars"
]

for q in queries:

    print("\n")
    print("=" * 60)

    print("QUESTION:")
    print(q)

    print("\nANSWER:")

    print(
        bot.answer(q)
    )