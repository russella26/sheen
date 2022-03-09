from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen
from flask import Flask
from flask import request
from os.path import exists

config = GPT2ConfigCPU()
fname = 'training.txt'
tname = "aitextgen.tokenizer.json" 

def main():
    if not exists(tname):
        train_tokenizer(fname)
    ai = aitextgen(tokenizer_file=tname, config=config)
    dataset = TokenDataset(fname, tokenizer_file=tname, block_size=64)
    numsteps = 20000
    gen_every = 1000
    save_every = 5000
    ai.train(dataset, batch_size=8, num_steps=numsteps, generate_every=gen_every, save_every=save_every)

if __name__ == '__main__':
    main()
