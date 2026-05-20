# AI-Powered Multi-Agent Credit Risk & Fraud Detection System

## Overview
An Agentic AI-powered multi-agent system for:

- Fraud Detection
- Credit Risk Assessment
- Audit & Compliance

The system uses **CrewAI**, **OpenAI**, **Adaptive Memory**, **RAG**, **Human-in-the-Loop**, and **Streamlit Dashboard** to automate intelligent banking decisions.

---

## Features

### Fraud Detection Agent
- Detects suspicious transactions
- Uses RAG-based fraud policies
- Risk scoring
- Human review escalation

### Credit Risk Agent
- Assesses customer creditworthiness
- Predicts loan/default risk
- Intelligent recommendations

### Audit Agent
- Generates compliance explanations
- Decision traceability
- Audit-ready reporting

### Dashboard
- KPI cards
- Fraud risk gauge
- Risk distribution charts
- Transaction analytics
- Multi-agent reports

### Human-in-the-Loop
High-risk transactions are escalated for manual review.

---

## Tech Stack

### AI / Agentic Framework
- CrewAI
- OpenAI API

### RAG & Memory
- Local Knowledge Base (.txt / PDF)
- Adaptive Memory
- ChromaDB (planned / optional)

### Frontend
- Streamlit
- Plotly
- Pandas

### Backend
- Python
- FastAPI (future extension)

### Reporting
- ReportLab (PDF generation)

---

## Project Structure

```text
credit-fraud-agentic-ai/
│── agents/
│── crews/
│── services/
│── memory/
│── rag/
│── ui/
│── reports/
│── human_loop/
│── README.md
│── architecture.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run ui/streamlit_app.py
```

---

## Future Enhancements
- Real-time APIs
- Kafka streaming
- ChromaDB semantic memory
- Model monitoring
- Docker deployment
- CI/CD
