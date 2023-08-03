  # **AI Assistant**

As of now this is an early version of this AI assistance. I plan to add a variety of different features to this. Do note that I am still a student and I'm still learning programming so don't have high expectations. This is just a personal projects that I'm choosing to post online, any feedback will be greatly appreciated!

  ## **Features**
**Currently this project does not have many features but as time will come more features will be added.**

**Long Term Memory** -
  The AI saves all your past conversations into a JSON file, whenever the user mentions the word "remember" in their prompt to the AI, the entire message will be sent     to a sentence transformer model which will compare his prompt to previous ones, so for example if you mentioned to add milk to your shopping list because you are        running out, this will be saved to the JSON file, when you mention to the AI some along the lines of "Do you remember what I had on my shopping list?", the long term    memory script will run and it will compare this prompt to previous ones and the best match will be sent to the AI, allowing the illusion of a memory.

**Short Term Memory** - 
  The short term memory works in very similiar way as the long term one except instead of a sentence transofer model running and checking every single past                converstaion, the AI is given your entire chat history in the prompt with a limit of 4000 characters which can be increased by you if you wish, the AI itself will have to read your converstaion and find the best answer. If you wish to change the limit, change the 4000 value inside main.py on line 39.

**Telegram Integration** -
 You are now able to communicate with your AI remotly using Telegram! Before this you were forced to use your terminal to communicate and could not do it remotly, but    now you can. Currently I limited it so the AI can only talk to you in what ever chat you choose, so you can put it inside a group chat but it is not recommended.


## **Future Features:**
  - ~~Discord or other communication service integration~~
  - Stable Diffusion or other image generation integration
  - Voice Communication
  - Ability to search the internet
  - Google Calendar or alternative calendar software integration
  - More things that I will come up with in the future.


  ## **Installation:**
Note: As of the Version 0.1 the installation program is not created yet, so all the installations will have to be done manually and all the models and settings need to be modified manually. This will be different in future versions.

1. Install [oobabooga text generation](https://github.com/oobabooga/text-generation-webui) and install any models you want. 
2. Install a sentence transofermer model of your choice, by default the program will use [mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). Put the model of your choice inside the same folder as this repo, and ensure that you choose the correct model on LTM.py ln(22)
3. Ensure that you have the memories folder with two json files inside.
4. Run the oobabooga webui with the -API parameter set, choose the model you want using the webui
5. Ensure that you have a bot created in Telegram, if you do not just message @BotFather and get it setup
6. Edit the telegram_main.py and change the "bot_token" and "user_chat_value" values. If you do not know your chat value just message the bot and it will be inside the terminal, but run the telegram_main.py first.
7. After editing all values you are able to run the telegram_main.py and enjoy your conversations
