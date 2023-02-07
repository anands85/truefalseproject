## True or False Text Detection ##

This python FastAPI module consists of intelligent query completion engine using the OpenAI Text Completion API.

## Installation ##

1. Create the OpenAI platform API keys by following the [link](https://platform.openai.com/account/api-keys).
2. Install the OpenAI python package.
`pip install openai`
3. Install the FastAPI python package.
`pip install fastapi`
4. Install the UVICORN standard python package for testing the FastAPI application.
`pip install "uvicorn[standard]`
5. Open the terminal and in the same file location of the main.py run the following command:
`uvicorn main:app --reload`

## Testing the True or False Text Detector ##

Open the URL link below and change the query accordingly.

`http://127.0.0.1:8000/trueorfalse/query=Scanner%20is%20an%20input%20device`

The response of the API are:

`{"query":"Scanner is an input device","output_text":"False"}`
