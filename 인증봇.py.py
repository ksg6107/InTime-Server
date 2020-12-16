import discord

client = discord.Client()

@client.event
async def on_ready():
    #봇이 준비가 되면 콘솔 창에 "ready" 가 출력 됨.
    print("ready")



@client.event

async def on_message(message):
    #channels 는 ["채널 이름"] 이다
    channels = ["🎊ㅣ인증신청"]
    #만약 메시지 채널이 channels 안에 있다면 계속 진행
    if str(message.channel) in channels:
        #시작 스위치 : !인증 라는 메시지가 보이면
        if message.content.startswith("!뉴비인증"):
            #role 값 지정
            role = discord.utils.get(message.guild.roles, id=int("787312552438530070"))
            #메시지 를 적은사람에게 role 을 추가 해줌.
            await message.author.add_roles(role)



#구동 할 봇 토큰
client.run("Nzg3NTg5Mjg5OTUzMDY3MDE4.X9XJrw.EloVNbrvm7IDV60m9vJm-jd8QNM")