from pypdf import PdfReader


def extract_text(path: str) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


KNOWN_SKILLS = ["Java", "Python", "Selenium", "SQL", "Jira", "API Testing",
                "Manual Testing", "Playwright", "Git", "Docker"]


def parse_resume(path: str) -> dict:
    text = extract_text(path)
    skills = [s for s in KNOWN_SKILLS if s.lower() in text.lower()]
    return {"skills": skills, "raw_text_length": len(text)}
