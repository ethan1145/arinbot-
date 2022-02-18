from webserver import keep_alive
import json, time, pytz, requests, datetime, asyncio, discord, os, random, sqlite3
from discord.utils import get
from discord.ext import commands
from typing import Union

# 파일 데이터 가져오기 =================================================

with open('date.json', 'r', encoding='utf-8-sig') as dt:
	dt = json.load(dt)


bot = commands.Bot(command_prefix=commands.when_mentioned_or('아린 ','아린아 ','ㅇ')) #
bot.remove_command("help")

# 파일 변수설정
prexfix = ['아린 ','ㅇ','아린아 ']
vsison = dt['version']
owner_id = dt['owner_id']
token = dt['token']
# 봇 활동메시지 =================================================

@bot.event
async def on_ready():
	print("Cogs")
	for file in os.listdir("cogs"):
		if file.endswith(".py"):
			bot.load_extension(f"cogs.{file[:-3]}")			
			print(f"{file[:-3]}를(을) 로드 함")
	print(f'\nLog\n{bot.user.name}으로 접속됨')
	asda = random.choice(prefix)
	await bot.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.listening, name=f"{asda}도움말"))
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.CommandOnCooldown) or isinstance(error, commands.CommandNotFound):
      return
    else:
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="🚫 권한부족", description="봇의 권한이 부족합니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))
      else:
        await ctx.send(embed=discord.Embed(title="🚫 오류 발생",description=f"[에러] : {error}",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))
    print(error)

@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title=f"📌 {bot.user.name} 명령어", color=0xCCFFFF)
    embed.add_field(name="📝 | 정보",value=f"`{prefix}정보`,`{prefix}핑`,`{prefix}서버정보`,`{prefix}개발자`,`{prefix}서포터서버`,`{prefix}초대`",inline=False)
    embed.add_field(name="💻 | 미니게임",value=f"`{prefix}돈줘 (ㄷㅂㄱ)`,`{prefix}돈 (ㄷ)`,`{prefix}도박 (ㄷㅂ)`,`{prefix}송금 [멘션] [금액](ㅅㄱ)`,`{prefix}가입 (ㄱㅇ)`,`{prefix}저금 [금액] (ㅈㄱ)`,`{prefix}출금 [금액](ㅊㄱ)`",inline=False)
    embed.add_field(name="⚙️ | 서버관리", value=f"`{prefix}킥`,`{prefix}밴`,`{prefix}삭제 [1~100]`", inline=False)
    embed.add_field(name="🔭 | 유틸리티", value=f"`{prefix}타이머`", inline=False)
    await ctx.channel.send(embed=embed) 
keep_alive()
bot.run(token)
