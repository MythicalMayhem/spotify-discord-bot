import time
import discord
import threading
from discord.ext import tasks
from fyupdate import fyupdate
from keepalive import keep_alive
from env import client, disTOKEN, QUEUE,authlink,forDeletion

time.sleep(7)


def qq():
    while True:
        print(' [**] queue : '+str(len(QUEUE)), end='\r')
        time.sleep(1)
t1 = threading.Thread(target=qq)


#@tasks.loop(seconds=1800)
#async def lpchktwo():
#    while len(forDeletion) != 0:
#        delmsgid = list(forDeletion.keys())[0]
#        delmsgchanl = list(forDeletion.values())[0]
#        fordelmsg = await delmsgchanl.fetch_message(delmsgid)
#        await fordelmsg.delete()
#        forDeletion.pop(delmsgid)
#    time.sleep(1)

@tasks.loop(seconds=5)
async def lpchk():
    while len(QUEUE) != 0:
        uid = list(QUEUE.keys())[0]
        cod = list(QUEUE.values())[0][0]
        typ = list(QUEUE.values())[0][1]
        cid = list(QUEUE.values())[0][2]
        await fyupdate(uid,cod,typ,cid)


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="//fy"))
    print('      innitiated      ')
    t1.start()
    lpchk.start()
#    lpchktwo.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == '//fy':
        return
    elif message.content.startswith('//stats'):
        uid = message.channel.id
        u = client.get_channel(uid)
        ss = message.content.split()
        if not len(ss) == 2:
            await u.send("""```
//stats {type}
           ^^^^^^
choose tracks, artists or genres```""")
        else:
            await message.add_reaction('\U0001F3B5')
            await message.reply('Go to this link and paste the last url here ! \n >' + authlink+'<')
            res = await client.wait_for("message",check=lambda x: x.content.startswith('https://mythicalmayhem.github.io/spotify-api/'))
            if res:
                await res.channel.send(res.author.mention + 'fetching your data...')         
                rescontent = res.content
                if res.channel.type is not discord.ChannelType.private:
                    await res.delete()
                code = str(rescontent).split('?code=')[1]
                ki = str(res.author.id)
                uid = res.channel.id
                QUEUE.update({ki:[code,ss[len(ss)-1],uid]})
              
keep_alive()
try:
  client.run(disTOKEN)
except Exception as e:
  print(e)