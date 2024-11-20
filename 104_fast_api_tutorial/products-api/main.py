from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
import uvicorn
from config.prisma_config import connectPrisma, disconnectPrisma
from routers.product_routers import router as productRouter


@asynccontextmanager
async def myLifeSpan(app:FastAPI):
    await connectPrisma()
    yield
    await disconnectPrisma()

app = FastAPI(lifespan=myLifeSpan)

@app.get('/welcome' )
def welcome():
    return {"data":"success..."}

# @app.get("/id/{id}")
# def getId(id: int):
#     return {"data": f"you have entered = {id}"}

# @app.get("/id/{id}/{limit}")
# def getId(id: int, limit:int):
#     return {"msg":"success" , "id": id, "limit": limit}

app.include_router(productRouter, prefix="/api") #prefix="/api/v1/prod"

if __name__ == "__main__":
    uvicorn.run(app=app, host="http://127.0.0.1", port=8000)


