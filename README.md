  # **AI Assistance**

As of now this is an extremely early version of this AI assistance. I plan to add a variety of different features to this. Do note that I am still a student and I'm still learning programming so don't have high expectations. This is just a personal projects that I'm choosing to post online, any feedback will be greatly appreciated!

  ## **Features**
Currently this project does not have many features but as time will come more features will be added.
Currently the only notable feature is "Short Term Memory". All the user inputted messages are stored into a JSON file, when the user inputs "remember" in the converstation the LTM.py program will run and will try to match the clostest prompt to the saved history, so if you talked to the AI about something specific for example "Do you remember what I put on my shopping list?" and if you told the AI prevously to add a specific item to the shopping list it will be able to tell you the item.

  ## **Installation:**
Note: As of the Version 0.1 the installation program is not created yet, so all the installations will have to be done manually and all the models and settings need to be modified manually. This will be different in future versions.

1. Install [oobabooga text generation](https://github.com/oobabooga/text-generation-webui) and install any models you want. 
2. Install a sentence transofermer model of your choice, by default the program will use [mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). Put the model of your choice inside the same folder as this repo, and ensure that you choose the correct model on LTM.py ln(22)
3. Ensure that you have a memories folder with the json file inside.
4. Run the oobabooga webui with the -API parameter set enabled, choose the model you want using the webui
5. Run the main.py and enjoy
