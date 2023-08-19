#
#
import json
from fastapi import APIRouter
from pydantic import BaseModel

from celery_app import celery_app


router = APIRouter()

class Item(BaseModel):
    num: int
    name: str


@router.post("/start")
async def create_item(item: Item):
    task_name = "hello.task"

    task = celery_app.send_task(task_name, args=[item.num, item.name])
    return dict(
        status="PROCESS",
        task_id=task.id
    )


@router.get("/status/{task_id}")
def check_task(task_id: str):
    task = celery_app.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        response = {
            'status': task.state,
            'result': task.result,
            'task_id': task_id
        }
    elif task.state == 'FAILURE':
        response = json.loads(task.backend.get(task.backend.get_key_for_task(task.id)).decode('utf-8'))
        del response['children']
        del response['traceback']
    else:
        response = {
            'status': task.state,
            'result': task.info,
            'task_id': task_id
        }
    return response
