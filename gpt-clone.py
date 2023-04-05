from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)
load_dotenv()



def mychat(prompt):
    openai.api_key = os.environ["API_KEY_CHATGPT"]
    response = openai.Completion.create(
        model = os.environ["MODEL_GPT"],
        prompt=prompt,
        max_tokens=int(os.environ["MAX_TOKENS"]),
    )
    
    return response.choices[0].text


@app.route('/chatbot') 
def chatbot():
    try:
        pergunta = request.args.get('pergunta')
        resposta = mychat(pergunta)
    except Exception as e:
        resposta = "Ocorreu um erro: " + str(e)
    return jsonify(resposta=resposta)

app.run()
