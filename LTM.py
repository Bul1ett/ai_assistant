from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import torch
import subprocess
import sys
from decimal import *

if len(sys.argv) > 1:
    info = sys.argv[1]
    prompt = sys.argv[2]

sentences = [] #Raw Data

with open("memory/general_memory.jsonl", "r") as f:
    for line in f:
        try:
            sentence = eval(line)
            sentences.append(sentence)
        except SyntaxError:
            print("\n {line}")
            pass

model = SentenceTransformer('all-mpnet-base-v2') #Make sure to have the model downloaded that you want to use
embeddings = model.encode(sentences) #Encodes all of the information from the JSON folder

query = info #chat_message #What needs to be searched

query_embedding = model.encode(query)

search_result = util.dot_score(query_embedding,embeddings) #Searches for a match between your prompt and stored data

search_result.tolist()
search_result = search_result[0]
search_result_final = search_result.tolist()
closest_match = search_result_final.index(max(search_result_final))
actual_message = sentences[closest_match][1]
#Converts your json file into a list to make it easier to search, might be a bad way to convert the formats but it works


def send_message(infor):
    subprocess.run(["python", "Chat.py",prompt,info,infor ])

send_message(str(actual_message))
