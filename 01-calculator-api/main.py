from fastapi import FastAPI, HTTPException

app = FastAPI(title="Calculator API")

@app.get("/add")
def add_numbers(a: float, b: float) -> dict[str, float]:
    return {"result" : a + b}

@app.get("/subtract")
def subtract_numbers(a: float, b: float) -> dict[str, float]:
    return {"result" : a - b}

@app.get("/multiply")
def multiply_numbers(a: float, b: float) -> dict[str, float]:
    return {"result" : a * b}

@app.get("/divide") 
def divide_numbers(a: float, b: float) -> dict[str, float]:
    if b == 0:  
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result" : a / b}


