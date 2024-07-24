from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import redis

r = redis.Redis(host='redis', port=6379, db=0)

app = FastAPI()

app.mount("/front", StaticFiles(directory="front/", html=True), name="front")


@app.get("/name")
async def hello():
      r.incr('counter')
      return f"{r.get('counter')}"

@app.get('/')
async def front():
   return RedirectResponse(url='front')