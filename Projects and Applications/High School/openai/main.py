import os
import openai

openai.api_key = ""

q = input("What do you want to ask the ai: ")

response = openai.Completion.create(model="text-davinci-003", 
                                    prompt=q, 
                                    temperature=0, 
                                    max_tokens=2000)

print(response.choices[0].text)
