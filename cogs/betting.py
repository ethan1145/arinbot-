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
class bet(commands.Cog):
		def __init__(self, bot):
			self.bot = bot
		@commands.command(name='출첵', aliases=['ㅊㅊ', '출석체크'])
		@commands.cooldown(1, 43200, commands.BucketType.user)
		async def check(self, ctx):
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				if result == None:
						embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				mns_money = int(n_money) + 50000
				sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(ctx.author.id)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				db.commit()
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				await ctx.send(embed=discord.Embed(title="✅ | 출첵 완료!",description=f"{ctx.author.mention} 출석체크 성공!\n유저 : {ctx.author}({ctx.author.id})\n서버 : {ctx.guild.name}\n출첵보상으로 `50000`원을 드렸어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))


		@check.error
		async def on_command_error(self, ctx, error):
				if isinstance(error, commands.CommandOnCooldown):
						msg = f'`{int(error.retry_after // 3600)}`시간 뒤에 다시 시도할 수 있습니다.'
						await ctx.send(msg)
		# 명령어를 사용할 권한이 부족해요!
		


		@commands.command(name='ㅇㅇ', aliases=['올인'])
		async def allin(self, ctx):
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				battingmoney = n_money

				if int(battingmoney) < 500:
						await ctx.send('적어도 500이상은 배팅해야되요!')
						return
				if result == None:
						embed = discord.Embed(title='❌ | 오류', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				if int(battingmoney) > int(n_money):
						await ctx.send('돈이 부족해요!')
						return
				ea = [500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000,
							500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000,
							500000000000000]
				aa = [0, 0, 0, 2, 2, 0, 0, 3, 2, 4, 0, 6, 5, 4, 0, 0]
				rndm = random.choice(aa)
				battingmoney1 = int(battingmoney) * int(rndm)

				if battingmoney1 == 0:
						mns_money = int(n_money) - int(battingmoney)
						tt = '-'
						rndm += 1
				else:
						mns_money = int(n_money) - int(battingmoney)
						mns_money = int(mns_money) + int(battingmoney1)
						tt = '+'  # 우와 축하해요! 2배로 성공했어요.#
						rndm -= 1

						battingmoney = int(battingmoney1) - int(battingmoney)
				sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(ctx.author.id)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				await ctx.send(embed=discord.Embed(title=f'🪙 | {tt}{rndm}배!', color=0xCCFFFF))


		# 명령어를 사용할 권한이 부족해요!
		nomsg = ["다음에는 성공할 수 있을 거예요.. 화이팅!", "성공한 줄 알았는데..! 진짜 아쉬워요.", "아쉬워요.. 베팅한 전적 코인을 잃었어요."]


		@commands.command(name='ㄷㅂ', aliases=['도박'])
		async def batting(self, ctx, *, battingmoney):
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")

				if int(battingmoney) < 500:
						await ctx.reply('적어도 500이상은 배팅해야되요!')
						return
				if result == None:
						embed = discord.Embed(title='❌ | 오류', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
						await ctx.reply(embed=embed)
						return
				if int(battingmoney) > int(n_money):
						await ctx.reply('돈이 부족해요!')
						return
				ea = [500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000,
							500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000, 500000000000000,
							500000000000000]
				aa = [0, 0, 0, 2, 2, 0, 0, 3, 2, 4, 0, 0, 5, 4, 0, 0]
				rndm = random.choice(aa)

				battingmoney1 = int(battingmoney) * int(rndm)

				if battingmoney1 == 0:
						mns_money = int(n_money) - int(battingmoney)
						tt = '-'
						rndm = 1
				else:
						rndm -= 1
						mns_money = int(n_money) - int(battingmoney)
						mns_money = int(mns_money) + int(battingmoney1)
						tt = '+'  # 우와 축하해요! 2배로 성공했어요.#
						#
						battingmoney = int(battingmoney1) - int(battingmoney)
				sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(ctx.author.id)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				await ctx.send(embed=discord.Embed(title=f'🪙 | {tt}{rndm}배!', color=0xCCFFFF))
		@batting.error
		async def on_command_error(self, ctx, error):
				if isinstance(error, commands.MissingRequiredArgument):
						await ctx.reply('베팅할 금액을 적으세요!')



		@commands.command(name='가입', aliases=['ㄱㅇ'])
		async def sign_in(self, ctx):
				cursor.execute('SELECT user_id FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				if result is None:
						a = await ctx.send(embed=discord.Embed(title='가입 진행', description='게임에 가입 하실려면 ⭕ 이모지를 클릭하세요', colour=0xCCFFFF))
						await a.add_reaction('⭕')
						await a.add_reaction('❌')

						def check(reaction, user):
								return user == ctx.author and str(reaction.emoji) in [ '⭕', '❌']

						try:
								reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
								
								if str(reaction.emoji) == '⭕':
									await a.delete()
									sql = 'INSERT INTO main(user, user_id, user_money, user_level, user_bank,buying,items,item_level) VALUES(?,?,?,?,?,?,?,?)'
									val = (str(ctx.author), str(ctx.author.id), str('50000'), str('0'), str('0'),str('없음'),str('없음'),str('0'))
									cursor.execute(sql, val)
									db.commit()
									embed = discord.Embed(title='✅ | 가입성공!', description='가입됬습니다.\n기본적으로 `50000`원을 드릴게요.', colour=0xCCFFFF)
									await ctx.send(embed=embed)

								if str(reaction.emoji) == '❌':
									await a.delete()
									embed = discord.Embed(title='❌ | 가입취소', description='가입을 취소했습니다.', colour=0xCCFFFF)
									await ctx.send(embed=embed)
						except asyncio.TimeoutError:
							await ctx.send('시간이 초과되었습니다.')
						
				else:
						embed = discord.Embed(title='❌ | 오류!', description='이미 가입된 유저입니다', colour=0xCCFFFF)
						await ctx.send(embed=embed)


		@commands.command(name='압수', aliases=['ㅇㅅ'])
		async def give_to_ad(self, ctx, member: discord.Member, *, qmoney):
				if ctx.author.id == 739673575929282571:
						cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(member.id))
						result = cursor.fetchone()
						result2 = str(result)
						n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
						if result == None:
								embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
								await ctx.send(embed=embed)
								return
						mns_money = int(n_money) - int(qmoney)
						sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(member.id)
						val = (str(mns_money),)
						cursor.execute(sql, val)
						db.commit()
						cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(member.id))
						result = cursor.fetchone()
						result2 = str(result)
						n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")

						embed = discord.Embed(title='✅ | 압수성공', description=f'{qmoney}원을 압수했어요.\n현재 잔액 : `{n_money}`원 입니다.',colour=0xCCFFFF)
				await ctx.send(embed=embed)


		@commands.command(name='강충', aliases=['ㄱㅊ'])
		async def in_ad(self, ctx, member: discord.Member, *,qmoney):
				if ctx.author.id == 739673575929282571:
						cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(member.id))
						result = cursor.fetchone()
						result2 = str(result)
						n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
						if result == None:
								await ctx.send(
										embed=discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF))
								return
						mns_money = int(n_money) + int(qmoney)
						sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(member.id)
						val = (str(mns_money),)
						cursor.execute(sql, val)
						db.commit()
						cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(member.id))
						result = cursor.fetchone()
						result2 = str(result)
						n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")

						embed = discord.Embed(title='✅ | 지급성공', description=f'{qmoney}원을 지급했어요.\n현재 잔액 : `{n_money}`원 입니다.',colour=0xCCFFFF)
				await ctx.send(embed=embed)


		@commands.command(name='ㄷ', aliases=['돈', '내돈', '진액'])
		async def mm(self, ctx):
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				money1 = cursor.fetchone()
				if money1 is None:
						embed = discord.Embed(title='❌  오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xFF0000)
						await ctx.send(embed=embed)
						return
				money = str(money1)
				money = money.replace('(', '').replace(')', '').replace(',', '').replace("'", "")  # 보유 코인

				cursor.execute('SELECT user FROM main WHERE user_id = {0}'.format(ctx.author.id))
				user = cursor.fetchone()  # aliases
				user = str(user)
				user = user.replace('(', '').replace(')', '').replace(',', '').replace("'", "")  # 닉네임
				embed = discord.Embed(title='🪙 | 돈', description=f'{ctx.author.name}\n현재 잔액 : `{money}`원', colour=0xCCFFFF)
				await ctx.send(embed=embed)


		@commands.command(name='돈줘', aliases=['ㄷㅈ', 'ㄷㅂㄱ', '돈내놔', 'ㄷㄴㄴ'])
		@commands.cooldown(1, 300, commands.BucketType.user)
		async def gmm(self, ctx):
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				if result == None:
						embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				mns_money = int(n_money) + 50000
				sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(ctx.author.id)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				db.commit()
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")

				embed = discord.Embed(title='💸 | 지급성공', description=f'50,000원을 지급했어요.\n현재 잔액 : `{n_money}`원 입니다.', colour=0xCCFFFF)
				await ctx.send(embed=embed)


		@gmm.error
		async def on_command_error(self, ctx, error):
				if isinstance(error, commands.CommandOnCooldown):
						msg = f'`{int(error.retry_after) // 60}`분`{int(error.retry_after) % 60}`초 뒤에 다시 시도할 수 있습니다.'
						await ctx.send(msg)


		@commands.command(name='ㅅㄱ', aliases=['송금'])
		async def givey(self, ctx, member: discord.Member, *,givemoney):
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result0 = str(result)
				na_money = result0.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				givem = int(givemoney)
				iidd = member.id
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(iidd))
				result1 = cursor.fetchone()
				result2 = str(result1)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")

				if result1 == None:
						embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				if result == None:
						embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				if int(na_money) < int(givem):
						await ctx.send('돈이 부족해요')
						return

				mns_money = int(n_money) + int(givem)
				sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(iidd)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				db.commit()
				mns_money = int(na_money) - int(givem)
				sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(ctx.author.id)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				db.commit()
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				embed = discord.Embed(title='📨 | 송금 성공!',
															description=f'송금 내역 : \n받으시는 분 : <@{iidd}>\n보내시는분 : <@{ctx.author.id}>\n송금 : `{givem}`원\n남은잔액 : `{n_money}`원',
															colour=0xCCFFFF)
				await ctx.send(embed=embed)


		@givey.error
		async def on_command_error(self, ctx, error):
				if isinstance(error, commands.MissingRequiredArgument):
						await ctx.reply('송금할 금액을 적으세요!')


		@commands.command(name='ㅈㄱ', aliases=['저금'])
		async def ina(self, ctx, *, savemoney):
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result0 = str(result)
				na_money = result0.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				givem = int(savemoney)
				iidd = ctx.author.id
				cursor.execute('SELECT user_bank FROM main WHERE user_id = {0}'.format(iidd))
				result1 = cursor.fetchone()
				result2 = str(result1)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")

				if result1 == None:
						embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				if result == None:
						embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				if int(na_money) < int(savemoney):
						await ctx.send('돈이 부족해요')
						return

				mns_money = int(n_money) + int(savemoney)
				sql = 'UPDATE main SET user_bank = ? WHERE user_id = {0}'.format(iidd)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				db.commit()
				mns_money = int(na_money) - int(savemoney)
				sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(ctx.author.id)
				val = (str(mns_money),)
				cursor.execute(sql, val)
				db.commit()
				cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)

				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				embed = discord.Embed(title='🏦 | 저금 성공!', description=f'저금 : `{savemoney}`원\n남은잔액 : `{n_money}`원', colour=0xCCFFFF)
				await ctx.send(embed=embed)


		@ina.error
		async def on_command_error(self, ctx, error):
				if isinstance(error, commands.MissingRequiredArgument):
						await ctx.reply('저금 할 금액을 적으세요!')


		@commands.command(name='ㅌㅈ', aliases=['통장'])
		async def mybank(self, ctx):	

				cursor.execute('SELECT user_bank FROM main WHERE user_id = {0}'.format(ctx.author.id))
				result = cursor.fetchone()
				result2 = str(result)
				n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
				if result == None:
						embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
						await ctx.send(embed=embed)
						return
				embed = discord.Embed(title='💳 | 통장잔액', description=f'현재 잔액 : `{n_money}`원 입니다.', colour=0xCCFFFF)
				await ctx.send(embed=embed)


		@commands.command(name='ㅇㅊ',aliases=['인출','출금','ㅊㄱ'])
		async def out(self, ctx, *, give):
				
			cursor.execute('SELECT user_money FROM main WHERE user_id = {0}'.format(ctx.author.id))
			result = cursor.fetchone()
			result0 = str(result)
			na_money = result0.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
			givem = int(give)
			iidd = ctx.author.id
			cursor.execute('SELECT user_bank FROM main WHERE user_id = {0}'.format(iidd))
			result1 = cursor.fetchone()
			result2 = str(result1)
			n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")

			if result1 == None:
				embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다', colour=0xCCFFFF)
				await ctx.send(embed=embed)
				return
			if result == None:
				embed = discord.Embed(title='❌ | 오류!', description='등록되지 않은 유저입니다\n가입 먼저 진행해주세요\n가입방법 : `ㅇ가입`', colour=0xCCFFFF)
				await ctx.send(embed=embed)
				return
			if int(n_money) < int(givem):
				await ctx.send('돈이 부족해요')
				return

			mns_money = int(na_money) + int(givem)
			sql = 'UPDATE main SET user_money = ? WHERE user_id = {0}'.format(iidd)
			val = (str(mns_money),)
			cursor.execute(sql, val)
			db.commit()
			mns_money = int(n_money) - int(givem)
			sql = 'UPDATE main SET user_bank = ? WHERE user_id = {0}'.format(ctx.author.id)
			val = (str(mns_money),)
			cursor.execute(sql, val)
			db.commit()
			cursor.execute('SELECT user_bank FROM main WHERE user_id = {0}'.format(ctx.author.id))
			result = cursor.fetchone()
			result2 = str(result)
			n_money = result2.replace('(', '').replace(')', '').replace(',', '').replace("'", "")
			embed = discord.Embed(title='💸 | 인출 성공!', description=f'인출 내역 : \n인출 : `{givem}`원\n남은잔액 : `{n_money}`원', colour=0xCCFFFF)
			await ctx.send(embed=embed)
		@out.error
		async def on_command_error(self, ctx, error):
			if isinstance(error, commands.MissingRequiredArgument):
				await ctx.reply('인출 할 금액을 적으세요!')
		
		@commands.command(name = '가위바위보')
		async def rspgame(self, ctx):
			e = await ctx.send(embed=discord.Embed(title='✊ | 가위바위보',description='✌,👊,🖐중 하나를 선택하세요. \n취소할려면 ❌을 선택하세요.', color=0xCCFFFF))
			await e.add_reaction("✌")
			await e.add_reaction('👊')
			await e.add_reaction('🖐') 
			await e.add_reaction('❌') 
			rn = random.randint(1, 3)
			print(rn)
			def check(reaction, user):
					return user == ctx.author and str(reaction.emoji) in ["✌", "👊", "🖐","❌"]

			try:
					reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
		
					if str(reaction.emoji) == '✌':
							if rn == 1:
									await ctx.send('비겼습니다.')
							if rn == 2:
									await ctx.send('졌습니다.')
							if rn == 3:
									await ctx.send('이겼습니다.')

					elif str(reaction.emoji) == '👊':
							if rn == 1:
									await ctx.send('이겼습니다.')
							if rn == 2:
									await ctx.send('비겼습니다.')
							if rn == 3:
									await ctx.send('졌습니다.')

					elif str(reaction.emoji) == '🖐':
							if rn == 1:
									await ctx.send('졌습니다.')
							if rn == 2:
									await ctx.send('이겼습니다.')
							if rn == 3:
									await ctx.send('비겼습니다.')
					elif str(reaction.emoji) == '❌':
						await ctx.send('취소하였습니다.')
			except asyncio.TimeoutError:
					await ctx.channel.send('시간이 초과되었습니다.')			
def setup(bot):
		bot.add_cog(bet(bot))