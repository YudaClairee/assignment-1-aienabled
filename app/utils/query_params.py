from fastapi import Query

def standard_params(limit: int | None = Query(default=None)):
    return {"limit": limit}