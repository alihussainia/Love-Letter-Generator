from transformers import pipeline, AutoTokenizer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import torch

from warnings import filterwarnings
filterwarnings("ignore")  #ignore deprecation warnings


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model
model = torch.load("gptj_fp16_model.pt")
# load tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

# create pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer)

@app.get('/')
def welcome():
    return "Append /docs to the above URL to use Swagger UI" 

@app.post('/generate')
async def generate(text: str):
    return generator(text)[0]["generated_text"]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
