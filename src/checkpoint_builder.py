from src.topic_summary import summarize_topic

def build_100_message_checkpoints(messages):

    checkpoints = []

    checkpoint_id = 1

    for i in range(0, len(messages), 100):

        chunk = messages[i:i+100]

        summary = summarize_topic(chunk)

        checkpoints.append({
            "checkpoint_id": checkpoint_id,
            "start_msg": chunk[0]["global_msg_id"],
            "end_msg": chunk[-1]["global_msg_id"],
            "summary": summary
        })

        checkpoint_id += 1

    return checkpoints