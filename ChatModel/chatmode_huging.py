import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load environment variables
load_dotenv()

# Get token from .env
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Create HF endpoint with API key
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3.1",
    task="text-generation",
    huggingfacehub_api_token=hf_token
)

# Wrap with Chat interface
model = ChatHuggingFace(llm=llm)

# Call the model
result = model.invoke("What is the capital of India?")
print(result.content)
