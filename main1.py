from fastapi import FastAPI
import uvicorn

app = FastAPI()
deb = FastAPI()

@app.get("/")
def healthcheck():
    return 'OK'

@deb.get("/")
def healthcheck():
    return '101'

def func1():
    uvicorn.run(app)

def func2():
    uvicorn.run(deb, port=1212)

if __name__ == "__main__":
    Thread(target = func1).start()
    Thread(target = func2).start()