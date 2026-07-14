from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

client = Groq(api_key = api_key)

model = "llama-3.3-70b-versatile"
text = 'hello my name is diwesh i brought a electronic gadget from this site its now not working this is my mailid - janusharma@gmail.com and contant number is 7584862678'
prompt = f""" this is a customer ticket and extract the personal information and give it to me {text}"""
mes_user ={
    'role' : 'user',
    'content': prompt
}
# mes_system



from pydantic import BaseModel

class info(BaseModel):
    name: str
    email: str
    issue : str

schema = info.model_json_schema()
response_format ={
    'type' : 'json_object'
}

prom_sys = f""" extract the information and give strictly based on the given schema{schema} and give me a json  output"""
mes_sys ={
    'role': 'system',
    'content': prom_sys
}
messages = [mes_sys , mes_user]
response = client.chat.completions.create(model = model , messages = messages , response_format =response_format)
data =response.choices[0].message.content

import json
raw_json = data
data_file=json.loads(raw_json)
Info = info(**data_file)
print(Info.name)