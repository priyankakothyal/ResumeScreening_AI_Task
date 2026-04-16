def run_matching(resume_data, job_description):

    jd_skills = []
    jd_lines = job_description.lower().split("\n")

    for line in jd_lines:
        if "skills:" in line:
            jd_skills = line.replace("skills:", "").strip().split(",")
            jd_skills = [s.strip().capitalize() for s in jd_skills]

    matched = list(set(resume_data["skills"]) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_data["skills"]))

    match_percentage = int((len(matched) / len(jd_skills)) * 100)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": match_percentage
    }