import json, time, pytz, requests, datetime, asyncio, discord, os, random
import sqlite3
from discord.utils import get
from discord.ext import commands
from typing import Union

class user_server_infor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
		
    @commands.command(name='유저정보')
    async def userif(self, ctx, user: discord.Member):
      date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
      data = user.joined_at
      embed = discord.Embed(title="❓ | 유저 정보", timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xCCFFFF)
      embed.add_field(name="이름", value=user.name, inline=True)
      embed.add_field(name="태그", value=f'#{user.discriminator}', inline=True)
      embed.add_field(name="별명", value=user.display_name, inline=True)
      embed.add_field(name="아이디", value=user.id, inline=True)  # verified
      embed.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + '일 ' + str(date.hour) + '시 ' + str(date.minute) + '분 ' + str(date.second) + '초', inline=True)
      embed.add_field(name="서버 가입일", value=str(data.year) + "년 " + str(data.month) + "월 " + str(data.day) + '일 ' + str(data.hour) + '시 ' + str(data.minute) + '분 ' + str(data.second) + '초', inline=True)
      embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
      embed.set_thumbnail(url=user.avatar_url)
      await ctx.channel.send(embed=embed)


    @userif.error
    async def on_command_erro(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        date = datetime.datetime.utcfromtimestamp(((int(ctx.author.id) >> 22) + 1420070400000) / 1000)
        data = ctx.author.joined_at
        embed = discord.Embed(title="❓ | 유저 정보", timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xCCFFFF)# bot.user.discriminator
        embed.add_field(name="이름", value=ctx.author.name, inline=True)
        embed.add_field(name="태그", value=f'#{ctx.author.discriminator}', inline=True)
        embed.add_field(name="별명", value=ctx.author.display_name, inline=True)
        embed.add_field(name="아이디", value=ctx.author.id, inline=True)  # verified
        embed.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + '일 ' + str(date.hour) + '시 ' + str(date.minute) + '분 ' + str(date.second) + '초', inline=True)
        embed.add_field(name="서버 가입일",value=f"{str(data.year)}년 {str(data.month)}월 {str(data.day)}일 {str(data.hour)}시 {str(data.minute)}분 {str(data.second)}초", inline=True)
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)


    @commands.command(name='서버정보')
    async def _severinfo(self, ctx):
      embed = discord.Embed(title="서버 정보", timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xCCFFFF)  # 0xCCFFFF
      embed.add_field(name="서버 이름", value=ctx.guild.name, inline=False)
      embed.add_field(name="서버 아이디", value=ctx.guild.id, inline=False)
      embed.add_field(name="서버 제작일", value=ctx.guild.created_at.strftime('20%y년%m월%d일'), inline=False)
      embed.add_field(name="서버 멤버", value=f'{ctx.guild.member_count}명', inline=False)
      embed.add_field(name="서버 주인 아이디", value=f'{ctx.guild.owner_id}', inline=False)
      embed.add_field(name="서버 역할수", value=f'{len(ctx.guild.roles)}개', inline=False)
      embed.add_field(name="서버 채팅채널", value=f'{len(ctx.guild.text_channels)}개', inline=False)
      embed.add_field(name="서버 음성채널", value=f'{len(ctx.guild.voice_channels)}개', inline=False)
      embed.add_field(name="서버 부스트 ", value=f'{ctx.guild.premium_subscription_count}번', inline=False)
      embed.add_field(name="서버 인증 레벨", value=f'{ctx.guild.verification_level}', inline=False)
      embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
      embed.set_thumbnail(url=ctx.guild.icon_url)
      await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(user_server_infor(bot))