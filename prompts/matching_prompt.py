from langchain_core.prompts import PromptTemplate

matching_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
You are an AI recruiter.

Compare the candidate profile with the job description.

Return:
- matched_skills
- missing_skills
- match_percentage (0-100)

Candidate:
{resume_data}

Job Description:
{job_description}

RULES:
- Do NOT assume skills
- Keep it accurate
- Output in JSON
"""
)