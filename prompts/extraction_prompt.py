from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Resume:
{resume}

Task:
Extract skills, tools, and experience.

Answer ONLY in this format:

Skills: ...
Tools: ...
Experience: ...

Do not repeat the question.
"""
)