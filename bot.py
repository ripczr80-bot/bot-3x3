import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def criar_3x3(ctx, valor: float):
    embed = discord.Embed(
        title="🔥 Novo 3x3 Criado!",
        description=f"Valor da partida: R$ {valor:.2f}",
        color=discord.Color.green()
    )
    embed.add_field(name="Formato", value="3x3", inline=False)
    embed.add_field(name="Status", value="Aguardando jogadores...", inline=False)

    await ctx.send(embed=embed)

bot.run("SEU_TOKEN_AQUI")
