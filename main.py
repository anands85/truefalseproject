import openai #OpenAI API Package
from fastapi import FastAPI #FastAPI for creating API interfaces
import openai_key #File to get the OpenAI Key

# Create a FastAPI application
app = FastAPI()

# FastAPI decorator for hosting the API application
# input:
#       query   Text input for checking for true or false
@app.get("/trueorfalse/{query}")
def return_reponse(query: str):
    openai.api_key = openai_key.openai_key #replace with the OpenAI key
    true_false_text = 'True or False.' #additional OpenAI completion text to check for True or False.
    combined_text = query + true_false_text #concatenate the query and additional completion text
    # response for the combined text
    response = openai.Completion.create(
        model = "text-davinci-001",
        prompt = combined_text,
        temperature = 0.4,
        max_tokens = 64,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    output_text = response['choices'][0]['text']
    query = query.replace('query=','')
    output_text = output_text.replace('\n','')
    return {"query": query, "output_text": output_text}


