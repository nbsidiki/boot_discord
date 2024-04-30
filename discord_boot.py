import os
from dotenv import load_dotenv
import discord #import du module
from discord.ext import commands
import requests
#Intents
load_dotenv()
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True
# guilds = serveurs discords
intents.guilds = True
intents.members = True
# fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur
@bot.event
async def on_ready():
 print (f"{bot.user.name} s'est bien connecté !")

welcome_message = "Bienvenue sur le serveur ! Nous sommes heureux de vous avoir parmi nous. Pour Info le mot 'fuck' est interdit"

# Événement pour le nouvel utilisateur

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  
    if channel is not None:
        await channel.send(welcome_message)

# Commande !welcome
@bot.command()
async def welcome(ctx):
    await ctx.send(welcome_message)
    
def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = response.json()
    return f"{joke['setup']}\n{joke['punchline']}"

# Commande !joke
@bot.command()
async def joke(ctx):
    random_joke = get_random_joke()
    await ctx.send(random_joke)
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Fonction pour répondre à la commande !touché
@bot.command()
async def touché(ctx):
    await ctx.send("coulé ! 💥")
    

@bot.command()
async def members(ctx):
    members_info = []
    for member in ctx.guild.members:
        roles = [role.name for role in member.roles]
        members_info.append(f"{member.display_name}: {', '.join(roles)}")
    
    members_list = "\n".join(members_info)
    await ctx.send("Liste des membres :\n" + members_list)
    
@bot.event
async def on_message(message):
    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")
        
    if "feu" in message.content.lower():
        await message.add_reaction("🔥🔥🔥🔥🔥")
        
    if "feu" in message.content.lower():
        await message.add_reaction("❤️❤️❤️")
        
    if "fuck" in message.content.lower():
    # Bannir l'utilisateur
        await message.author.ban(reason="Utilisation du mot interdit")
        await message.channel.send(f"{message.author.mention} a été banni pour avoir utilisé un mot interdit.")
    
    if "fdp" in message.content.lower():
    # Bannir l'utilisateur
        await message.author.ban(reason="Utilisation du mot interdit")
        await message.channel.send(f"{message.author.mention} a été banni pour avoir utilisé un mot interdit.")
    
    await bot.process_commands(message)



@bot.event
async def on_ready():
    # Récupérer le canal où se trouve le bot
    guild = bot.guilds[0]  # Première guilde où le bot est présent
    channel = guild.get_channel(guild._system_channel_id)
    
    
    # Parcourir toutes les commandes du bot
    commandList = ""
    for command in bot.commands:
        # Récupérer la commande et son aide (description)
        commandList += f"!{command.name} \n"
        
#connexion du bot au serveur avec au token
    pinned_message = await channel.send(f"Commandes disponibles :\n {commandList}")

    await pinned_message.pin()
token = os.environ.get('TOKEN')
print(token)
bot.run(token)