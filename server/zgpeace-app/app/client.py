from langserve import RemoteRunnable

api = RemoteRunnable("http://127.0.0.1:8000/pirate-speak")
response = api.invoke({"text": "hi"})
print('response >> ', response)