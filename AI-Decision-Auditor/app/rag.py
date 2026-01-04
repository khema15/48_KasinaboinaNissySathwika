# Simple RAG implementation (conceptual)

EDUCATION_KNOWLEDGE_BASE = [
    "Education loan EMI should ideally be less than 20% of annual family income.",
    "Government colleges usually have lower tuition fees compared to private institutions.",
    "Scholarships significantly reduce long-term financial burden on students.",
    "High interest rates increase repayment risk over time.",
    "Students with strong academic scores have better chances of scholarships and aid."
]

def retrieve_relevant_knowledge(query: str, top_k: int = 2):
    """
    Retrieves relevant domain knowledge snippets based on keywords.
    This is a lightweight RAG simulation suitable for hackathon screening.
    """
    results = []

    for doc in EDUCATION_KNOWLEDGE_BASE:
        if any(word.lower() in doc.lower() for word in query.split()):
            results.append(doc)

    # fallback if nothing matches
    if not results:
        results = EDUCATION_KNOWLEDGE_BASE[:top_k]

    return results[:top_k]
