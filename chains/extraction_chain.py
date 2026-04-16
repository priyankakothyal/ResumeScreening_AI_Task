def run_extraction(resume_text):
    skills = []
    tools = []
    experience = ""

    lines = resume_text.split("\n")

    for line in lines:
        line = line.lower()

        if "skills:" in line:
            skills = line.replace("skills:", "").strip().split(",")
            skills = [s.strip().capitalize() for s in skills]

        if "tools:" in line:
            tools = line.replace("tools:", "").strip().split(",")
            tools = [t.strip().capitalize() for t in tools]

        if "experience" in line:
            experience = line.strip()

    return {
        "skills": skills,
        "tools": tools,
        "experience": experience
    }