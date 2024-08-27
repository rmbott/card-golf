from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlmodel import Field, Session, SQLModel, create_engine

class Counter(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    counter: int | None = None

sqlite_file_name = "golf.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def initialize_counter():
      counter = Counter(counter=0)
      with Session(engine) as session:
            session.add(counter)
            session.commit()

def increment_counter():
      with Session(engine) as session:
            counter = session.get(Counter, 1)
            counter.counter += 1
            session.add(counter)
            session.commit()

def get_counter():
      with Session(engine) as session:
            counter = session.get(Counter, 1)
            return counter.counter

app = FastAPI()
app.mount("/golf", StaticFiles(directory="golf/", html=True), name="golf")
create_db_and_tables()
initialize_counter()

counter = Counter(counter=0)

@app.get("/counter")
async def hello():
      increment_counter()
      return f"{get_counter()}"

@app.get('/')
async def front():
   return RedirectResponse(url='golf')