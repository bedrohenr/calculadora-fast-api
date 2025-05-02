from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculator(BaseModel):
    first_number: int
    second_number: int
    
    def soma(self):
        return self.first_number + self.second_number

    def subt(self):
        return self.first_number - self.second_number

    def multi(self):
        return self.first_number * self.second_number

    def div(self):
        if(self.second_number):
            return self.first_number / self.second_number

        return 0

    def expo(self):
        return self.first_number ** self.second_number

@app.get("/")
def read_root():
    return {
        "message": "Este programa é uma calculadora",
        "operacoes": "soma, subtração, multiplicação, divisão, exponenciação.",
        "endpoints": "/soma, /subt, /multi, /div, /expo"
    }


@app.post("/soma")
def soma(calc: Calculator):
    return {
        "message": "Soma concluída",
        "resultado": f"{calc.soma()}"
    }

@app.post("/subt")
def subt(calc: Calculator):
    return {
        "message": "Subtração concluída",
        "resultado": f"{calc.subt()}"
    }

@app.post("/multi")
def multi(calc: Calculator):
    return {
        "message": "Multiplicação concluída",
        "resultado": f"{calc.multi()}"
    }

@app.post("/div")
def div(calc: Calculator):
    return {
        "message": "Divisão concluída",
        "resultado": f"{calc.div()}"
    }

@app.post("/expo")
def expo(calc: Calculator):
    return {
        "message": "Exponenciação concluída",
        "resultado": f"{calc.expo()}"
    }
