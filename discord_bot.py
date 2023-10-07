import discord
from discord.ext import commands, tasks
import datetime
import asyncio
import operate_db as db

TABLE_NAME = "toilet0"
TOKEN = "***"

def create_bot():
    a = 0
    b = 0
    c = a+b

    intents = discord.Intents.default()
    intents.members = True  # メンバー管理の権限
    intents.message_content = True  # メッセージの内容を取得する権限

    # Botをインスタンス化
    bot = commands.Bot(
        command_prefix="$",
        case_insensitive=True,
        intents=intents  # 権限を設定
    )

    @bot.event
    async def on_ready():
        print("Bot is ready!")
        # タイマーを開始
        send_variable_values.start()


    @tasks.loop(minutes=10)  # 10分ごとに実行
    async def send_variable_values():
        d_now,t_now = db.current_time()
        connection = db.connect_database()
        result_A = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '1' AND (date =  '{}' )".format(d_now))
        result_B = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '2' AND (date =  '{}' )".format(d_now))
        a = len(result_A)
        b = len(result_B)
        c = a+b
        connection.close()
         
        # チャンネルIDを指定してチャンネルを取得
        channel = bot.get_channel(1159166408589058119)  # CHANNEL_IDを実際のチャンネルのIDに置き換える

        if channel:
            message = f"aの使用回数は{a}回、bの使用回数は{b}回です。トータル{c}回です。"
            # メッセージを送信
            await channel.send(message)


    @send_variable_values.before_loop
    async def before_send_variable_values():
        await bot.wait_until_ready()  # Botが完全に起動するのを待つ

    @bot.command()
    async def get_a(ctx):
        print(a)
        d_now,t_now = db.current_time()
        connection = db.connect_database()
        result_A = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '1' AND (date =  '{}' )".format(d_now))
        a_n = len(result_A)
        connection.close()
        """変数aの値を表示するコマンド"""
        await ctx.send(f" {d_now}  {t_now} 時点での aの使用回数は{a_n}回です。")

    @bot.command()
    async def get_b(ctx):
        d_now,t_now = db.current_time()
        connection = db.connect_database()
        result_B = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '2' AND (date =  '{}' )".format(d_now))
        b_n = len(result_B)
        connection.close()
        """変数bの値を表示するコマンド"""
        await ctx.send(f" {d_now}  {t_now} 時点でのbの使用回数は{b_n}回です。")

    @bot.command()
    async def get_total(ctx):
        d_now,t_now = db.current_time()
        connection = db.connect_database()
        result_A = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '1' AND (date =  '{}' )".format(d_now))
        result_B = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '2' AND (date =  '{}' )".format(d_now))
        a_n = len(result_A)
        b_n = len(result_B)
        c_n = a_n + b_n
        connection.close()
        """変数cの値を表示するコマンド"""
        await ctx.send(f" {d_now}  {t_now} 時点でのトータル回数は{c_n}回です。")
        
    @bot.command()
    async def get_yesterday(ctx):
        d_previous = db.previous_date()
        connection = db.connect_database()
        result_A = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '1' AND (date =  '{}' )".format(d_previous))
        result_B = db.read_table(connection,TABLE_NAME,"time,date ,name ",option="WHERE name = '2' AND (date =  '{}' )".format(d_previous))
        a_p = len(result_A)
        b_p = len(result_B)
        c_p = a_p + b_p
        connection.close()
        """変数cの値を表示するコマンド"""
        await ctx.send(f"昨日の aの使用回数は{a_p}回、bの使用回数は{b_p}回です。トータル{c_p}回です。")

    
    return bot

# ボットを作成
bot = create_bot()

# トークンを設定してボットを起動
bot.run(TOKEN)
