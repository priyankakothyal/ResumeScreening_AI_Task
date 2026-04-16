from chains.extraction_chain import run_extraction
from chains.matching_chain import run_matching
from chains.scoring_chain import run_scoring
from chains.explanation_chain import run_explanation

def load_file(path):
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    resume = load_file("data/resumes/weak.txt")
    job_desc = load_file("data/job_description.txt")

    # Step 1: Extraction
    extracted = run_extraction(resume)
    print("\n=== EXTRACTION ===\n", extracted)

    # Step 2: Matching
    matched = run_matching(extracted, job_desc)
    print("\n=== MATCHING ===\n", matched)

    # Step 3: Scoring
    score = run_scoring(matched)
    print("\n=== SCORE ===\n", score)

    # Step 4: Explanation
    explanation = run_explanation(extracted, matched, score)
    print("\n=== EXPLANATION ===\n", explanation)