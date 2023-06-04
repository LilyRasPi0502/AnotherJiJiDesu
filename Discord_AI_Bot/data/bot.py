# -*- coding: utf-8 -*-

from discord.ext import tasks
from discord.ext import commands
from Fnc.asyncChat import *

import datetime
import discord
import asyncio
import json

intents		= discord.Intents.default()
intents.message_content = True
intents.members = True

config		= open("data/json/DC_config.json", "r", encoding="utf-8")
conf		= json.load(config)
bot_ID		= conf["bot_ID"]
Master_ID	= conf["Master_ID"]
Token		= conf["DC_key"]

class MyBot(commands.Bot):
	
	def __init__(self, command_prefix, intent):
		commands.Bot.__init__(self, command_prefix=command_prefix, intents=intent)
		self.add_commands()
	
	async def on_ready(self):
		self.message1 = f"正在使用身分: {self.user}({self.user.id})"
		self.message2 = f"正在使用身分: {self.user}({self.user.id})"
		print(self.message1)
		self.changeActivity.start()
		await self.Reflash_Character()
		self.Reflash_CharacterAI.start()
		
	async def on_message(self, message):
		#排除自己的訊息，避免陷入無限循環
		if message.author == self.user:
			return
		#設定是否已回覆旗標
		send = True

		#列印接收到的訊息
		print(f"[{Get_Time()}] Get Message from {str(message.guild)}.{str(message.channel)}.{str(message.author)}: {str(message.content)}")
		
		#判斷有無回覆訊息
		if message.reference is not None:
			#獲取被回覆的訊息
			ctx = await message.channel.fetch_message(message.reference.message_id)
		
			#如果被回覆的對象是此機器人
			if (ctx.author == self.user):
				await self.cmd(message, f"{self.ID_To_Name(message.content)}")
				send = False
	
		#指令程序
		if ((message.content.find(bot_ID) != -1) or (self.is_Mention(message.content))) and (send == True):
	
			await self.cmd(message, self.ID_To_Name(message.content))
			send = False

	async def Reaction(self, message):
		text = await self.ChangeText(message, f"你是{str(self.user)[:-5]}，請你以{str(self.user)[:-5]}的視角給予頻道內的訊息些許表情符號、emoji回應，不用每一則訊息都回應，基本回應格式如下[🤮,❌,❤,❓,⭕]，任何的表情符號、emoji都可以使用，數量沒有限定，如果沒有要做回應請給我[None]，如果明顯不是找{str(self.user)[:-5]}請給我[None]，如果有回應表情符號、emoji則不需要回應[None]，除了格式化的回應請不要做出任何文字回應，來自&guild;.&channel;的[&author;]的訊息如下：「&message;」")
		Str = await chai(text)
		Str = Str.split("[")[-1]
		Str = Str.split("]")[0]
		if Str.find("None") == -1:
			if Str.find(",") != -1:
				emojiList = Str.split(",")
				for emoji in emojiList:
					try:
						await message.add_reaction(emoji)
					except:
						pass
			else:
				try:
					await message.add_reaction(Str)
				except:
					pass


	#指令讀取
	async def cmd(self, ctx, cmd):
		await self.Reaction(ctx)
		if cmd.find("Replace ") != -1:					#測試功能:取代訊息
			if ctx.reference is not None:
				message = await ctx.channel.fetch_message(ctx.reference.message_id)
				print(f"[{Get_Time()}] Replace message of {str(ctx.guild)}.{str(ctx.channel)}: {message.content}")
				if len(message.content) > 0:
					await self.sender(ctx, message.content)
				if message.attachments:
					FileName	= f"./data/file/file.{message.attachments[0].url.split('/')[-1].split('.')[-1]}"
					res2 = requests.post(message.attachments[0].url)
					with open(FileName, mode='wb') as f:
						f.write(res2.content)
					await self.FileSender(ctx, FileName)
				await message.delete()
			else:
				print(f"[{Get_Time()}] Replace message of {str(ctx.guild)}.{str(ctx.channel)}: {cmd.split('Replace ')[1]}")
				await ctx.channel.send(cmd.split("Replace ")[1])
				if ctx.attachments:
					FileName	= f"./data/file/file.{ctx.attachments[0].url.split('/')[-1].split('.')[-1]}"
					res2 = requests.post(ctx.attachments[0].url)
					with open(FileName, mode='wb') as f:
						f.write(res2.content)
					await self.FileSender(ctx, FileName)
			await ctx.delete()
		
		elif cmd.find("ReAI") != -1:					#測試功能:Reflash CharacterAI page
			async with ctx.channel.typing():
				
				Str = await self.Reflash_Character()
			await ctx.reply(Str)
			print(f"[{Get_Time()}] Reply message to {str(ctx.guild)}.{str(ctx.channel)}.{ctx.author}: {Str}")
		elif cmd.find("CMD") != -1:					#測試功能:CMD
			import os
			async with ctx.channel.typing():
				os.system(cmd.split("CMD ")[-1])
			msg = await ctx.reply(f"Used command: {cmd.split('CMD ')[-1]}")
			print(f"[{Get_Time()}] Reply message to {str(ctx.guild)}.{str(ctx.channel)}.{ctx.author}: {msg.content}")
		elif cmd.find("--Search") != -1:				#測試功能:Search
			async with ctx.channel.typing():
				f = open("data/json/CharacterSet.json", "r", encoding="utf-8")
				Chara = json.load(f)
				text = await self.ChangeText(ctx, f"{Chara['Net']}")
				Str = await NetWork(f"[{Get_Time()}] {cmd.replace('--Search', '')[-1]}")
				Str = await chai(text)

				try:
					msg = await ctx.reply(Str)

				except:
					f = open("data/json/CharacterSet.json", "r", encoding="utf-8")
					text = await self.ChangeText(ctx, f"{Chara['Err']}")
					Str = await chai(text)
					msg = await ctx.reply(Str)
			print(f"[{Get_Time()}] Reply message to {str(ctx.guild)}.{str(ctx.channel)}.{ctx.author}: {msg.content}")
	
		else:								#暴力連接chatGPT

			async with ctx.channel.typing():
				f = open("data/json/CharacterSet.json", "r", encoding="utf-8")
				Chara = json.load(f)
				text = await self.ChangeText(ctx, f"{Chara['Character']}")
				Str = await chai(text)

				try:
					msg = await ctx.reply(Str)

				except:
					f = open("data/json/CharacterSet.json", "r", encoding="utf-8")
					text = await self.ChangeText(ctx, f"{Chara['Err']}")
					Str = await chai(text)
					msg = await ctx.reply(Str)

			print(f"[{Get_Time()}] Reply message to {str(ctx.guild)}.{str(ctx.channel)}.{ctx.author}: {msg.content}")

	async def ChangeText(self, ctx, text):
		if ctx.reference is not None:
			f = open("data/json/CharacterSet.json", "r", encoding="utf-8")
		
			msg = f"{json.load(f)['Reference']}"
			rectx = await ctx.channel.fetch_message(ctx.reference.message_id)
			msg = msg.replace("&reference;", str(self.ID_To_Name(rectx.content)))
			msg = msg.replace("&author;", str(rectx.author)[:-5])
		else:
			msg = ""
		text = text.replace("&author;", str(ctx.author)[:-5])
		text = text.replace("&guild;", str(ctx.guild))
		text = text.replace("&channel;", str(ctx.channel))
		text = text.replace("&Master_ID;", str(Master_ID))
		text = text.replace("&bot_ID;", str(bot_ID))
		text = text.replace("&message;", str(self.ID_To_Name(ctx.content)))
		text = text.replace("--Search", "")
		text = text.replace("&ReferenceSTR;", str(self.ID_To_Name(msg)))
		text = text.replace("&Time;", str(Get_Time()))
		return text


	#傳送訊息用
	async def sender(self, Message, Str):
		await Message.channel.send(Str)
		print(f"[{Get_Time()}] Send message to {str(Message.guild)}.{str(Message.channel)}: {Str}")

	#傳送檔案用
	async def FileSender(self, Message, File):
		print(f"[{Get_Time()}] Send file to {str(Message.guild)}.{str(Message.channel)}")
		await Message.channel.send(file=discord.File(File))

	#是否被文字提及
	def is_Mention(self, Message):
		My_Name = open("data/json/Name.json", "r", encoding="utf-8")
		data			=	json.load(My_Name)
		NameList		=	data["Name"]
		for i in range(len(NameList)):
			FindName	=	NameList[str(i)]
			if Message.find(FindName) != -1:
				return True
		return False


	#將代號或ID指向默認的名字
	def ID_To_Name(self, Message):
		My_Name = open("data/json/Name.json", "r", encoding="utf-8")
		data			=	json.load(My_Name)
		if Message.find("Rename") != -1:
			return Message
		return Message.replace(bot_ID, data["DefaultName"])
	
	#更改機器人狀態
	@tasks.loop(seconds=5.0)
	async def changeActivity(self):
		f = open("data/json/Stetas.json", "r", encoding="utf-8")
		data			=	json.load(f)
		State			=	data["State"]
		await self.change_presence(activity=discord.Activity(name=State, type=0))
		
	utc = datetime.timezone.utc
	times = [
		datetime.time(hour=0, tzinfo=utc),
		datetime.time(hour=8, tzinfo=utc),
		datetime.time(hour=16, tzinfo=utc)
	]
	#Reflash CharacterAI
	@tasks.loop(time=times)
	async def Reflash_CharacterAI(self):
		await self.Reflash_Character()
	
	async def Reflash_Character(self):
		await ReflashAI()
		
		print("On_Reflash")
		return "Ok"
		
	def add_commands(self):
		@self.command(name="status", pass_context=True)
		async def status(ctx):
			print(ctx)


def bot1():
	# Your code here
	bot = MyBot(command_prefix="!", intent=intents)
	bot.run(Token)

	

#獲取時間
def Get_Time():
	now = datetime.datetime.now()
	return now.strftime("%Y-%m-%d %H:%M:%S")



bot1()
