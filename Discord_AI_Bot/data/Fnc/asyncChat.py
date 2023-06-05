from playwright.async_api import async_playwright
import asyncio
import json

playwright = None
browser = None
context = None
page = None

async def ChaInt():
	global playwright
	global browser
	global context
	global page
	playwright = await async_playwright().start()
	browser = await playwright.firefox.launch()
	context = await browser.new_context()
	page = await context.new_page()
	await page.goto(f"https://chateverywhere.app/zh")
	await asyncio.sleep(5)
	f = open("data/json/CharacterSet.json", "r", encoding="utf-8")
	Chara = json.load(f)
	text = Chara['Character']
	text = text.replace("&author;", "初始化專員").replace("&guild;", "初始化情報").replace("&channel;", "").replace("&ReferenceSTR;", "").replace("&message;", "嗨嗨（探頭）").replace("&Time;", Get_Time())
	
	return await initChat(text)
	
	
async def ReflashAI():
	global page
	del page
	
	print(f"initialization message: {await ChaInt()}")
	
	print("Page initialization complete!")
	
	await page.screenshot(path="data/example.png")

async def NetWork(text):
	global page
	
	await page.screenshot(path="data/example.png")
	Sstr = ""
	
	while Sstr.find("重新生成") == -1:
		S = await page.query_selector_all(".gap-3")
		for i in range(len(S)):
			#print(f"find Regenerate: {await S[i].inner_text()}")
			Sstr = await S[i].inner_text()
			if Sstr.find("重新生成") != -1:		#wait genelate complete
				break
				
				
	await page.select_option('select', value='langchain-chat')
	await page.get_by_placeholder("輸入訊息").fill(f"{text}")
	await page.get_by_placeholder("輸入訊息").press("Enter")
	
	
	Sstr = ""
	while Sstr.find("重新生成") != -1:
		S = await page.query_selector_all(".gap-3")
		for i in range(len(S)):
			#print(f"find Stop: {await S[i].inner_text()}")
			Sstr = await S[i].inner_text()
			if Sstr.find("重新生成") == -1:		#wait genelate start
				break
	await page.screenshot(path="data/example.png")
	Sstr = ""
	while Sstr.find("重新生成") == -1:
		S = await page.query_selector_all(".gap-3")
		for i in range(len(S)):
			#print(f"find Regenerate: {await S[i].inner_text()}")
			Sstr = await S[i].inner_text()
			if Sstr.find("重新生成") != -1:		#is genelate complete
				return "Ok"
	

async def chai(text):
	global page
	
	await page.screenshot(path="data/example.png")
	Sstr = ""
	
	while Sstr.find("重新生成") == -1:
		S = await page.query_selector_all(".gap-3")
		for i in range(len(S)):
			#print(f"find Regenerate: {await S[i].inner_text()}")
			Sstr = await S[i].inner_text()
			if Sstr.find("重新生成") != -1:		#wait genelate complete
				break
				
				
	await page.select_option('select', value='default')
	await page.get_by_placeholder("輸入訊息").fill(f"中文的話請用繁體中文做回覆,如有使用程式碼區塊請使用/Code/語言類型/ln //程式碼 /Code/幫我做包覆(例如:\n/Code/py/lnprint(Str)\n/Code/),並且請你以角色的視角給予些許表情符號、emoji回應，不用每一則訊息都回應表情符號，格式化的回應如下<Reactions>[🤮,❌,❤,❓,⭕]</Reactions>,回應一定要使用Reactions的HTML標籤包覆，任何的表情符號、emoji都可以使用，數量沒有限定，如果沒有要做回應請給我<Reactions>[None]</Reactions>，如果有回應表情符號、emoji則不需要回應<Reactions>[None]</Reactions>,{text}")
	await page.get_by_placeholder("輸入訊息").press("Enter")
	
	
	Sstr = ""
	while Sstr.find("重新生成") != -1:
		S = await page.query_selector_all(".gap-3")
		for i in range(len(S)):
			#print(f"find Stop: {await S[i].inner_text()}")
			Sstr = await S[i].inner_text()
			if Sstr.find("重新生成") == -1:		#wait genelate start
				break

	Sstr = ""
	while Sstr.find("重新生成") == -1:
		S = await page.query_selector_all(".gap-3")
		for i in range(len(S)):
			#print(f"find Regenerate: {await S[i].inner_text()}")
			Sstr = await S[i].inner_text()
			if Sstr.find("重新生成") != -1:		#is genelate complete
				break

	div = await page.query_selector_all(".text-base")
	output_text = await div[-1].inner_text()
	
	output_text = output_text.replace("/ln", "\n")
	output_text = output_text.replace("/Code/", "```")
	output_text = output_text.replace("複製代碼","")
	
	await page.screenshot(path="data/example.png")
	return output_text

async def initChat(text):
	global page
	
	await page.screenshot(path="data/example.png")
	await page.get_by_placeholder("輸入訊息").click()
	await page.get_by_placeholder("輸入訊息").fill(text)
	await page.select_option('select', value='default')
	await page.get_by_placeholder("輸入訊息").press("Enter")
	await page.screenshot(path="data/example.png")
	
	Sstr = ""
	while Sstr.find("重新生成") == -1:
		S = await page.query_selector_all(".gap-3")
		for i in range(len(S)):
			#print(f"find Regenerate: {await S[i].inner_text()}")
			Sstr = await S[i].inner_text()
			if Sstr.find("重新生成") != -1:		#is genelate complete
				break
	
	div = await page.query_selector_all(".text-base")
	output_text = await div[-1].inner_text()
	

	return output_text


def Pwd(Pwd):
	Str = ""
	for i in range(len(Pwd)):
		Str += "*"
	return Str
	
def Get_Time():
	import datetime
	now = datetime.datetime.now()
	return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
	ChaInt()
	while True:
		print(chai(input(">")))
