#
#
from uuid import uuid4
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def test():
    return {
        "app": "ml-frcr-01",
        "msg": "API is running",
        "random": str(uuid4())
    }
