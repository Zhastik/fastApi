from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
list_user_name = ['Artem', 'Andrey', 'Dima', 'Alex', 'Max']

class Response(BaseModel):
    new_W: str

@app.get('/')
async def home():
    return(list_user_name)

@app.post('/post/')
async def test_post(response: Response):
    new_data = response.text
    list_user_name.append(new_data)
    return {list_user_name}

@app.put('/put/{user_name}')
async def test_put(user_name: str):
    print(user_name)
    list_user_name.append(user_name)

@app.delete("/delete/{user_name}")
async def test_delete(user_name: str):
    print(user_name)
    list_user_name.remove(user_name)
    return {
        'deleted'
    }

@app.api_route("/pepls_list", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_homedata(username: str):
    print(username)
    return {
        'username':username
    }

