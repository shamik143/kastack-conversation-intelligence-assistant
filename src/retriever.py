import json


with open(
    "outputs/topic_summaries.json",
    "r",
    encoding="utf-8"
) as f:

    TOPICS = json.load(f)


def retrieve(query):

    query = query.lower()

    matches = []

    for topic in TOPICS:

        summary = topic.get(
            "summary",
            ""
        )

        if query in summary.lower():

            matches.append(
                summary
            )

    if not matches:

        # fallback retrieval

        for topic in TOPICS[:20]:

            summary = topic.get(
                "summary",
                ""
            )

            if len(summary) > 20:

                matches.append(
                    summary
                )

        return {
            "topics": matches[:5]
        }

    return {
        "topics": matches[:5]
    }
