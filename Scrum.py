import os
import openai

os.environ["OPEN_API_KEY"] = ""

openai_api_key = os.environ["OPEN_API_KEY"]

def chatgpt_call(prompt, model="gpt-3.5-turbo"):
   response = openai.ChatCompletion.create(
       model=model,
       messages=[{"role": "user", "content": prompt}]
   )
   return response.choices[0].message["content"]

prompt = "My name is Andrea"
response = chatgpt_call(prompt)
print(response)