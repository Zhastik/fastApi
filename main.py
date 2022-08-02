from fastapi import FastAPI

app = FastAPI()
data = {"Name": None , "Language": None,}

@app.get('/')
def home():
    return(data)

@app.post('/test')
def test_post():
    return(data)
