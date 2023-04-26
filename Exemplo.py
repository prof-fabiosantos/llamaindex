
import os

os.environ["OPENAI_API_KEY"] = 'coloque aqui a sua chave'

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# Load data from the journal text file
documents = SimpleDirectoryReader('./data').load_data()
# Create a simple vector index
# Isso cria um índice sobre os documentos na pasta de dados
index = GPTSimpleVectorIndex.from_documents(documents)
index.save_to_disk("generated_index.json")

# Create an infinite loop asking for user input and then breaking out of the loop when the response is empty
while True:
  query = input("Faça uma pergunta: ")
  if not query:
    print("Goodbye")
    break

  # query the index with the question and print the result
  result = index.query(query)
  print(result)