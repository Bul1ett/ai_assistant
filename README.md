  # **AI Assistant**

As of now this is an extremely early version of this AI assistance. I plan to add a variety of different features to this. Do note that I am still a student and I'm still learning programming so don't have high expectations. This is just a personal projects that I'm choosing to post online, any feedback will be greatly appreciated!

  ## **Features**
**Currently this project does not have many features but as time will come more features will be added.**

**Long Term Memory** -
  The AI saves all your past conversations into a JSON file, whenever the user mentions the word "remember" in their prompt to the AI, the entire message will be sent     to a sentence transformer model which will compare his prompt to previous ones, so for example if you mentioned to add milk to your shopping list because you are        running out, this will be saved to the JSON file, when you mention to the AI some along the lines of "Do you remember what I had on my shopping list?", the long term    memory script will run and it will compare this prompt to previous ones and the best match will be sent to the AI, allowing the illusion of a memory.

**Short Term Memory** - 
  The short term memory works in very similiar way as the long term one except instead of a sentence transofer model running and checking every single past                converstaion, the AI is given your entire chat history in the prompt with a limit of 4000 characters, the AI itself will have to read your converstaion and find the     best answer. This limit could be increased depening on the model you use but I can not test how well that would work as I do not have a good graphics card.


  ## **Installation:**
Note: As of the Version 0.1 the installation program is not created yet, so all the installations will have to be done manually and all the models and settings need to be modified manually. This will be different in future versions.

1. Install [oobabooga text generation](https://github.com/oobabooga/text-generation-webui) and install any models you want. 
2. Install a sentence transofermer model of your choice, by default the program will use [mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). Put the model of your choice inside the same folder as this repo, and ensure that you choose the correct model on LTM.py ln(22)
3. Ensure that you have a memories folder with the json file inside.
4. Run the oobabooga webui with the -API parameter set enabled, choose the model you want using the webui
5. Run the main.py and enjoy
