from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

app.mount("/front", StaticFiles(directory="front/", html=True), name="front")
# app.mount("/dist", StaticFiles(directory="front/dist"), name="dist")
# app.mount("/front", StaticFiles(directory="front/public", html=True), name="front")
# app.mount("/build", StaticFiles(directory="front/public/build"), name="build")


@app.get("/name")
async def hello():
   return "Betty"

@app.get('/')
async def front():
   return RedirectResponse(url='front')