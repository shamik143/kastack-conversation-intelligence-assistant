import re
from collections import Counter

def extract_persona(messages):

    text = " ".join(
        [m["text"] for m in messages]
    ).lower()

    persona = {
        "habits": [],
        "personal_facts": [],
        "traits": [],
        "communication_style": {}
    }

    habit_patterns = {
        "sleep": r"sleep|wake up|bed",
        "fitness": r"gym|workout|exercise|yoga|run",
        "study": r"study|college|student|exam",
        "music": r"music|band|guitar|song",
        "smoking": r"smoke|cigarette"
    }

    for habit, pattern in habit_patterns.items():

        if re.search(pattern, text):
            persona["habits"].append(habit)

    fact_patterns = {
        "relationship":
        r"girlfriend|boyfriend|wife|husband",

        "student":
        r"college|student|university",

        "job":
        r"job|internship|work"
    }

    for fact, pattern in fact_patterns.items():

        if re.search(pattern, text):
            persona["personal_facts"].append(fact)

    question_count = text.count("?")

    if question_count > 100:
        persona["traits"].append(
            "curious"
        )

    avg_words = sum(
        len(m["text"].split())
        for m in messages
    ) / len(messages)

    persona["communication_style"] = {
        "avg_words_per_message":
        round(avg_words,2),

        "question_count":
        question_count
    }

    return persona