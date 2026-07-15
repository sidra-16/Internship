from fastapi import FastAPI

app = FastAPI()
todo = [
    {"title": "Buy groceries", "completed": False},
    {"title": "Study FastAPI", "completed": False},
    {"title": "Exercise", "completed": True}]

@app.get("/tasks")
def view_tasks():
    return todo

@app.post("/tasks")
def add_task(title: str):

    new_task = {
        "title": title,
        "completed": False
    }

    todo.append(new_task)

    return {
        "message": "Task added successfully!",
        "task": new_task
    }

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_title: str):

    # Check if index exists
    if task_id >= len(todo):
        return {"message": "Task not found"}

    # Indexing is used here
    todo[task_id]["title"] = new_title

    return {
        "message": "Task updated successfully!",
        "updated_task": todo[task_id]
    }


@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):

    if task_id >= len(todo):
        return {"message": "Task not found"}

    # Indexing
    todo[task_id]["completed"] = True

    return {
        "message": "Task marked as completed!",
        "task": todo[task_id]
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id >= len(todo):
        return {"message": "Task not found"}

    # Remove task using index
    deleted = todo.pop(task_id)

    return {
        "message": "Task deleted successfully!",
        "deleted_task": deleted
    }







