from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import torch
import json
from decimal import *

sentences = []
#Senteces is where the raw json file information will be stored

with open("memory/pokemon.jsonl", "r") as f:
    for line in f:
        sentences.append(json.loads(line))

model = SentenceTransformer('all-mpnet-base-v2') #Make sure to have the model downloaded that you want to use
embeddings = model.encode(sentences) #Encodes all of the information from the JSON folder


query = "What do I need to buy from my shopping list? "
query_embedding = model.encode(query)

search_result = util.dot_score(query_embedding,embeddings) #Searches for a match between your prompt and stored data

search_result.tolist()
search_result = search_result[0]
search_result_final = search_result.tolist()
closest_match = search_result_final.index(max(search_result_final))
#Converts your json file into a list to make it easier to search, might be a bad way to convert the formats but it works

print(str(closest_match) + " " + str(sentences[closest_match]) )