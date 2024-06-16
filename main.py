from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/front", StaticFiles(directory="front"), name="front")

@app.get("/name")
async def hello():
   return "Betty"

@app.get('/')
async def front():
   return RedirectResponse(url='front')