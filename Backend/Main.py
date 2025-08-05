from fastapi import FastAPI
from routers.screener import router as screener_router

app = FastAPI()

app.include_router(screener_router, prefix="/screener")

@app.get("/")
def root():
    return {"message": "Bullish platform backend live"}
