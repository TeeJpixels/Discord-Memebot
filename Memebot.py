import discord, requests, json
# This is a simple Discord bot that fetches memes from the meme-api and sends them to the channel when a user types $meme.

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    
    if message.content.startswith('$hello'):
     await message.channel.send('Hello World!') #GREETS YOU BACK

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme()) #DISPLAYS A MEME

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('YOUR API HERE') #Enter you token here

##END##
