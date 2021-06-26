
my_secret = 'token'
#this token is going to be the bots secret code thats pulled from the discord developer portal.
import os
import discord
import random
import urllib.request
from bs4 import BeautifulSoup
from keep_alive import keep_alive


client = discord.Client()
league = ["Aatrox", "Akali", "Ahri", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Camille", "Caitlyn", "Cassiopeia", "Cho'Gath", "Corki", "Darius", "Dr. Mundo", "Diana", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Irelia", "Ivern", "Illaoi", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Karma", "Kalista", "Karthus", "Kassadin", "Kai'Sa", "Katarina", "Kayn", "Kayle", "Kennen", "Kha'Zix", "Kog'Maw", "Kled", "Kindred", "LeBlanc", "Lee Sin", "Leona", "Lucian", "Lissandra", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu & Willump", "Olaf", "Orrn", "Orianna", "Pantheon", "Poppy", "Pyke", "Quinn", "Rammus", "Rakan", "Rek'Sai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra", "Sylas", "Talon", "Taliyah", "Taric", "TahmKench", "Thresh", "Teemo", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "VelKoz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "XinZhao", "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra", "Yuumi", "Senna", "Qiana", "Sett", "Aphelios", "Lillia", "Yone"]
top = ["Wukong", "Nocturne", "Riven", "Warwick", "Kled", "Nasus", "Quinn", "Singed", "Shen", "Fiora", "Camille", "Ornn", "Rengar", "Urgot", "Kayle", "Poppy", "Sett", "Jax", "Cho'Gath", "Yorick", "Maokai", "Trundle", "Heimerdinger", "Zac", "Aatrox", "Pantheon", "Kennen", "Gwen", "Darius", "Mordekaiser", "Garen", "Vladimir", "Malphite", "Llaoi", "Gnar", "Sion", "Vayne", "Rumble", "Lee Sin", "Volibear", "Tryndamere", "Teemo", "Yone", "Sylas", "Yasuo", "Akali", "Gragas", "Renekton", "Viego", "Dr.Mundo", "Gangplank", "Jayce", "Karma", "Ryze", "Irelia", "Tahm Kench", "Lucian"]
botl = ["Swain", "Seraphine", "Veigar", "Kog 'Maw", "Ashe", "Vayne", "Yasuo", "Sivir", "Miss Fortune", "Jhin", "Jinx", "Tristana", "Ezreal", "Draven", "Twitch", "Senna", "Caitlyn", "Samira", "Kai'sa", "Varus", "Kalista", "Xayah", "Lucian", "Aphelios"]
mid = ["Rumble", "ASol", "Annie", "Anivia", "Heimerdinger", "Wukong", "Pantheon", "Corki", "Talon", "Nocturne", "Sett", "Ahri", "Malzahar", "Galio", "Lee Sin", "Kayle", "Garen", "Katarina", "Vladimir", "Vel' Koz", "Diana", "Fizz", "Ekko", "Kassadin", "Lissandra", "Lux", "Xerath", "Zed", "Viego", "Yasuo", "Cassiopeia", "Seraphine", "Leblanc", "Malphite", "Neeko", "Sylas", "Qiyana", "Tryndamere", "Karma", "Victor", "Tristana", "Veigar", "Renekton", "Gwen", "Yone", "Twisted Fate", "Ziggs", "Zoe", "Jayce", "Akali", "Orianna", "Ryze", "Azir", "Syndra", "Lucian", "Irelia"]
jgl = ["Fiddlesticks", "Xin Zhao", "Kha'Zix", "Shaco", "Skarner", "Taliyah", "Wukong", "Rek'sai", "Warwick", "Zac", "Nunu & Willump", "Trundle", "Evelynn", "Nocturne", "Ivern", "Elise", "Gragas", "Vi", "Poppy", "Karthus", "Ekko", "Volibear", "Kayn", "Lee Sin", "Master Yi", "Kindred", "Sejuani", "Gwen", "Udyr", "Jarvan IV", "Mordekaiser", "Diana", "Olaf", "Amumu", "Shyvana", "Jax", "Rammus", "Rengar", "Morgana", "Graves", "Viego", "Nidalee", "Rumble", "Dr. Mundo", "Hecarim", "Nautilus", "Lilia"]
sup = ["Maokai", "Zilean", "Sona", "Lulu", "Janna", "Zyra", "Bard", "Leona", "Nami", "Vel'Koz", "Blitzcrank", "Xerath", "Soraka","Thresh", "Braum", "Shaco", "Veigar", "Rakan", "Neeko", "Senna", "Alistar", "Morgana", "Yuumi", "Pyke", "Lux", "Seraphine", "Taric", "Gragas", "Swain", "Nautilus", "Karma", "Galio", "Brand", "Rell", "Pantheon", "Shen", "Sett"]
#This is a list of all the viable champions per lane.
counters=[]
#an empty array that will have champions later added to it.

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$help"):
        embedVar = discord.Embed(title="COMMANDS", description="here are a list of commands", color=0xF1FF05)
        embedVar.add_field(name="$help", value="List of commands", inline=False)
        embedVar.add_field(name="${top, bot, mid, jg, supp}", value="Random laner", inline=False)
        embedVar.add_field(name="$rnd", value="Random champ", inline=False)
        embedVar.add_field(name="${name}", value="Will give you the top 10 counter picks for that champ", inline=False)

        await message.channel.send(embed=embedVar)
  elif message.content.startswith("$top"):
    await message.channel.send(random.choice(top))
  elif message.content.startswith("$bot"):
    await message.channel.send(random.choice(botl))
  elif message.content.startswith("$mid"):
    await message.channel.send(random.choice(mid))
  elif message.content.startswith("$jg"):
    await message.channel.send(random.choice(jgl))
  elif message.content.startswith("$supp"):
    await message.channel.send(random.choice(sup))
  elif message.content.startswith("$rnd"):
    await message.channel.send(random.choice(league))
#^^ these if statements will generate a random champion from the arrays.
  if message.content.startswith("$") and message.content != ("$top") and message.content != ("$bot") and message.content != ("$mid") and message.content != ("$jg") and message.content != ("$supp") and message.content != ("$rnd") and message.content != ("$help"):
#this if statement will start the counterpicks for champions
    fix = message.content[1:]
    fix = fix.replace(" ", "")
    fix = fix.replace("'", "")
    #because lots of champions have spaces in their names these will replace apostrophes and spaces all together
    gwen = "https://u.gg/lol/champions/" + fix + "/build?rank=overall"
    #this is the website u.gg where all the counterpicks are going to be pulled from.
    x = urllib.request.urlopen(gwen)
    soup = BeautifulSoup(x)
    for x in soup.find_all('div', attrs = {'class': 'toughest-matchups'}):
      for y in soup.find_all('div', attrs = {'class': 'matchups'}):
        for z in soup.find_all('a', attrs = {'class': 'champion-matchup'}):
          name = z.find('div', attrs = {'class': 'champion-name'})
          #each counterpick is pulled from u.gg
          counters.insert(0, name.text)
          #because u.gg lists their champions backwards i've created an array so that they are in order
    if len(counters) == 10:
      for t in range(0, len(counters)):
        await message.channel.send(counters[t])
    #the counterpicks are then printed onto discord
    counters.clear()
    #the counter array is then cleared for its next use 
  

keep_alive()
client.run(os.getenv("token"))


