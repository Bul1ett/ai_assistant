import subprocess

def chat_function():
    User_Input = str(input("\n You: "))
    if "remember" in User_Input.lower():
        memory(User_Input)
    else:
        subprocess.run(["python", "Chat.py",User_Input])

def memory(Memory_Message):
    subprocess.run(["python", "LTM.py", Memory_Message])

while True:
    chat_function()
