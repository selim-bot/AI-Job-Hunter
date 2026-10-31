"""Job discovery. Only use sources that permit automated access
(Greenhouse/Lever public boards, employer feeds, authorized APIs)."""
import httpx


def normalize(title, company, location, experience, source, apply_url, description):
    return {
        "title": title, "company": company, "location": location,
        "experience": experience, "source": source,
        "apply_url": apply_url, "description": description,
    }


def dedupe(jobs: list[dict]) -> list[dict]:
    seen, out = set(), []
    for j in jobs:
        key = (j["title"].lower().strip(), j["company"].lower().strip(), j["location"].lower().strip())
        if key not in seen:
            seen.add(key)
            out.append(j)
    return out


def fetch_greenhouse(board_token: str) -> list[dict]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"
    data = httpx.get(url, timeout=20).json()
    return [
        normalize(j["title"], board_token, j.get("location", {}).get("name", ""),
                  "", "Greenhouse", j["absolute_url"], j.get("content", ""))
        for j in data.get("jobs", [])
    ]
