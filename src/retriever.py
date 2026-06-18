from src.vector_store import (
    topic_collection,
    checkpoint_collection,
    message_collection
)


def retrieve_topics(query, top_k=5):
    """
    Retrieve relevant topic summaries.
    """

    results = topic_collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results


def retrieve_checkpoints(query, top_k=3):
    """
    Retrieve relevant 100-message checkpoints.
    """

    results = checkpoint_collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results


def retrieve_messages(query, top_k=5):
    """
    Retrieve raw message chunks.
    """

    results = message_collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results


def retrieve(query, top_k=5):
    """
    Hierarchical retrieval.

    1. Topic summaries
    2. Checkpoints
    3. Message chunks
    """

    response = {
        "topics": [],
        "checkpoints": [],
        "messages": []
    }

    try:

        topic_results = topic_collection.query(
            query_texts=[query],
            n_results=top_k
        )

        response["topics"] = topic_results.get(
            "documents",
            [[]]
        )[0]

    except Exception as e:

        print(
            f"Topic retrieval error: {e}"
        )

    try:

        checkpoint_results = checkpoint_collection.query(
            query_texts=[query],
            n_results=min(3, top_k)
        )

        response["checkpoints"] = checkpoint_results.get(
            "documents",
            [[]]
        )[0]

    except Exception as e:

        print(
            f"Checkpoint retrieval error: {e}"
        )

    try:

        message_results = message_collection.query(
            query_texts=[query],
            n_results=top_k
        )

        response["messages"] = message_results.get(
            "documents",
            [[]]
        )[0]

    except Exception as e:

        print(
            f"Message retrieval error: {e}"
        )

    return response


def generate_answer(query):
    """
    Simple RAG response generation.
    """

    results = retrieve(query)

    answer = []

    answer.append(
        f"Query: {query}\n"
    )

    if results["topics"]:

        answer.append(
            "\nRelevant Topics:\n"
        )

        for topic in results["topics"][:3]:

            answer.append(
                f"- {topic}"
            )

    if results["checkpoints"]:

        answer.append(
            "\nRelevant Checkpoints:\n"
        )

        for checkpoint in results["checkpoints"][:2]:

            answer.append(
                f"- {checkpoint}"
            )

    if results["messages"]:

        answer.append(
            "\nRelevant Messages:\n"
        )

        for message in results["messages"][:3]:

            answer.append(
                f"- {message}"
            )

    return "\n".join(answer)