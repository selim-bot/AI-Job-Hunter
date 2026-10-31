from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter(prefix="/resume", tags=["resume"])
MAX_SIZE = 5 * 1024 * 1024


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(400, "Only PDF resumes are accepted")
    content = await file.read()
    if len(content) > MAX_SIZE:
        raise HTTPException(400, "File too large (max 5 MB)")
    return {"filename": file.filename, "size": len(content)}
