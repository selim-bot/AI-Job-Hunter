WEIGHTS = {
    "skills": 0.40,
    "education": 0.20,
    "experience": 0.20,
    "role": 0.10,
    "location": 0.10,
}


def calculate_match(score_components: dict) -> float:
    """Each component must be a score between 0 and 100."""
    return round(sum(score_components[k] * w for k, w in WEIGHTS.items()), 2)


def skill_overlap(candidate_skills: list[str], job_text: str) -> float:
    if not candidate_skills:
        return 0.0
    text = job_text.lower()
    hits = sum(1 for s in candidate_skills if s.lower() in text)
    return round(100 * hits / len(candidate_skills), 2)
