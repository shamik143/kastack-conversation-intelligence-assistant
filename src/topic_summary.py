from collections import Counter
import re

STOPWORDS = {
    "the","a","an","is","are","and","or",
    "to","of","in","on","for","with",
    "i","you","it","that","this",
    "was","were","be","been","have",
    "has","had","do","does","did"
}

def summarize_topic(messages):

    text = " ".join(
        [m["text"] for m in messages]
    )

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text
    )

    if len(sentences) <= 2:
        return text[:300]

    words = re.findall(
        r"\w+",
        text.lower()
    )

    words = [
        w for w in words
        if w not in STOPWORDS
    ]

    freq = Counter(words)

    sentence_scores = {}

    for sentence in sentences:

        score = 0

        for word in re.findall(
            r"\w+",
            sentence.lower()
        ):

            score += freq.get(word, 0)

        sentence_scores[sentence] = score

    ranked = sorted(
        sentence_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top_sentences = [
        x[0]
        for x in ranked[:2]
    ]

    return " ".join(top_sentences)