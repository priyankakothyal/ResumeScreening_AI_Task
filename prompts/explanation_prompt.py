from langchain_core.prompts import PromptTemplate

explanation_prompt = PromptTemplate(
    input_variables=["resume_data", "match_data", "score"],
    template="""
Explain why the candidate received this score.

Include:
- Strengths
- Weaknesses
- Missing skills

Candidate:
{resume_data}

Match:
{match_data}

Score:
{score}

Keep it simple and clear.
"""
)