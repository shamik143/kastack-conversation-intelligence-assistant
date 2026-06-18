import pandas as pd
import re

def parse_conversations(csv_path):

    df = pd.read_csv(csv_path)

    conversations = []

    global_msg_id = 1

    for conv_id, row in df.iterrows():

        conversation_text = str(row.iloc[0])

        lines = conversation_text.split("\n")

        messages = []

        local_msg_id = 1

        for line in lines:

            line = line.strip()

            if not line:
                continue

            match = re.match(
                r"(User\s*\d+):(.*)",
                line,
                re.IGNORECASE
            )

            if match:

                speaker = match.group(1)

                text = match.group(2).strip()

                messages.append({
                    "global_msg_id": global_msg_id,
                    "local_msg_id": local_msg_id,
                    "speaker": speaker,
                    "text": text
                })

                global_msg_id += 1
                local_msg_id += 1

        conversations.append({
            "conversation_id": conv_id + 1,
            "messages": messages
        })

    return conversations