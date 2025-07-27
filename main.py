from fastapi import FastAPI
from generate_rain_video import main

app = FastAPI()

@app.get("/generate")
def generate_video():
    path = main()
    return {"status": "success", "file": path}
