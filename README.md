# Conversation Intelligence Assistant

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system over conversation data. The system processes conversations chronologically, detects topic transitions, generates topic checkpoints, extracts user persona information, and provides a chatbot interface for semantic retrieval and user analysis.

The solution was developed as part of the KaStack Labs AI/ML Engineer Intern assignment.

---

## Dataset Statistics

* Total Conversations: 11,000
* Total Messages: 191,578
* Topic Checkpoints Generated: 25,516
* 100-Message Checkpoints Generated: 1,916

---

## System Architecture

Conversation Dataset (CSV)
↓
Chronological Parser
↓
Topic Segmentation
↓
Topic Checkpoints
↓
Topic Summaries
↓
ChromaDB Vector Store
↓
Persona Extraction
↓
Semantic Retrieval Layer
↓
Chatbot Interface (Streamlit)

---

## Part 1: Topic Checkpoints & RAG System

### Topic Segmentation

The system processes conversations in chronological order.

Semantic embeddings are generated using SentenceTransformers (`all-MiniLM-L6-v2`).

Topic changes are detected by measuring semantic drift between consecutive groups of messages. Whenever similarity drops below a threshold, a new topic checkpoint is created.

Each checkpoint stores:

* Topic ID
* Start Message
* End Message
* Topic Summary

Example:

* Topic 1 → Messages 1–25 → Summary
* Topic 2 → Messages 26–60 → Summary
* Topic 3 → Messages 61–90 → Summary

### 100 Message Checkpoints

Independent summaries are generated every 100 chronological messages across the dataset.

These checkpoints are separate from topic segmentation and provide long-range context summaries.

---

## Part 2: Persona Extraction

The system extracts persona information from explicit conversational evidence.

### Extracted Persona Categories

#### Habits

Examples:

* Study-related discussions
* Fitness and exercise
* Music-related activities
* Sleep-related conversations
* Smoking-related mentions

#### Personal Facts

Examples:

* Education-related information
* Relationship discussions
* Career and work-related information

#### Personality Traits

Examples:

* Curiosity
* Information-seeking behavior
* Interactive engagement

#### Communication Style

Metrics include:

* Average words per message
* Question frequency
* Conversational characteristics

Persona data is stored in structured JSON format.

---

## Part 3: Chatbot

The chatbot supports both persona analysis and semantic retrieval.

### Persona Questions

Examples:

* What kind of person is this user?
* What are their habits?
* How do they talk?

### Semantic Retrieval Questions

Examples:

* Tell me about music
* Tell me about cars
* Tell me about education
* Tell me about relationships
* Tell me about fitness

The chatbot retrieves relevant topic summaries from ChromaDB and presents the most relevant conversational context.

---

## Retrieval Pipeline

1. User submits a query.
2. Query is embedded using SentenceTransformers.
3. ChromaDB performs semantic similarity search.
4. Relevant topic summaries are retrieved.
5. Retrieved information is returned to the chatbot.

This approach enables semantic retrieval rather than keyword matching.

---

## Technologies Used

* Python
* Sentence Transformers
* ChromaDB
* Transformers
* Pandas
* JSON
* Streamlit

---

## Project Structure

```text
kastack-assignment/
│
├── app.py
├── requirements.txt
├── README.md
│
├── outputs/
│   ├── persona.json
│   └── topic_summaries.json
│
├── src/
│   ├── parser.py
│   ├── topic_segmenter.py
│   ├── build_topics.py
│   ├── checkpoint_builder.py
│   ├── persona_extractor.py
│   ├── retriever.py
│   ├── chatbot.py
│   └── vector_store.py
│
└── tests/
```

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate persona:

```bash
python save_persona.py
```

Generate topic summaries:

```bash
python build_dataset.py
```

Index summaries:

```bash
python index_all_topics.py
```

Run the chatbot:

```bash
streamlit run app.py
```

---

## Future Improvements

* LLM-based answer synthesis over retrieved summaries
* More advanced persona extraction
* Hybrid retrieval using summaries and raw message chunks
* Dynamic topic segmentation thresholds
* Multi-user conversation analytics
