import requests
from env import cli,topArtists,topTracks,client,trial,QUEUE,forDeletion
async def fyupdate(K,c,tp,cd):
    kkk = K
    ckk = c
    tpkk = tp
    cdkk = cd 
    QUEUE.pop(K)
    K = kkk
    c = ckk
    tp = tpkk
    cd = cdkk
    chnl = client.get_channel(cd)
    u  = await client.fetch_user(K)
    
    headers = {'Authorization': f'Basic {cli}',}
    data = {'grant_type': 'authorization_code','code': c,'redirect_uri': 'https://mythicalmayhem.github.io/spotify-api/',}
    try:
        res = requests.post('https://accounts.spotify.com/api/token',headers=headers,data=data).json()
        spotify_token = res["access_token"]
        def req (lnk):
            return requests.get(lnk,headers={
            "Content-Type": "application/json",
            "Authorization":f"Bearer {spotify_token}"}).json()
        if tp == 'tracks':
            tracks = []
            tt = req(topTracks)
            for i in range(len(tt['items'])):
                q = tt['items'][i]['name']
                i = i + 1
                tracks.append(f'[{i}] - {q} \n')        
            trk = u.mention + '\n' +'__**Most Played Tracks**__' + '\n```' + ''.join(tracks[0:trial]) + '```'+ '> this message is set for deletion in less than 30 minutes '
            mess = await chnl.send(trk)
            messid = mess.id
            messch = mess.channel
            forDeletion.update({messid:messch})
        elif tp == 'genres' or tp == 'artists':
            ta = req(topArtists)
            if tp == 'artists':
                artists = []
                for i in range(len(ta['items'])):
                    q = ta['items'][i]['name']
                    i = i + 1
                    artists.append(f'[{i}] - {q} \n')
                art = u.mention + '\n' + '__**Your Favourite Artists**__' + '\n```' + ''.join(artists[0:trial]) + '```'+ '> this message is set for deletion in less than 30 minutes '
                mess = await chnl.send(art)
                messid = mess.id
                messch = mess.channel
                forDeletion.update({messid:messch})
            elif tp == 'genres':
                genres = []
                for i in range(len(ta['items'])):
                    q = ta['items'][i]['genres']    
                    genres.append(q)
                al = []
                for i in genres:
                    for j in i:
                        al.append(j)
                up = []
                for i in al:
                    if i in up:
                        continue
                    else:
                        up.append(i)
                tweak = []
                count = 1
                for i in up:
                    if i == up[len(up)-1]:
                        i = f'[{count}] - {i} \n'
                        tweak.append(i)        
                        count = count + 1
                    else:    
                        i = f'[{count}] - {i} \n'
                        tweak.append(i)        
                        count = count + 1
                genres = tweak
                gnr = u.mention + '\n' +'__**Your Taste in Music ;) **__' + '\n```' + ''.join(genres[0:trial]) + '```' + '> this message is set for deletion in less than 30 minutes '
                mess = await chnl.send(gnr)
                messid = mess.id
                messch = mess.channel
                forDeletion.update({messid:messch})
        else:
            return
    except Exception as e :
        try:
            QUEUE.pop(K)
        except:
            pass   
        print(e)
        await chnl.send('token error')
