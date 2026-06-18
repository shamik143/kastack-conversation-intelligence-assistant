from src.retriever import generate_answer

queries = [
    "college student",
    "music band",
    "relationship",
    "fitness",
    "cars"
]

for q in queries:

    print("\n")
    print("=" * 60)

    result = generate_answer(q)

    print(result)