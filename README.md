# AnotherJiJiDesu
 - 本專案將使用python與網頁交互,使網頁版的AI語言模型串接在Discord機器人上面
 - 此專案可用來做性癖機器人(目前使用的模型其網站沒有明文規定不能做色情的問答)

## 若有侵權疑慮將會下架此儲存庫<br>(If there is any infringement concern, this repository will be taken down)

# How to use?(好阿都不要教阿)
在Launcher.exe的目錄下使用`python Launchar.py`指令或是直接在windows環境下使用Launcher.exe

# 環境建置
本程式使用火狐瀏覽器(需要安裝Firefox)
另外還要python

還有*DC API for Python*在setup-lib檔案裏面有最低限度的安裝指令

安裝相依庫時可以先前往data/json填寫資料

Stetas.json -> 正在玩 XXX 的那個(機器人活動狀態)

CharacterSet.json -> 要傳給AI的設定(角色設定等等的)

DC_config.json -> 設定DC bot key跟Bot ID還有持有者ID

Name.json -> 設定機器人默認名稱與別名(這個必填不然只要講話機器人就會回覆)

到這裡就可以開啟機器人來玩了

↓成功啟動大概像這樣<br>
![image](https://github.com/LilyRasPi0502/AnotherJiJiDesu/assets/115215163/ef8b6f6c-e805-499b-a628-726f678c12b7)



目前應該是沒啥問題(<sub>有問題的只有我這個python證照考不過的垃圾</sub>)

# 預設操作指令
 - Replace
   - `XXX Replace String`
     - 可讓名字為XXX的機器人講出String
   - `XXX Replce this`(回覆任意訊息)
     - 可讓名字為XXX的機器人講出被回覆的訊息
 - ReAI
   - `XXX ReAI`
     - 可讓名字為XXX的機器人重整AI頁面並且清除較早的生成紀錄
   - `XXX OOO ReAI`
     - 可讓名字為XXX以及OOO的機器人重整AI頁面並且清除較早的生成紀錄
 - --Search
   - `Search XXX幫我找OO`
     - 可讓名字為XXX的機器人搜尋OO的資料並且用角色的語氣幫你介紹(不過正確率還不高<sub>對不起是我在爛</sub>)
 - Restart
   - `OOO Restart`
     - 可讓名字為OOO的機器人重新啟動(還沒詳細測試過<sub>對不起是我在爛</sub>)
 

# 更新日誌

- 20230519
  - 從JiJiDesu(<https://github.com/LilyRasPi0502/JiJiDesu>)搬移成不用登入帳號的AI聊天網站<b>chateverywhere</b>(<https://chateverywhere.app/zh>)
- 20230523
  - 更新data/bot.py:新增指令`--Search 文字`可藉由<b>chateverywhere</b>連網功能搜尋資料(雖然正確率還不高<sub>對不起是我在爛</sub>)
- 20230524
  - 更新data/bot.py:調整指令傳送資料
  - 更新data/json/CharacterSet.json:對應內部使用資料
- 20230604
  - 更新data/bot.py:可回覆表情符號
- 20230606
  - 更新data/bot.py:回覆表情符號架構
  - 更新data/Fnc/asyncChat.py:整合回覆表情符號架構(應該沒問題？<sup>有問題的只有我這個python證照沒考過的拉機</sup>)
- 20230608
  - 更新data/bot.py:新增Restart指令重啟機器人
- 20230609
  - 更新Launchar.py:應該能支援24小時不間斷執行
