from src.topic_segmenter import segment_conversation
from src.topic_summary import summarize_topic

def build_topic_checkpoints(conversation):

    topics = segment_conversation(
        conversation["messages"]
    )

    topic_results = []

    for topic in topics:

        start_idx = topic["start_msg"] - 1
        end_idx = topic["end_msg"]

        msgs = conversation["messages"][
            start_idx:end_idx
        ]

        summary = summarize_topic(msgs)

        topic_results.append({
            "conversation_id":
            conversation["conversation_id"],

            "topic_id":
            topic["topic_id"],

            "start_msg":
            topic["start_msg"],

            "end_msg":
            topic["end_msg"],

            "summary":
            summary
        })

    return topic_results