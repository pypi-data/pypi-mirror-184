#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request

from taskbox.db import get_db

tasks = Blueprint("tasks", __name__)


@tasks.post("/tasks")
def create_task():
    db = get_db()
    db.execute(
        "INSERT INTO tasks (name, command, device_id) VALUES (:name, :command, :device_id)",
        request.form,
    )
    db.commit()
    return "Task created successfully", 201


@tasks.get("/tasks/<int:id>")
def read_task(id: int):
    task = get_db().execute("select * from tasks where id = ?", (id,)).fetchone()
    if task is None:
        return f"Task {id} does not exist", 404
    return dict(task)


@tasks.put("/tasks/<int:id>")
def update_task(id: int):
    form = request.form.copy()
    form.add("id", id)
    db = get_db()
    db.execute(
        "UPDATE tasks SET name = :name, command = :command, device_id = :device_id WHERE id = :id",
        form,
    )
    db.commit()
    return "Task updated successfully", 201


@tasks.delete("/tasks/<int:id>")
def delete_task(id: int):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (id,))
    db.commit()
    return "Task deleted successfully"
