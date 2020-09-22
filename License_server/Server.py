from fastapi import FastAPI
import random
import uvicorn

from License_server import serv_addons

app = FastAPI()

@app.get('/check_lic')
def check_lics(rest_code: int):
    return serv_addons.check_lic(str(rest_code))

@app.get('/check_lic_day')
def check_lic_day(rest_code: int):
    return serv_addons.check_lic_day(str(rest_code))


@app.get('/get_list')
def check_lic_day(rest_code: int):
    return serv_addons.get_list(str(rest_code))

@app.get('/get_file')
def check_lic_day(rest_code: int):
    return serv_addons.get_file(str(rest_code))

@app.get('/check_in')
def check_in(rest_code: int, nickname: str):
    return serv_addons.check_in(str(rest_code), nickname)

@app.get('/add_list')
def add_list(rest_code: int, nickname: str):
    return serv_addons.add_list(str(rest_code), nickname)




@app.get("/")
def method(a: int, b: int):
    return random.uniform(a, b)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)