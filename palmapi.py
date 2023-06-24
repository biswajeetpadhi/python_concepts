import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY'])

response = genai.chat(messages=["Hello."])
print(response.last) #  'Hello! What can I help you with?'
response.reply("Can you tell me a joke?")