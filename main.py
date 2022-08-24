from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
user_db = {
    'Artem': {'name': 'Artem', 'date_birth': '24.03.2001', 'location': 'Samara'},
    'Ivan': {'name': 'Ivan', 'date_birth': '12.08.1993', 'location': 'Moscow'},
    'Dasha': {'name': 'Dasha', 'date_birth': '7.11.1998', 'location': 'Boston'}
}

class Response(BaseModel):
    name: str
    date_birth: str
    location: str

@app.get('/user')
async def home():
    list_user = list(user_db.values())
    return(list_user)

@app.post('/user')
async def test_post(response: Response):
    new_name = response.name
    user_db[new_name] = response.dict()
    return {'200'}

@app.put('/user')
async def test_put(response: Response):
    new_name = response.name
    user_db[new_name] = response.dict()
    return {'200'}

@app.delete("/delete/{user_name}")
async def test_delete(user_name: str):
    del user_db[user_name]
    return {
        'deleted'
    }

@app.patch('/user')
async def test_put(response: Response):
    new_name = response.name
    user_db[new_name].update(response.dict())
    user_db[new_name] = response.dict(exclude_unset=True)
    return {'200'}

@app.api_route("/pepls_list", methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_homedata(username: str):
    print(username)
    return {
        'username':username
    }

