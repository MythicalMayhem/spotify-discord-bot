import base64
import discord
import os 

client = discord.Client()

clientid = os.environ['clientid']
clientsecret = os.environ['clientsecret']

cli = clientid + ':' + clientsecret
cli = base64.b64encode(cli.encode('ascii'))
cli = cli.decode('utf-8')

authlink = os.environ['authlink']

botTOKEN = os.environ['botTOKEN']
disTOKEN = os.environ['disTOKEN']

whurl = os.environ['whurl']

topTracks = os.environ['topTracks']
topArtists = os.environ['topArtists']

trial = 25
QUEUE = {}
forDeletion = {}