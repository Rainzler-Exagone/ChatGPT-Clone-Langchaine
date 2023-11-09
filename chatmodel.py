from langchain.chat_models import ChatOpenAI
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = " "

# Now you can access it using os.environ["OPENAI_API_KEY"]
openai_api_key = os.environ["OPENAI_API_KEY"]

chat = ChatOpenAI(temperature=0)

chat = ChatOpenAI(temperature=0, openai_api_key="", openai_organization="YOUR_ORGANIZATION_ID")

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="say hello world."
    ),
]
chat(messages)