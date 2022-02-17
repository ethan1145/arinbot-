import json, time, pytz, requests, datetime, asyncio, discord, os, random
import sqlite3
from discord.utils import get
from discord.ext import commands
from typing import Union
db = sqlite3.connect('main.sqlite')
cursor = db.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS main(
          user TEXT,
          user_id TEXT,
          user_money TEXT,
					user_level TEXT,
					user_bank TEXT,
					buying TEXT,
					items TEXT,
					item_level TEXT)''')
class pet(commands.Cog):
		def __init__(self, bot):
			self.bot = bot
		@commands.command(name='마이펫',aliases=['내펫'])
		async def mypet(self, ctx):
			cursor.execute('SELECT items FROM main WHERE user_id = {0}'.format(ctx.author.id))
			result = cursor.fetchone()
			result2 = str(result)
			asd = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
			cursor.execute('SELECT user FROM main WHERE user_id = {0}'.format(ctx.author.id))
			result = cursor.fetchone()
			result2 = str(result)
			user = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
			if user is None:
				embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
				await ctx.send(embed=embed)
				return
			if asd == '없음'or asd == None:
						await ctx.send(embed=discord.Embed(title='❌ | 오류!', description='보유한 펫이 없습니다.', colour=0xCCFFFF))
						return
			cursor.execute('SELECT item_level FROM main WHERE user_id = {0}'.format(ctx.author.id))
			result = cursor.fetchone()
			result2 = str(result)
			result2 = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
			await ctx.send(embed=discord.Embed(title='💕 | 마이펫', description=f'이름 : {asd}\n레벨 : {result2}', colour=0xCCFFFF))
		@commands.command(name='펫등록')
		async def singinpet(self,ctx):
			cursor.execute('SELECT items FROM main WHERE user_id = {0}'.format(ctx.author.id))
			result = cursor.fetchone()
			result2 = str(result)
			asd = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
			cursor.execute('SELECT user FROM main WHERE user_id = {0}'.format(ctx.author.id))
			result = cursor.fetchone()
			result2 = str(result)
			user = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
			if user is None:
				embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
				await ctx.send(embed=embed)
				return
			if asd == '없음':
						a=await ctx.send(embed=discord.Embed(title='❌ | 오류!', description='보유한 펫이 없습니다. 펫을 등록하겠습니까?', colour=0xCCFFFF))
						await a.add_reaction('⭕')
						await a.add_reaction('❌')

						def check(reaction, user):
								return user == ctx.author and str(reaction.emoji) in [ '⭕', '❌']

						try:
								reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
								
								if str(reaction.emoji) == '⭕':
									def check(m):
										return m.author == ctx.author and m.channel == ctx.channel

									await a.edit(embed=discord.Embed(title='💕 | 등록', description='펫의 이름을 적어주세요', colour=0xCCFFFF))
									desc = await self.bot.wait_for("message", check=check)
									desc = desc.content
									sql = 'UPDATE main SET items = ? WHERE user_id = {0}'.format(ctx.author.id)
									val = (str(desc),)
									cursor.execute(sql, val)

								if str(reaction.emoji) == '❌':
									embed = discord.Embed(title='❌ | 등록취소', description='등록을 취소했습니다.', colour=0xCCFFFF)
									await ctx.send(embed=embed)
						except asyncio.TimeoutError:
							await ctx.send('시간이 초과되었습니다.')
def setup(bot):
    bot.add_cog(pet(bot))