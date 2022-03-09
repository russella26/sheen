# sheen
sheen is served in two parts:

# sheenserver
sheenserver is a simple flask app that uses the aitextgen library to generate text. simple.

sheenserver usage:
run trainsheen.py with python to train a model. the input text is expected to be in a file named 'training.txt'.
then, either run sheenserver.py or docker-compose up to serve generation options.

# sheenbot
sheenbot is a simple discord bot written with py-cord built to interface with sheenserver

sheenbot usage:
run sheenbot with python
bot token and guild ID expected to be in a .env file


note: sheenserver uses aitextgen which requires python 3.7, while sheenbot uses py-cord which requires python 3.8+.
do yourself a favor and use virtual enviroments here, be it conda or virtualenv.
it'll make everything way easier for local testing without spinning up docker.
