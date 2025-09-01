from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Invoke model
response = model.invoke("what is the capital of india")

print(response)  # response is a ChatMessage, so use .content
