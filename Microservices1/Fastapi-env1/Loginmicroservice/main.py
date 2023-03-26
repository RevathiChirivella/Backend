from fastapi import FastAPI

app=FastAPI()

@app.get('/')

def hey():
    return {"hii"}