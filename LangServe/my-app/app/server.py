from fastapi import FastAPI
from langserve import add_routes
from pirate_speak.chain import chain as pirate_speak_chain

app = FastAPI()

add_routes(app, pirate_speak_chain, path="/pirate-speak")