from tools import compute_risk

# -------------------------
# Agent 1: Decision Parser
# -------------------------
def decision_parser(user_input: dict):
    """
    Extracts relevant features from user input.
    """
    required_fields = [
        "loan_amount",
        "family_income",
        "student_score",
        "family_dependents",
        "college_type",
        "college_ranking",
        "course_type",
        "scholarship",
        "loan_interest_rate"
    ]

    parsed_data = {key: user_input[key] for key in required_fields}
    return parsed_data


# -------------------------
# Agent 2: Risk Analysis Agent
# -------------------------
def risk_analysis_agent(parsed_data: dict):
    """
    Calls ML model to compute risk.
    """
    return compute_risk(parsed_data)


# -------------------------
# Agent 3: Final Auditor Agent
# -------------------------
from rag import retrieve_relevant_knowledge

def auditor_agent(parsed_data: dict, risk_result: dict):
    knowledge = retrieve_relevant_knowledge("education loan risk")

    explanation = (
        f"The decision has a {risk_result['risk_level']} risk. "
        f"Key factors include loan amount, income, and scholarship availability. "
        f"Relevant insights: {knowledge}"
    )

    if risk_result["risk_level"] == "High":
        alternatives = [
            "Consider reducing loan amount",
            "Explore government colleges",
            "Look for scholarships or financial aid"
        ]
    else:
        alternatives = ["Proceed with caution and monitor finances"]

    return {
        "decision_summary": "Education loan decision audit",
        "risk_score": risk_result["risk_score"],
        "risk_level": risk_result["risk_level"],
        "explanation": explanation,
        "suggested_alternatives": alternatives,
        "guardrail": "This is not professional financial advice."
    }
