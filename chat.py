import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from cachetools import TTLCache
CACHE_SIZE, CACHE_TIME = int(os.getenv("CACHE_SIZE")), int(os.getenv("CACHE_TIME"))

current_dir = os.path.dirname(__file__)
cache = TTLCache(maxsize=CACHE_SIZE, ttl=CACHE_TIME)

def load_templates(filename):
    f = open(filename)
    return f.read()
def load_new_conv(address):
    if address in cache:
        return cache[address]
    cache[address] = chat_lagchain()
    return cache[address]

def chat_lagchain():
    openai.api_key=os.getenv("OPENAI_KEY")
    chat = ChatOpenAI(temperature=0)

    sys_instructions_file = os.path.join(os.path.dirname(__file__),'ff.txt')
    hum_instructions_file = os.path.join(os.path.dirname(__file__),'human.txt')
    system_template = load_templates(sys_instructions_file)
    human_template = load_templates(hum_instructions_file)
    

    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    system_message_prompt.format_messages()
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([
        system_message_prompt,
        MessagesPlaceholder(variable_name="history"),
        human_message_prompt
    ])

    memory = ConversationBufferMemory(input_key = "input", output_key="response", return_messages=True)
    conversation = ConversationChain(memory=memory, prompt=chat_prompt, llm=chat)
    return conversation

 
            
         
# def chat():
#     load_dotenv()
    
#     openai.api_key = os.getenv("OPENAI_KEY")
#     conversation = [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "What's the weather like in africa?"},
#     ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # Use the appropriate model name
#         messages=conversation
#     )
#     assistant_reply = response['choices'][0]['message']['content']
#     # print(assistant_reply)
#     return assistant_reply