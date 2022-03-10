from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen
from flask import Flask
from flask import request
from os.path import exists

app = Flask(__name__)

tname = "aitextgen.tokenizer.json"
ai = aitextgen(tokenizer_file=tname, model_folder="trained_model")


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'GET':
        gentext = ai.generate_one()
        return(str(gentext))
    elif request.method == 'POST':
        context = request.json['context']
        gentext = ai.generate_one(prompt=context)
        return(str(gentext))
    else:
        return "hm."

@app.route('/')
def hello_world():
    return "gaming"
