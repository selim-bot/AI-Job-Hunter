import sys
sys.path.insert(0, "backend")

from app.services.job_matcher import calculate_match


def test_calculate_match():
    s = {"skills": 100, "education": 100, "experience": 100, "role": 100, "location": 100}
    assert calculate_match(s) == 100.0
    s = {"skills": 50, "education": 100, "experience": 0, "role": 0, "location": 0}
    assert calculate_match(s) == 40.0
