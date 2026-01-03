 **AI Decision Auditor**  
**Auditing Human Decisions using ML-backed Risk Analysis and Agentic AI**

 1. Problem Statement

Human decision-making in critical domains such as **education, finance, and healthcare** is often influenced by incomplete information, emotional bias, and lack of quantitative risk awareness.  

While Large Language Models (LLMs) like ChatGPT and Gemini can provide general advice, they:
- Do not quantify decision risk using data
- Do not audit decisions systematically
- Do not enforce domain-specific guardrails
- Provide unstructured, non-reproducible outputs

There is a need for an **AI system that does not replace human decisions**, but instead **audits them**, highlighting risks, biases, and safer alternatives using both **Machine Learning and Generative AI**.

---

 2. Proposed Solution

We propose **AI Decision Auditor**, a hybrid AI system that evaluates a human decision and produces a **structured audit report**.

The system:
- Accepts a user’s decision and context
- Computes a **quantitative risk score** using Machine Learning
- Uses **multi-agent Generative AI** to analyze bias and reasoning
- Retrieves trusted domain knowledge using **Retrieval Augmented Generation (RAG)**
- Produces an **explainable, evidence-backed audit report**

This approach positions AI as a **decision reviewer**, not a decision maker.

---

3. Key Innovation

Unlike traditional chatbots or recommender systems:

- The system **audits an existing decision**
- Combines **ML (risk scoring)** with **LLMs (reasoning & explanation)**
- Uses **agentic architecture**, where each agent has a specialized role
- Emphasizes **Responsible AI** through guardrails and disclaimers

This makes the project innovative, explainable, and aligned with real-world AI governance principles.

---

4. System Architecture

User Decision Input
↓
Decision Parsing Agent
↓
ML Risk Scoring Tool
↓
Bias Detection Agent
↓
RAG Knowledge Retrieval
↓
Alternative Scenario Generator
↓
Final Decision Audit Report


Each component is independently testable and reproducible.

---

## 5. Technologies Used

### Machine Learning
- Logistic Regression / Decision Tree
- Used to compute a **risk probability score**
- Implemented using `scikit-learn`

### Generative AI
- Large Language Models (OpenAI / Gemini / Local LLM)
- Used for reasoning, explanation, and bias detection

### Agentic AI
- Multi-agent pipeline implemented using **LangChain**
- Agents communicate through structured tool outputs

### Retrieval Augmented Generation (RAG)
- Domain documents embedded using vector embeddings
- Stored and retrieved using **ChromaDB**
- Improves factual accuracy and reduces hallucinations

### Guardrails
- Input validation
- Output constraints
- Ethical disclaimers (e.g., “Not professional advice”)

---

## 6. Domain and Dataset

### Initial Domain: Education

Example decision:
> “I want to take an education loan of ₹8 lakhs to study engineering in a private college.”

Datasets used:
- Student performance / education outcome datasets (Kaggle or public sources)
- Domain knowledge documents (career guidance reports, policy documents)

The system is **domain-agnostic** and can be extended to finance or healthcare.

---

## 7. Output Format

The system produces a **structured audit report**:

```json
{
  "decision_summary": "Education loan for private engineering college",
  "risk_score": 0.72,
  "risk_level": "High",
  "identified_biases": ["financial stress bias", "brand name bias"],
  "alternative_options": [
    "Consider government colleges",
    "Explore scholarships or lower loan amount"
  ],
  "explanation": "The loan EMI exceeds recommended income thresholds...",
  "guardrails": "This is not professional advice"
}

The system follows a modular, agent-based architecture.
```
8. Evaluation Strategy
-ML Model Evaluation
-Risk probability analysis
-Sanity checks on edge cases
-LLM Output Evaluation
-Manual review
-Prompt-based consistency checks
-System Robustness
-Invalid input testing
-Extreme decision scenarios

9.Limitations
-Risk scores depend on dataset quality
-Bias detection is partially heuristic
-Not a replacement for professional advice

