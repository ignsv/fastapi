from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/second")
def read_second():
    return {"Second": "Second"}


@app.get("/nano")
def read_nano():
    return {"Nano": "Nano"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
