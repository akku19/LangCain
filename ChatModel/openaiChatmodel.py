from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

response = model.predict("what is the capital of india?")
print(response)


