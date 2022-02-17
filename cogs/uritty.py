import googletrans,requests,warnings,discord,urllib,bs4,re,os,time,datetime,pytz
from urllib.request import urlopen, Request, HTTPError
from discord.ext import commands
from urllib.parse import quote
from bs4 import BeautifulSoup
class ntry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['tr'])
    async def 번역(self, ctx, lang_to, *, args):
        try:
            if lang_to == "한국어": lang_to = "ko"
            elif lang_to == "영어": lang_to = "en"
            elif lang_to == "일본어": lang_to = "ja"
            elif lang_to == "독일어": lang_to = "de"
            elif lang_to == "러시아어": lang_to = "ru"
            elif lang_to == "태국어": lang_to = "th"
            elif lang_to == "중국어-간체": lang_to = "zh-cn"
            elif lang_to == "중국어-번체": lang_to = "zh-tw"
            elif lang_to == "페르시아어": lang_to = "fa"
            elif lang_to == "포르투갈어": lang_to = "pt"
            elif lang_to == "프랑스어": lang_to = "fr"
            elif lang_to == "스페인어": lang_to = "es"
            lang_to = lang_to.lower()
            if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES: await ctx.send("번역할 언어가 잘못되었습니다.")
            text = ' '.join(args)
            t = googletrans.Translator()
            text_t = t.translate(text, dest=lang_to).text
            if lang_to == "ko": lang_to = "한국어"
            elif lang_to == "en": lang_to = "영어"
            elif lang_to == "ja": lang_to = "일본어"
            elif lang_to == "de": lang_to = "독일어"
            elif lang_to == "ru": lang_to = "러시아어"
            elif lang_to == "th": lang_to = "태국어"
            elif lang_to == "zh-cn": lang_to = "중국어-간체"
            elif lang_to == "zh-tw": lang_to = "중국어-번체"
            elif lang_to == "fa": lang_to = "페르시아어"
            elif lang_to == "pt": lang_to = "포르투갈어"
            elif lang_to == "fr": lang_to = "프랑스어"
            elif lang_to == "es": lang_to = "스페인어"
            await ctx.send(embed = discord.Embed(title="번역", color=0x00FFFF).set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjzC2JyZDZ_RaWf0qp11K0lcvB6b6kYNMoqtZAQ9hiPZ4cTIOB").add_field(name=f"{lang_to}", value=f"{text_t}").set_footer(text='???', icon_url=None))
        except HTTPError: await ctx.send("> :x: - 번역 할 말을 적어주세요!")
        except AttributeError: await ctx.send("> :x: - 번역 할 말을 적어주세요!")
        except UnicodeEncodeError: await ctx.send("> :x: - 번역 할 말을 적어주세요!")
    @commands.command()
    async def 날씨(self, ctx):
        try:
            if len(ctx.message.content.split(" ")) == 1: await ctx.send("> :x: - 검색할 지역 적어주세요!")
            else:
                learn = ctx.message.content.split(" ")
                location = learn[1]
                url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={urllib.parse.quote(location+'날씨')}"
                bsObj = self.soup(url)
                todayBase = bsObj.find('div', {'class': 'main_info'})
                todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
                todayTemp = todayTemp1.text.strip()
                todayValueBase = todayBase.find('ul', {'class': 'info_list'})
                todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
                todayValue = todayValue2.text.strip()
                todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
                todayFeelingTemp = todayFeelingTemp1.text.strip()
                todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
                todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
                todayMiseaMongi3 = todayMiseaMongi2.find('dd')
                todayMiseaMongi = todayMiseaMongi3.text
                tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
                tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
                tomorrowTemp2 = tomorrowTemp1.find('dl')
                tomorrowTemp3 = tomorrowTemp2.find('dd')
                tomorrowTemp = tomorrowTemp3.text.strip()
                tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
                tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
                tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
                tomorrowMoring = tomorrowMoring2.text.strip()
                tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
                tomorrowValue = tomorrowValue1.text.strip()
                tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
                tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
                tomorrowAfter1 = tomorrowAllFind[1]
                tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
                tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
                tomorrowAfterTemp = tomorrowAfter3.text.strip()
                tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
                tomorrowAfterValue = tomorrowAfterValue1.text.strip()
                await ctx.send(embed = discord.Embed(title=learn[1]+ ' 날씨 정보', description=learn[1]+ '날씨 정보입니다.', color=0x00FFFF).add_field(name='현재온도', value=todayTemp+'˚', inline=False).add_field(name='체감온도', value=todayFeelingTemp, inline=False).add_field(name='현재상태', value=todayValue, inline=False).add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False).add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False).add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False).add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False).add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False).add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False).add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False).set_footer(text=None, icon_url=None))
        except HTTPError: await ctx.send("> :x: - 올바르지 않는 지역입니다. 다시 확인 해 주세요.")
        except AttributeError: await ctx.send("> :x: - 올바르지 않는 지역입니다. 다시 확인 해 주세요.")
        except UnicodeEncodeError: await ctx.send("> :x: - 올바르지 않는 지역입니다. 다시 확인 해 주세요.")
    @commands.command(aliases=['ㅑㅡㅁㅎㄷ'])
    async def image(self, ctx, *, search):
        try:
            if len(ctx.message.content.split(" ")) == 1: await ctx.send("> :x: - 이미지 검색할 말을 적어주세요!")
            else:
                load = await ctx.send("> ⏳ 이미지 로드 중...")
                options = webdriver.ChromeOptions()
                options.add_argument("headless")
                driver = self.load_chrome_driver()
                driver = webdriver.Chrome(options=options)
                driver.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={search}")
                time.sleep(1)
                driver.find_elements_by_css_selector("._image._listImage")[0].click()
                time.sleep(2)
                img = driver.find_element_by_css_selector("._image").get_attribute("src")
                driver.quit()
                await load.delete()
                await ctx.send(embed = discord.Embed(title=f"이미지 검색 결과({search})", color=0x00FFFF).set_image(url=img).set_footer(text=None, icon_url=None))
        except HTTPError: await ctx.send("> :x: - 이미지가 로드되지 않습니다. 다시 확인 해 주세요.")
        except AttributeError: await ctx.send("> :x: - 이미지가 로드되지 않습니다. 다시 확인 해 주세요.")
        except UnicodeEncodeError: await ctx.send("> :x: - 이미지가 로드되지 않습니다. 다시 확인 해 주세요.")

    @commands.command(name='초대')
    async def invent(self, ctx):
      await ctx.send(embed=discord.Embed(title="🌐 |아린",description="아래의 링크를 눌러 봇을 초대하세요!\n[**Invent**](https://discord.com/api/oauth2/authorize?client_id=794028653171179530&permissions=8&scope=bot)",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF))

    @commands.command(name='hellothisisverification')
    async def _hellothisisverification(self, ctx):
      await ctx.send('ZETA#0088(739673575929282571)')

    @commands.command(name='핑')
    async def ping(self, ctx):
      start = time.perf_counter()
      message = await ctx.send(embed=discord.Embed(title='로딩중', color=0xCCFFFF))
      end = time.perf_counter()
      duration = round((end - start) * 1000)
      pings = round(self.bot.latency * 1000)
      if duration < 100:
        pinglevels = '🔵 매우좋음'
      elif duration < 300:
        pinglevels = '🟢 양호함'
      elif duration < 400:
        pinglevels = '🟡 보통'
      elif duration < 6000:
        pinglevels = '🔴 나쁨'
      else:
        pinglevels = '⚪ 매우나쁨'
      if pings < 100:
        pinglevel = '🔵 매우좋음'
      elif pings < 300:
        pinglevel = '🟢 양호함'
      elif pings < 400:
        pinglevel = '🟡 보통'
      elif pings < 6000:
        pinglevel = '🔴 나쁨'
      else:
        pinglevel = '⚪ 매우나쁨'
		
      embed = discord.Embed(title="🏓 퐁!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCFFFF)
      embed.add_field(name="Discord API", value=f"> {pings}ms", inline=True) 
      embed.add_field(name="메시지 지연시간", value=f"> {duration}ms", inline=True)

      await message.edit(embed=embed)




def setup(bot):
    bot.add_cog(ntry(bot))