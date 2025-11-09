import os
import requests
from diagram_generator import create_diagram_json
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def generate_architecture(req):
    prompt = f"""
    Generate an AWS architecture for a {req.product_type} app with {req.expected_users} users.
    Region: {req.region}. Database: {req.database_preference}.
    Include explanations and cost estimate.
    Respond in JSON with keys: architecture, explanation, estimated_cost.
    """

    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    payload = {"prompt": prompt, "max_tokens": 800}

    # Replace with real DeepSeek endpoint
    response = requests.post("https://api.deepseek.com/v1/completions", json=payload, headers=headers)
    data = response.json()

    # Mock result if DeepSeek not connected yet
    architecture = {"compute": ["EC2", "Lambda"], "database": ["RDS MySQL"], "storage": ["S3"]}
    explanation = {"EC2": "Main compute", "Lambda": "Serverless tasks", "RDS": "Managed DB", "S3": "Storage"}
    cost = "$250/month"

    diagram_json = create_diagram_json(architecture)

    return {
        "architecture": architecture,
        "explanation": explanation,
        "estimated_cost": cost,
        "diagram_json": diagram_json
    }
