import discord
import requests
import json
def get_meme():
        response = requests.get("https://meme-api.com/gimme")
        meme = json.loads(response.text)
        return meme['url']
class myclient(discord.Client):    
    async def on_ready(self):
        print("Logged in as ",self.user)
    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())
intents = discord.Intents.default()
intents.message_content = True

client = myclient(intents = intents)
client.run("Enter Your Discord Bot Token Here")
