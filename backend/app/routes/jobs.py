from fastapi import APIRouter

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("")
def list_jobs():
    return []


@router.post("/search")
def start_search():
    return {"status": "started"}


@router.get("/{job_id}")
def get_job(job_id: int):
    return {"id": job_id}


@router.post("/{job_id}/match")
def match_job(job_id: int):
    return {"id": job_id, "match_score": None}
