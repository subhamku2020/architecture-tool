from fastapi import FastAPI
from models import ProductRequirement
from deepseek_service import generate_architecture

app = FastAPI(title="DeepSeek AWS Architecture Generator")

@app.post("/generate-architecture")
def generate(req: ProductRequirement):
    return generate_architecture(req)
