from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/yanna")
def read_second():
    return {"HI": "ferererfer!"}


@app.get("/checker")
def read_checker():
    return {"chcker": "checker"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
