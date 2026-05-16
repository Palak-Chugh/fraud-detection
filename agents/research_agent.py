 # pip install pymupdf
import fitz

class ResearchAgent:

    def read_report(self, pdf_path):

        doc = fitz.open(pdf_path)

        text = ""

        for page in doc:
            text += page.get_text()

        findings = []

        keywords = [
            "undisclosed liability",
            "irregular financial transactions",
            "offshore subsidiary"
        ]

        for keyword in keywords:
            if keyword.lower() in text.lower():
                findings.append(keyword)

        return {
            "findings": findings,
            "report_excerpt": text[:1000]
        }


def retriever_agent(company_data):
    agent = ResearchAgent()
    pdf_path = company_data.get("pdf_path", "data/sample_report.pdf")  # fallback path
    return agent.read_report(pdf_path)
