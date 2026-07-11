import os
# from pathlib import path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

if not api_key:
    raise ValueError('where is api key')

client = Groq(api_key = api_key)

model="llama-3.3-70b-versatile"
role = 'user'
prompt = 'do you know what is ai engineering '

message_system ={
    'role' : 'system',
    'content' : 'you are an engineer'
}
message ={
    'role' : role,
    'content' : prompt
}
messages = [message_system,message]

#by default the temperature value is 0 

response = client.chat.completions.create(model = model , messages = messages , temperature = 1.5)
answer = response.choices[0].message.content
print(answer)