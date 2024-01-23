from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/jk", response_class=HTMLResponse)
async def server():
    html_file = open("index.html", 'r').read()
    return html_file

@app.get("/kz", response_class=HTMLResponse)
async def server():
    html_file = open("index-2.html", 'r').read()
    return html_file

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=5555)
