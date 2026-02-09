from pydantic import BaseModel, Field
from typing import Optional, List

# ----------------------------------------------------------------------------
# COMPLIANCE & SAFETY MODELS (Sanitation Layer)
# ----------------------------------------------------------------------------
class KillSwitchResult(BaseModel):
    """
    Structured output for the Kill Switch Protocol.
    Captures the binary GO/NO-GO decision and the specific gate that failed.
    """
    decision: str = Field(
        ..., 
        description="Final decision: 'PASS' if safe, 'KILL' if violated."
    )
    gate_failed: Optional[int] = Field(
        None, 
        description="The number of the Hard Gate that failed (1-4). Null if PASS."
    )
    gate_name: Optional[str] = Field(
        None, 
        description="Name of the failed gate (e.g., 'Illegal Activities'). Null if PASS."
    )
    reason: str = Field(
        ..., 
        description="Detailed explanation of WHY the decision was made."
    )
    evidence: Optional[str] = Field(
        None, 
        description="Concrete proof (e.g., law citation, trademark ID). Null if PASS."
    )

# ----------------------------------------------------------------------------
# STRATEGIC MODELS (Board Layer)
# ----------------------------------------------------------------------------
class BoardDecision(BaseModel):
    """
    Structured output for the Final Board Decision.
    """
    decision: str = Field(
        ..., 
        description="Outcome: 'APPROVED', 'REJECTED', or 'REVISE'."
    )
    rationale: str = Field(
        ..., 
        description="The strategic reasoning behind the decision."
    )
    success_criteria: Optional[List[str]] = Field(
        None, 
        description="List of top 3 success criteria if APPROVED."
    )
