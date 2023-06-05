from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure


@component
def HelloWorld():
    return html.h1("Hello, world!")


app = FastAPI()
configure(app, HelloWorld)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
    