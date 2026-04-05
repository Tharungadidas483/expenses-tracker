from fastapi import APIRouter

router = APIRouter(prefix="/records", tags=["Records"])

@router.get("/")
def get_records():
    return {"message": "Records working"}