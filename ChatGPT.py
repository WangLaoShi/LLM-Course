# 使用方法 https://github.com/openai/openai-python
import os
from openai import OpenAI
config = {
    "OPENAI_API_KEY": "sk-proj-t9k983js8KN4taOjtEP9T3BlbkFJcwtKZQh94PIpjFw9AEk"
}
client = OpenAI(
    # This is the default and can be omitted
    api_key=config['OPENAI_API_KEY'],
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Tell me a joke",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)