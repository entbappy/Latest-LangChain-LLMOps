from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/chain/c/N4XyA")
res = chain.invoke({"language": "Spanish", "text": "Generative AI is a bigger opportunity than Internet"})
print(res)