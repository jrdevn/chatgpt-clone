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

def mydraw(prompt):
    response = openai.Image.create(
        size = '512x512',
        prompt=prompt,
        n = 1,
        response_format="url"
    )
    return response["data"][0]["url"]

@app.route('/chatbot') 
def chatbot():
        pergunta = request.args.get('pergunta')
        if pergunta[0:4] == 'img:':
            pergunta = pergunta.replace("img:", "")
            resposta = mydraw(pergunta)
            return jsonify(url_imagem=resposta, resposta="")
        else:
            resposta = mychat(pergunta)
            return jsonify(resposta=resposta)
        
app.run()
