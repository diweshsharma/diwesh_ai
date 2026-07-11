import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError('where is api key')

client = Groq(api_key = api_key)

model = "llama-3.3-70b-versatile"

prompt1 = 'Hey!'
prompt2 = 'hello, how are you?'
prompt3 = 'what are you doing?'

prompts = [prompt1 , prompt2 , prompt3]

for prompts in prompts:
    message = {
        'role' : 'user' ,
        'content' : prompts
    }
    
    messages = [message]

    response = client.chat.completions.create(model = model , messages = messages , max_tokens =5000 )
    usage=response.usage
    print(f"Prompt: {prompts} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}  Finish Reason: {response.choices[0].finish_reason}")
    
    # answer = response.choices[0].message.content

    # print(answer)