import asyncio
import os
import re
import time
import openai
import discord
import logging
from discord.ext import commands

# Set up the logging system
#logging.basicConfig(filename='bot.log', level=logging.DEBUG,
#                    format='%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Set up OpenAI API key
try:
    openai.api_key = "openai api key here"
except openai.OpenAIError as e:
    raise Exception(f"Error setting OpenAI API key: {e}")

# Create the bot instance
intents = discord.Intents.all()
#intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

# List to store the questions in a queue
question_queue = []

# Dictionary to store user IDs and the time they last asked a question
rate_limit_dict = {}

# Load the list of bad words from the file
with open("badwords.txt") as f:
    bad_words = f.read().splitlines()

# Event handler for when a user sends a message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_id = message.author.id

    if message.content.startswith("/chat"):
        question = message.content[5:].strip()
        
        # Check for bad words
        for word in bad_words:
            if word in question.lower():
                await message.channel.send(f"{message.author.mention}, I cannot respond to questions like that.")
                return
        
        # Perform input validation to prevent XSS, SQL injection, and directory traversal
        question = re.sub(r'[^\w\s]', '', question)

        # Log the user's question to the log file
        logging.info(f"{message.author.name}: {question}")
        
        if user_id not in rate_limit_dict:
            rate_limit_dict[user_id] = time.time()
        else:
            time_since_last_question = time.time() - rate_limit_dict[user_id]
            if time_since_last_question < 3:
                await message.channel.send(f"{message.author.mention}, you are asking too fast! Please slow down.")
                return

        question_queue.append((message.channel, question, message))
        rate_limit_dict[user_id] = time.time()
        print(f"{message.author.name}: {question}")



# Coroutine to handle sending the response to the user
async def send_message(channel, response, message):
    await channel.send(f"{message.author.mention}, {response}")

# ...

# Coroutine to handle the questions in the queue
async def handle_question_queue():
    while True:
        if question_queue:
            channel, question, message = question_queue.pop(0)
            try:
                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=question,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,
                ).choices[0].text
            except Exception as e:
                print (f"Error answering question: {e}")
                continue
            await send_message(channel, response, message)
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(handle_question_queue())
    loop.run_until_complete(bot.start("discord token here"))
