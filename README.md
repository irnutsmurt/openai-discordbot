# openai-discordbot
simple python3 script to create a discord bot for openai

This script was written entirely using ChatGPT. I understand the basics of how this work, but if you're more advanced in Python then you will be able to do a lot more than I can. If you have issues, paste the contents of the script into chatgpt, and ask it for help. It will be able to provide you a lot of info.

To install
1. git clone the repository
2. pip install -r requirements.txt
3. Create an openai account at https://openai.com/api/
4. Open your account from the top right icon, then select "view api keys"
5. Select "Create New Api Key" and copy it
6. Paste the key into the aidiscord.py file where it says "openai api key here"
7. Create a discord api token by going to https://discord.com/developers/applications/
8. Select "New Application" and give it a name and save
9. Select Bot from the left hand panel
10. Press the "Add Bot" button, and press the "Yes, do it" button
11. Copy the token, and paste into the aidiscord.py file where it says "discord token here"
12. Select the intents you need, generally it should only be SERVER MEMBERS INTENT and MESSAGE CONTENT INTENT
13. Save Changes
14. From the left hand side, under OAuth2, select URL Generator
15. Select the Scopes. Will only need BOT
16. Select the Text Permissions that are required. These should be only
Send Messages
Send Messages in Threads
Embed Links
Attach Files
Read Message History
17. Copy the Generated URL, and paste into the URL bar of the browser and authorize the bot.
18. Start the bot. In Linux under Ubuntu 20.04 that this was tested on that should be
python3 aidiscordbot.py

To communicate with the bot, a user will type
/chat

Followed by their question. This is an example of what it will look like.
/chat tell me the weather of the bermuda triangle
