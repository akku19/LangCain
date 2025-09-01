from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name='anthropic-model', temperature=2)

response = model.invoke("create a poem about a fresh mind")

print(response.content)
