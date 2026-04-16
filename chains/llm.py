from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

def load_llm():
    pipe = pipeline(
        "text-generation",
        model="gpt2",
        max_new_tokens=200,
        temperature=0.3
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    return llm