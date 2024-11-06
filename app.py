from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_response_rec(name: str = None, message: str = None  ) -> HTMLResponse:
    return HTMLResponse(f"<h1>Hello {name}! {message}</h1>")