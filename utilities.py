import base64
import os

import requests
from dotenv import find_dotenv, load_dotenv
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from transformers import pipeline

HUGGINFACE_HUB_API_TOKEN = os.getenv("HUGGINFACE_HUB_API_TOKEN")


load_dotenv(find_dotenv())

# OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"

llm = ChatOpenAI(temperature=0.7, model=llm_model)


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_image_description(image_path):
    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Outline the position of divs, texts and other relevant web contents to help a web developer in this image. I do not need you to give me preliminary explanation like, in the image provided. Just discuss the contents of the image.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    results = response.json()
    return results["choices"][0]["message"]["content"]


def generate_code(code_text):
    template = """
    You are a extremely knowledgeable software engineer, techical engineer and technical instructor who also knows
                everything on code implementation, software design, technical design, writing software codes, cloud engineering and programming. 
                You know all there is to know about software and technical design, implementation, deployment and maintenance.
                
                You've also designed, implemented, designed and deployed many cutting-edge technologies. 
                
                You understand how to design software, implement codes, teach newbies coding and even troubleshoot and debug codes
                which can enable peope implement codes and design software at ease. 
                Your job is to assist users to build a web page including the html, css and javascript depending on the following variables:
                0/ {code_text}
                
                When implementing codes and writing the programming logics and codes,
                you'll answer with confidence and to the point.
                Keep in mind that when coming up
                with programming logics as well as writing the code implementations, you need to provide the complete code implemenation no
                matter how long it could get. Do not shorten any code logic.
                
                If the {code_text} are less than 5, feel free to add a few more
                as long as they will compliment the implementation.
                
            
                Make sure to format your answer as follows:
               
                - implementation codes (markdown):
                    - HTML Code Implemenation
                    - CSS Code Implementation
                    - JS code Implemenation if needed. If there is any button like searchbar, menu bar etc, please add javascript action code to the buttons like click actions or hover. 
                  
                - Code explanation (bold)
                    Explain all the codes you implemented for the user to understand 
                    
                    Please make sure to write a clean code or software design depending on the case.  
                    Make the implementations easy to follow and step-by-step.
    """
    prompt = PromptTemplate(template=template, input_variables=["code_text"])
    code_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    code = code_chain.run(code_text)

    return code


# use this if you do not want to use GPT4-vision
def from_image_to_text(url):
    pipe = pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-large",
        max_new_tokens=1000,
    )

    text = pipe(url)[0]["generated_text"]
    return text
