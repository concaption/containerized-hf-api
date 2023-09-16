#!/usr/bin/env python

"""
This is the main file for the webapp that generates text based of 'gpt2' model This does not uses padding and tokenization so, it is not recommended to use this for production.
"""

from transformers import pipeline
from fastapi import FastAPI, Response
from pydantic import BaseModel

generator = pipeline("text-generation", model="gpt2")

app = FastAPI(
    title="GPT2 Text Generator",
    description="This is a self-documenting API to interact with a GPT2 model and generate text",
    version="0.0.1",
)

class Body(BaseModel):
    text: str


@app.get("/")
async def root():
    """
    This is the root endpoint.
    """
    return Response(content="{'message':'A self-documenting API to interact with a GPT2 model and generate text'}", media_type="application/json")

@app.post("/generate")
async def generate(body: Body):
    """
    This is the generate endpoint.
    """
    result = generator(body.text, max_length=100, num_return_sequences=1)
    return Response(content=result[0]["generated_text"], media_type="text/plain")

@app.get("/health")
async def health():
    """
    This is the health endpoint.
    """
    return Response(content="OK", media_type="text/plain")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,
                host="0.0.0.0",
                port=8000,
                log_level="debug",
    )