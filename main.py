import discord
from discord import app_commands
import random

id_do_servidor =  1095769307650195479 #Coloque aqui o ID do seu servidor

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync() # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(name = 'teste', description='Testando') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    num = random.randint(1,100)
    await interaction.response.send_message(f"Numero: {num} seu número aleatorio foi gerado!", ephemeral = False) 

aclient.run('MTA5NTQzOTcxODgyMjQ2MTYzMQ.GAOnep.dJEM_DmhJTcIZ5rvOgiHTYHKlaeraRUqtQNyoQ')