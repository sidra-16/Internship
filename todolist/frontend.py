import streamlit as st
import requests

# FastAPI URL
API_URL = "http://127.0.0.1:8000"

st.title("To-Do List")

st.header("View Tasks")

if st.button("Show Tasks"):
    response = requests.get(f"{API_URL}/tasks")
    st.write(response.json())


st.header("Add Task")

title = st.text_input("Enter task")

if st.button("Add Task"):
    response = requests.post(
        f"{API_URL}/tasks",
        params={"title": title}
    )

    st.write(response.json())



st.header("Update Task")

task_id = st.number_input(
    "Task ID",
    min_value=0,
    step=1
)

new_title = st.text_input("New Title")

if st.button("Update Task"):
    response = requests.put(
        f"{API_URL}/tasks/{task_id}",
        params={"new_title": new_title}
    )

    st.write(response.json())



st.header("Mark Task as Completed")

complete_id = st.number_input(
    "Task ID to Complete",
    min_value=0,
    step=1
)

if st.button("Complete Task"):
    response = requests.put(
        f"{API_URL}/tasks/{complete_id}/complete"
    )

    st.write(response.json())



st.header("Delete Task")

delete_id = st.number_input(
    "Task ID to Delete",
    min_value=0,
    step=1
)

if st.button("Delete Task"):
    response = requests.delete(
        f"{API_URL}/tasks/{delete_id}"
    )

    st.write(response.json())