from fastapi import APIRouter

router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("")
def list_applications():
    return []


@router.post("/draft")
def create_draft():
    return {"status": "Draft Prepared"}


@router.post("/{app_id}/approve")
def approve(app_id: int):
    return {"id": app_id, "approval_status": "Approved"}


@router.post("/{app_id}/reject")
def reject(app_id: int):
    return {"id": app_id, "approval_status": "Rejected"}


@router.patch("/{app_id}")
def update_status(app_id: int, status: str):
    return {"id": app_id, "status": status}
