import sys
sys.path.insert(0, "backend")

from app.services.job_search import dedupe, normalize


def test_dedupe():
    j = normalize("QA", "Acme", "India", "Fresher", "x", "u", "d")
    assert len(dedupe([j, dict(j)])) == 1
