from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BASE_URL = "http://127.0.0.1:5000/"


@app.get("/")
def index():
    return render_template("index.html")


@app.get('/about')
def about():
    return render_template("about.html")


@app.get("/tasks")
def all_tasks():
    url = "%s/%s" % (BASE_URL, "tasks")
    response = requests.get(url)
    raw_json = response.json()
    tasks = raw_json.get("tasks")
    return render_template("list.html", task_list=tasks)


@app.get("/tasks/create")
def create_form():
    return render_template("new.html")


@app.post("/task/create")
def create_task():
    url = "%s/%s" % (BASE_URL, "tasks")
    raw_data = request.form
    task_dict = {
        "summary": raw_data.get("summary"),
        "description": raw_data.get("description"),
    }
    response = requests.post(url, json=task_dict)
    if response.status_code == 204:
        return render_template("success.html")
    else:
        return render_template("generic_error.html")


@app.get("/tasks/<int:pk>/update")
def update_form(pk):
    url = "%s%s/%s" % (BASE_URL, "tasks", pk)
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        task = response_json.get("task")
        return render_template("edit.html", task=task)
    else:
        return render_template("generic_error.html")


@app.post("/tasks/update")
def update_task():
    task_data = request.form
    task_dict = {
        "summary": task_data.get("summary"),
        "description": task_data.get("description")
    }
    url = "%s%s/%s" % (BASE_URL, "tasks", task_data.get("pk"))
    response = requests.put(url, json=task_dict)
    if response.status_code == 204:
        return render_template("success.html")
    else:
        return render_template("generic_error.html")
