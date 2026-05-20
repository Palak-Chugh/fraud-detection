# Architecture Document

## High-Level Architecture

```text
User Input
     ↓
Streamlit Dashboard
     ↓
Master Crew
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
Fraud Agent   Credit Agent   Audit Agent
 ↓               ↓               ↓
RAG          Adaptive Memory  Compliance Rules
 ↓               ↓               ↓
Human Review Decision Logic
     ↓
Executive PDF Report
```

---

## Multi-Agent Workflow

### 1. Fraud Agent
Responsibilities:
- Fraud risk detection
- Suspicious pattern analysis
- RAG-based policy validation
- Human escalation

Input:
- Transaction data

Output:
- Fraud score
- Risk level
- Recommendation

---

### 2. Credit Risk Agent
Responsibilities:
- Creditworthiness analysis
- Default prediction
- Financial behavior assessment

Input:
- Customer financial profile

Output:
- Credit risk category
- Confidence score
- Recommendation

---

### 3. Audit Agent
Responsibilities:
- Compliance validation
- Decision traceability
- Explainability

Input:
- Fraud + Credit decisions

Output:
- Audit summary
- Compliance report

---

## Human-in-the-Loop

```text
IF Fraud Score > Threshold
        ↓
Manual Review
        ↓
Approve / Reject / Need More Info
```

---

## RAG Architecture

```text
Knowledge Base
(.txt / PDFs)
      ↓
Retriever
      ↓
Context Injection
      ↓
Agent Reasoning
```

---

## Adaptive Memory

```text
Past Cases
     ↓
Similarity Retrieval
     ↓
Decision Context
```

---

## Tech Stack

| Layer | Technology |
|--------|-------------|
| AI Agents | CrewAI |
| LLM | OpenAI |
| Frontend | Streamlit |
| Visualization | Plotly |
| Data | Pandas |
| RAG | Local Files / ChromaDB |
| Memory | Adaptive Memory |
| Reporting | ReportLab |
| API | FastAPI |
| Language | Python |

---

## Deployment (POC)

```text
Local Machine
      ↓
Streamlit UI
      ↓
OpenAI API
      ↓
Local RAG + Memory
```

---

## Scalability Vision

Future production architecture:

```text
Microservices
      ↓
Kafka Event Streaming
      ↓
Vector DB
      ↓
Cloud Deployment
      ↓
Monitoring & Observability
```
