Agentic Credit Guardian
Multi-Agent Credit Risk & Fraud Detection System

An autonomous AI system that evaluates corporate creditworthiness using multi-agent orchestration (CrewAI), semantic RAG (FAISS), fraud detection ML models, and adaptive memory, all wrapped in an interactive Streamlit dashboard.

🚀 Project Overview

Agentic Credit Guardian is an AI-powered credit risk auditing system that simulates how financial institutions evaluate companies for lending decisions.

Instead of using a single model, the system uses multiple specialized AI agents:

📈 Financial Quant Agent → analyzes structured financial data
📄 Research Agent → extracts insights from audit PDFs using RAG
🕵️ Fraud Detection Agent → identifies anomalies using ML
⚖️ Auditor Agent → makes final GO / NO-GO decision
🧠 Memory Layer → stores past cases for learning patterns
🎯 Key Features
🧠 Multi-Agent AI System

Built using CrewAI, where each agent has a specialized role:

Financial analysis
Document intelligence
Fraud detection
Final decision-making
📊 Credit Risk Scoring

Computes:

Debt-to-Equity ratio
Liquidity ratios
Cash flow stability
Credit score estimation
📄 RAG-based Document Intelligence
Uses FAISS vector database
Extracts insights from PDF audit reports
Detects:
hidden liabilities
lawsuits
financial irregularities
🕵️ Fraud Detection Engine
Isolation Forest ML model
Detects anomalies in:
revenue
debt structure
cash flow inconsistencies
🧠 Adaptive Memory
Stores past audit cases
Retrieves similar financial risk patterns
Improves reasoning over time
🌐 Interactive Streamlit Dashboard
Select company
Run AI audit
View:
financial KPIs
fraud flags
final recommendation
agent execution trace
⚡ FastAPI Market Data Layer

Simulates live financial conditions:

sector-based interest rates
dynamic risk adjustments
🏗️ System Architecture
                ┌────────────────────┐
                │   Streamlit UI     │
                └─────────┬──────────┘
                          │
                          ▼
             ┌────────────────────────┐
             │ CrewAI Orchestrator    │
             │ (Auditor Agent)        │
             └─────────┬──────────────┘
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
┌────────────┐ ┌────────────┐ ┌──────────────┐
│ Quant Agent │ │ Research   │ │ Fraud Agent  │
│ KPI Engine  │ │ RAG PDFs   │ │ ML Detection │
└──────┬──────┘ └──────┬─────┘ └──────┬───────┘
       ▼               ▼               ▼
┌────────────┐ ┌────────────┐ ┌──────────────┐
│ CSV Data   │ │ FAISS DB   │ │ ML Model     │
└────────────┘ └────────────┘ └──────────────┘
🧰 Tech Stack
Layer	Technology
Orchestration	CrewAI
UI	Streamlit
RAG	FAISS + LangChain
Embeddings	OpenAI / SentenceTransformers
ML Fraud Detection	Scikit-learn (Isolation Forest)
API Layer	FastAPI
Memory	Custom Adaptive Memory (extendable to vector DB)
Data Generation	Faker + NumPy
PDF Parsing	PyMuPDF
Backend	Python 3.10+
📂 Project Structure
credit/
│
├── agents/
│   ├── quant_agent.py
│   ├── research_agent.py
│   ├── fraud_agent.py
│   ├── auditor_agent.py
│   ├── crew_setup.py
│
├── orchestration/
│   ├── graph.py
│
├── rag/
│   ├── embedding_pipeline.py
│   ├── retriever.py
│
├── memory/
│   ├── adaptive_memory.py
│
├── ml/
│   ├── fraud_model.py
│
├── api/
│   ├── market_api.py
│
├── data/
│   ├── financials.csv
│   ├── audit_reports/
│
├── ui/
│   ├── app.py
│
├── main.py
└── requirements.txt
⚙️ Installation & Setup
1️⃣ Clone Project
git clone https://github.com/your-username/agentic-credit-guardian.git
cd agentic-credit-guardian
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Generate Synthetic Data
python data/generate_dataset.py
python data/generate_reports.py
4️⃣ Build Vector DB
python rag/embedding_pipeline.py
5️⃣ Run Streamlit App
streamlit run ui/app.py
6️⃣ Run FastAPI Server (optional)
uvicorn api.market_api:app --reload
🧪 Example Workflow
User selects a company in Streamlit
Quant Agent computes financial KPIs
Research Agent retrieves PDF insights via RAG
Fraud Agent detects anomalies
Auditor Agent makes final decision
Output Example:
{
  "company": "ABC Corp",
  "risk_level": "HIGH",
  "fraud_flags": true,
  "recommendation": "NO-GO",
  "reason": [
    "High leverage ratio",
    "Hidden liabilities detected",
    "Cash flow inconsistency"
  ]
}
📊 Evaluation Metrics
RAGAS scoring:
faithfulness
answer relevance
ML evaluation:
anomaly detection precision
System evaluation:
audit consistency
decision explainability
🔐 Security Features
Input sanitization
Prompt injection protection (extendable via LLM Guard)
PII masking (synthetic safe dataset only)
📌 Future Improvements
GraphRAG integration
LangGraph full orchestration
Real banking dataset integration
Advanced fraud transformer model
Multi-tenant audit system
LangSmith tracing dashboard
👨‍💻 Author Notes

This project simulates a real-world AI underwriting system used in banking and fintech for:

Credit risk scoring
Fraud detection
Financial document intelligence
Automated auditing
⭐ Impact

This project demonstrates:

Multi-agent AI systems
RAG pipelines
ML + LLM hybrid reasoning
Production-style AI architecture
