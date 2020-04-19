from celery import Celery

app = Celery()

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y
