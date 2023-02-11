
# openai-discordbot #
simple python3 script to create a discord bot for openai

This script was written entirely using ChatGPT. I understand the basics of how this work, but if you're more advanced in Python then you will be able to do a lot more than I can. If you have issues, paste the contents of the script into chatgpt, and ask it for help. It will be able to provide you a lot of info.

## To install ##
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

12. Select the intents you need, generally it should only be SERVER MEMBERS INTENT, and MESSAGE CONTENT INTENT,

13. Save Changes

14. From the left hand side, under OAuth2, select URL Generator

15. Select the Scopes. Will only need BOT

16. Select the Text Permissions that are required. These should be only

*Send Messages*

*Send Messages in Threads*

*Embed Links*

*Attach Files*

*Read Message History*

17. Copy the Generated URL, and paste into the URL bar of the browser and authorize the bot.

18. Start the bot. In Linux under Ubuntu 20.04 that this was tested on that should be

```
python3 aidiscordbot.py
```

To communicate with the bot, a user will type

```
/chat
```

Followed by their question. This is an example of what it will look like.

```
/chat tell me the weather of the bermuda triangle
```

## Creating a daemon service ##
If you'd like to run the program in the background I suggest creating a systemd service
1. Create a new user:
```
sudo useradd -r aidiscordbot
```

2. Set where you want the user's home directory to be, this could be where the script is stored. Note, the directory must exist already: 

```
sudo usermod -d /var/empty aidiscordbot
```

3. Set the user's shell to /sbin/nologin: 

```
sudo usermod -s /sbin/nologin aidiscordbot
```

4. Create the systemd service file: 

```
sudo nano /etc/systemd/system/aidiscordbot.service
```

5. Add the following content to the service file:


```    [Unit]
    Description=Aidiscordbot Service

    [Service]
    User=aidiscordbot
    Group=aidiscordbot
    ExecStart=/usr/bin/python3 /path/to/aidiscordbot.py
    Restart=always

    [Install]
    WantedBy=multi-user.target) 
```
Note: Replace /path/to/aidiscordbot.py with the actual path to the aidiscordbot.py script on your system.

6. Make sure the aidiscordbot.py script has the correct permissions:

```
    sudo chown aidiscordbot:aidiscordbot /path/to/aidiscordbot.py
    
    sudo chmod 700 /path/to/aidiscordbot.py 
```

7. Reload the systemd configuration:

```
sudo systemctl daemon-reload
```

8. Start the service:
```
sudo systemctl start aidiscordbot.service
```

9. Enable the service to start automatically at boot:
```
sudo systemctl enable aidiscordbot.service
```

With these steps, the aidiscordbot.py script should now run as the aidiscordbot user, with the least privilege necessary to execute the script, and will start automatically at boot.
