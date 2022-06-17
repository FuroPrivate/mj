import discord
from discord.ext import commands
from discord.ui import text_input,Modal,View,Button




class Artifact(commands.cog):

    class ProcButton(View):
        
        def __init__(self):
            super().__init__()

            self.add_item((label="計算する",style=discord.ButtonStyle.red))

    
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def character(self,ctx):
        if not ctx.channel.id == 1234:
            return await ctx.send('このチャンネルでは実行できないぞ')
