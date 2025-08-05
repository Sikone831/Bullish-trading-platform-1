from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/bullish")
def get_bullish(tickers: list[str] = Query(...)):
    return {"tickers": tickers, "status": "Placeholder response"}
