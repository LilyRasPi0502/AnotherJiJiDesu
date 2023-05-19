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

	"""
	if page.url.find("https://chat.openai.com/chat") == -1:
		await Login(0)
	
		await ClickAd()
		
	"""
	
	print("Page initialization complete!")
	
async def Login(arg):
	global page
	config		= open("data/json/chatGPT_Config.json", "r", encoding="utf-8")
	conf		= json.load(config)

	Login = await page.wait_for_selector(".btn-primary")
	await Login.click()
	
	if arg == 0:
		print("Click Login button")
	await page.screenshot(path="data/example.png")
	
	Email = await page.wait_for_selector(".input")
	await Email.fill(conf["Account"])
	await Email.press("Enter")
	if arg == 0:
		print(f"Enter Account: {conf['Account']}")
	await page.screenshot(path="data/example.png")
			
	PW = await page.wait_for_selector(".input")
	await PW.fill(conf["Password"])
	await PW.press("Enter")
	if arg == 0:
		print(f"Enter Password: {Pwd(conf['Password'])}")
	await page.screenshot(path="data/example.png")
			
	print("chatGPt on login")
	
async def ClickAd():

	Sstr = ""
	while True:
		try:
			ADB = await page.query_selector_all(".mb-5")
		except:
			ADB = None
		await page.screenshot(path="data/example.png")
		for i in range(len(ADB)):
			Sstr = await ADB[i].inner_text()
			if Sstr.find("ChatGPT") != -1:
				break
		if Sstr.find("ChatGPT") != -1:
			break
			
	for i in range(3):
		Sstr = ""
		ADB = await page.query_selector_all(".btn")
		for i in range(len(ADB)):
			Sstr = await ADB[i].inner_text()
			if Sstr.find("Next") != -1 or Sstr.find("Done") != -1:
				await ADB[i].click()
		await asyncio.sleep(5)
	await page.screenshot(path="data/example.png")
	print("Tour skipped")
	
async def ReflashAI():
	global page
	
	await page.reload()
	
	await asyncio.sleep(5)
	
	if page.url.find("https://chat.openai.com/chat") == -1:
		Login = await page.query_selector(".btn-primary")
		if str(Login).find("NoneType") != -1:
			if await Login.is_visible():
				await Login(1)
				await ClickAd()
	await asyncio.sleep(1)
	print(f"initialization message: {await initChat('嗨嗨')}")
	await page.screenshot(path="data/example.png")

async def selectChat():
	global page
	config		= open("data/json/chatGPT_Config.json", "r", encoding="utf-8")
	conf		= json.load(config)
	Chat = ".gap-3"
	ChatName = conf["ChatName"]
	Sstr = ""
	
	while True:
		try:
			S = await page.query_selector_all(Chat)
		except:
			S = None
		if S != None:
			for i in range(len(S)):
				Sstr = await S[i].inner_text()
				if Sstr.find(ChatName) != -1:
					await S[i].click()
					print(f"select chat name: {ChatName}")
					break
		if Sstr.find(ChatName) != -1:
			break
		
	await page.screenshot(path="data/example.png")

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
				
				
	await page.get_by_placeholder("輸入訊息").fill(text)
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
	
	output_text = output_text.replace("ChatGPT\n!", "")
	output_text = output_text.replace("ChatGPT", "")
	output_text = output_text.replace("This content may violate our content policy. If you believe this to be in error, please submit your feedback — your input will aid our research in this area.","")
	
	await page.screenshot(path="data/example.png")
	return output_text

async def initChat(text):
	global page
	
	await page.screenshot(path="data/example.png")
	
	await page.get_by_placeholder("輸入訊息").fill(text)
	await page.get_by_placeholder("輸入訊息").press("Enter")
	
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
	
	output_text = output_text.replace("ChatGPT\n!", "")
	output_text = output_text.replace("ChatGPT", "")
	output_text = output_text.replace("This content may violate our content policy. If you believe this to be in error, please submit your feedback — your input will aid our research in this area.","")
	

	return output_text


def Pwd(Pwd):
	Str = ""
	for i in range(len(Pwd)):
		Str += "*"
	return Str
	
def Get_Time():
	now = datetime.datetime.now()
	return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
	ChaInt()
	while True:
		print(chai(input(">")))
