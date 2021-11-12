# Chatbot for D&amp;D One-shot "Glinidril's Secret Lab"

This is a program that runs a chatbot for the Glinidril's Secret Lab Dunegons and Dragons one-shot.
The chatbot was created as a fun little gimmick of using AI chatbots as NPCs in a RPG, so expect the quality of a toy one-time project.
The program is meant to be used by the DM in the background.

The adventure can be found in the file ```Adventure.pdf```

## Getting the code to run

To run the code, you'll need Python 3.6 or newer and Transformers library which can be installed with the following command:
```pip install transformers[torch]```
A chatbot (i.e. the AI model behind it) should then be downloaded from [here](https://drive.google.com/file/d/1fr02h61GOL4u_cYJf54VhpC6vJSzOPO7/view?usp=sharing) (Warning: 2.7GB). Unzip the folder and place it into the folder with the rest of the files.
You will need a computer with at least 4GB RAM to run this but no GPU support is needed. The program can then be opened by running the ```run_chatbot.py``` file.

## Running the Program

On the first window, the program will ask you to input the information about player characters - their race and class on the left, and a very short description on the right.
Between one and five player characters can be added.
To run the chatbot, pick one of the encounters at the bottom.
Note that the encounter with the animated armor is a two-way chat and only the first of the added characters will take part in the conversation.

![first window](https://github.com/vid-koci/rpg_chatbot/blob/main/images/first_window.png)

The chat screen will probably take a couple of minutes to load - this is because the AI model is being loaded.
For each interaction, three pieces of information have to be provided: Who is saying it, what are thay saying, and whether they do anything on top of that.
Either of the last two can be left empty.
Pressing the "Send" button does not automatically invoke the AI to allow multi-way communication, i.e. the user (DM) to add multiple entries from multiple non-AI characters.
The "AI response" button creates a response from the chatbot.

![second window](https://github.com/vid-koci/rpg_chatbot/blob/main/images/second_window.png)
### Good practices

While you're free to use this chatbot in any way you like, note that it works best when used in the same way as it was trained. Following tips below will give the best results:
  * Avoid using names. All characters and NPCs should be referred to as "race class" (e.g. human warlock), including the two knights, who should be referred to as "grey knight" and "white knight". If your players refer to something by name, consider writing it like above instead. The exception are the names Glinidril and Callus, which the model has been trained to recognize.
  * The description of each character should be minimal, i.e. "Skinny, cloaked, and carrying a knife." It doesn't really make much of a difference anyway, so don't worry about it.
  * The chatbot is trained to respond (somewhat correctly) to actions "hits someone", "dies", and "approaches the gem", so consider describing all kinds of attacks as "hits X" and only describe movements if somebody moves close to the gem (final encounter). Use more detailed descriptions at your own risk.
  * Finish the encounter with the animated armor once it lets players through or hits for the first time - it was not trained beyond this and will produce meaningless responses more likely.

### FAQ
  * **Your interface is bad an looks like it's from the 90s.** I know and I'll gladly accept git pulls with a nicer interface.
  * **Your chatbot is bad and produces meaningless responses.** I am limited by the technology of my time. Also, a schizophrenic chatbot is the whole gimmick behind this one-shot. 
  * **Your interface limits me, I need more than 5 player characters for the final fight.** Improvise, you're the DM. Use one in-chat character to say and do acts of two in-game characters. Chatbot is not bright enough to notice it anyway.
  * **I want to have multiple characters speak to the animated armor** See above.
