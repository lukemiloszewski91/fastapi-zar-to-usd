from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from forex_python.converter import CurrencyRates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
c = CurrencyRates()

@app.get('/')
def read_form():
    return 'A simple app to convert SA Rands into US Dollars'


@app.get("/form")
def form_post(request: Request):
    result = "Enter an amount (ZAR)"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    result = c.convert('ZAR', 'USD', num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})