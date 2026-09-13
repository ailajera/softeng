from fastapi import FastAPI

app = FastAPI(title="Tasks")
@app.get("/")
def root():
    return "ok"

tasks = []
"""
a task should look like
{
    "task_id": 1,
    "priority": "normal",
    "done": False
}
"""
next_id = 1

@app.post("/tasks")
def create_task(task_in):
    # create the logic for adding task on our tasks
    pass

@app.get("/tasks")
def list_tasks():
    # return the task
    pass

@app.get("/tasks/{task_id}")
def get_task(task_id):
    # create a loop to find a task using task_id
    # after making that work, create a function that will do that as well
    pass
