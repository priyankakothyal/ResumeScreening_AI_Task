def run_explanation(resume_data, match_data, score):

    explanation = f"""
Candidate Score: {score}/100

Strengths:
{', '.join(match_data['matched_skills'])}

Missing Skills:
{', '.join(match_data['missing_skills'])}

Experience:
{resume_data['experience']}
"""

    return explanation