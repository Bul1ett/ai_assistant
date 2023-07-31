import subprocess
import sys

short_term_memory = []
short_term_memory_list = []

def chat_function():
    update_short_term_memory()
    clearing_memory()
    User_Input = str(input("\n You: "))

    if "remember" in User_Input.lower():
        memory(User_Input)

    else:
        subprocess.run(["python", "Chat.py",User_Input,str(short_term_memory),''])

def memory(Memory_Message):
    subprocess.run(["python", "LTM.py", Memory_Message, str(short_term_memory)])

def update_short_term_memory():
    with open("memory/short_term_memory.jsonl", "r") as f:
        for line in f:
            try:
                sentence = eval(line)
                short_term_memory.append(sentence)
            except SyntaxError:
                print("\n " + line)
                pass

def clearing_memory():
    short_term_memory_list = [list(row) for row in short_term_memory]
    total_characters = 0
    for row in short_term_memory_list:
        for element in row:
            total_characters += len(str(element))
    if total_characters > 4000:
        short_term_memory_list.pop(0)
        clean_memory()
        with open("memory/short_term_memory.jsonl", "a") as files:
            for lines in short_term_memory_list:
                try:
                    files.write("\n" + str(lines) )
                except:
                    print("Error occurred during clearing_memory functions")

def clean_memory():
    with open("memory/short_term_memory.jsonl", "w") as file:
        pass


while True:
    update_short_term_memory()
    clearing_memory()
    chat_function()



