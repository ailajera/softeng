from fastapi import FastAPI

app = FastAPI()

tasks = [{
    "task_id": 1,
    "priority": "normal",
    "done": False
}, {
    "task_id": 2,
    "priority": "normal",
    "done": False
}, {
    "task_id": 3,
    "priority": "normal",
    "done": False
}]


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/loads")
def read_loads():
    return (tasks)