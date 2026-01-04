from pydantic import BaseModel
from typing import List

class DecisionInput(BaseModel):
    loan_amount: float
    family_income: float
    student_score: float
    family_dependents: int
    college_type: str
    college_ranking: int
    course_type: str
    scholarship: str
    loan_interest_rate: float


class RiskResult(BaseModel):
    risk_score: float
    risk_level: str


class AuditReport(BaseModel):
    decision_summary: str
    risk_score: float
    risk_level: str
    explanation: str
    suggested_alternatives: List[str]
    guardrail: str
