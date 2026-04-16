from langchain_core.prompts import PromptTemplate

scoring_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
You are an AI evaluator.

Based on the matching result, assign a score from 0 to 100.

Higher match = higher score.

Match Data:
{match_data}

Return ONLY the number.
"""
)