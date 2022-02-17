import json, time, pytz, requests, datetime, asyncio, discord, os, random
import sqlite3
from discord.utils import get
from discord.ext import commands
from typing import Union


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  
    @commands.command(aliases=['킥'])
    async def _kick(self, ctx, member: discord.Member, *, reason=None):
      if ctx.author.guild_permissions.kick_members:
        a = await ctx.send(embed=discord.Embed(title="⚠️ | 경고", description=f"{member}를 서버에서 강퇴시키겠습니까?",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))
        await a.add_reaction('⭕')
        await a.add_reaction('❌')
#pip install -U discord-py-slash-command

        def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) in ['⭕', '❌']

        try:
          reaction, user = await self.bot.wait_for('reaction_add', timeout=15.0, check=check)
				
          if str(reaction.emoji) == '❌':
            await ctx.send('취소하였습니다.')
          if str(reaction.emoji) == '⭕':
            await member.kick(reason=reason)
            if reason != None:
              await ctx.send(embed=discord.Embed(title="📋 킥 로그", description='유저 : {0}'.format(str(member)) + '\n\n이유 \n' + reason + '\n\n관리자 ' + ctx.author.display_name,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))
            else:
              await ctx.send(embed=discord.Embed(title="📋 킥 로그 ", description='유저 :  {0}'.format(str(member)) + '\n\이유 \n없음' + '\n\n관리자 ' + ctx.author.display_name,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))

        except asyncio.TimeoutError:
          await ctx.send('시간이 초과되었습니다.')
          return
      else:
        await ctx.send(embed=discord.Embed(title="⛔ | 오류!", description="명령어를 사용할 권한이 부족해요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))

    @_kick.error
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('유저를 적으세요!')


    @commands.command(aliases=['밴'])
    async def _ban(self, ctx, member: discord.Member, *, reason=None):
      if ctx.author.guild_permissions.ban_members:
        a = await ctx.send(embed=discord.Embed(title="⚠️ | 경고", description=f"{member}를 서버에서 차단시키겠습니까?",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))
        await a.add_reaction('⭕')
        await a.add_reaction('❌')


        def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) in ['⭕', '❌']

        try:
          reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
				
          if str(reaction.emoji) == '❌':
            await ctx.send('취소하였습니다.')
          if str(reaction.emoji) == '⭕':
            await member.ban(reason=reason)
            if reason != None:
              await ctx.send(embed=discord.Embed(title="📋 밴 로그", description='유저 : {0}'.format(str(member)) + '\n\n이유 \n' + reason + '\n\n관리자 ' + ctx.author.display_name,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))
            else:
              await ctx.send(embed=discord.Embed(title="📋 밴 로그 ", description='유저 :  {0}'.format(str(member)) + '\n\이유 \n없음' + '\n\n관리자 ' + ctx.author.display_name,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))

        except asyncio.TimeoutError:
          await ctx.send('시간이 초과되었습니다.')
          return
      else:
        await ctx.send(embed=discord.Embed(title="⛔ | 오류!", description="명령어를 사용할 권한이 부족해요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))

    @_ban.error
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.reply('유저를 적으세요!')


    @commands.command(name='ㅊㅅ',aliases=['삭제','청소'])
    async def dele(self, ctx, *,number):
        number = int(number)
        if number <= 0:
            await ctx.reply('메시지 개수는 `1 ~ 100`로 입력하세요.')
        else:
            if number >= 101:
                await ctx.reply('메시지 개수는 `1 ~ 100`로 입력하세요.')
            else:
                if ctx.author.guild_permissions.manage_messages:
                    await ctx.channel.purge(limit=number+1)
                    await ctx.send(embed=discord.Embed(title="🗑️ 삭제",description=f'{number}개의 메세지가 삭제되었습니다.\n담당자 : {ctx.author.display_name}',timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xCCFFFF))
                else:
                    await ctx.send(embed=discord.Embed(title="⛔ | 오류!", description="명령어를 사용할 권한이 부족해요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xCCFFFF))
    @dele.error
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.reply('삭제 할 메세지 개수를 입력하세요!')


		
def setup(bot):
    bot.add_cog(admin(bot))