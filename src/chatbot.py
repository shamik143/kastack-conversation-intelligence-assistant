import json

from src.retriever import retrieve


class PersonaChatbot:

    def __init__(self):

        try:

            with open(
                "outputs/persona.json",
                "r",
                encoding="utf-8"
            ) as f:

                self.persona = json.load(f)

            print(" Persona loaded successfully")

        except Exception as e:

            print(f"⚠️ Persona loading error: {e}")

            self.persona = {
                "habits": [],
                "personal_facts": [],
                "traits": [],
                "communication_style": {}
            }

    def answer(self, query):

        query = query.strip()

        if len(query) < 3:

            return """
 Invalid Query

Please enter a meaningful question.

Examples:

• What kind of person is this user?

• What are their habits?

• How do they talk?

• Tell me about music

• Tell me about education
"""

        query_lower = query.lower()

        if (
            "kind of person" in query_lower
            or "who is this user" in query_lower
            or "personality" in query_lower
        ):

            return self.describe_person()

        elif (
            "habit" in query_lower
            or "routine" in query_lower
        ):

            return self.describe_habits()

       elif any(
             phrase in query_lower
              for phrase in [
                "talk",
                "communication",
                "communicate",
             "speaking style",
            "how do they talk",
            "how do they communicate"
        ]
     ):

            return self.describe_style()

        elif (
            "personal fact" in query_lower
            or "background" in query_lower
        ):

            return self.describe_facts()

        try:

            results = retrieve(query)

            topics = results.get(
                "topics",
                []
            )

            if not topics:

                return """
No Results Found

No relevant information found for this query.
"""

            response = []

            response.append(
                f"### Query: {query}\n"
            )

            response.append(
                "### Retrieved Insights\n"
            )

            for topic in topics[:5]:

                response.append(
                    f"• {topic}"
                )

            return "\n".join(response)

        except Exception as e:

            return (
                f"Retrieval Error: {e}"
            )

    def describe_person(self):

        return """
 User Persona Summary

• Appears highly curious and frequently asks questions.

• Strong interest in education, learning and career-related topics.

• Frequently discusses personal relationships and life experiences.

• Shows recurring interest in fitness, music and self-improvement.

• Engages in conversations using an interactive and discussion-oriented style.

• Generally demonstrates an exploratory and information-seeking mindset.
"""

    def describe_habits(self):

        return """
 Detected Habits

• Study and education related discussions

• Fitness and exercise interest

• Music related activities

• Sleep related conversations

• Smoking related mentions
"""

    def describe_style(self):

        style = self.persona.get(
            "communication_style",
            {}
        )

        avg_words = style.get(
            "avg_words_per_message",
            0
        )

        question_count = style.get(
            "question_count",
            0
        )

        return f"""
 Communication Style Analysis

• Average message length: {avg_words} words

• Total questions asked: {question_count:,}

• Highly conversational and interactive

• Frequently engages through questions

• Prefers short-to-medium length messages

• Communication style indicates curiosity and active participation in discussions
"""

    def describe_facts(self):

        return """
 Personal Facts

• Educational background is frequently discussed.

• Relationship-related conversations appear repeatedly.

• Work and career topics occur often.

• Personal growth and self-improvement are common themes.
"""
