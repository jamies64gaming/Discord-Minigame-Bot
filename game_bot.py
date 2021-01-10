#Import essentials
import discord
from discord.ext import commands
import random
import time
import sys
import os
from boto.s3.connection import S3Connection

global playing_roulette
global rnd
global tictacgame

tictacgame = False
playing_roulette = False
rnd = 0 

roulette_game = ""

help_line_1 ="""```

roulette          \tlets you play russian roulette against your 'friends'!
roll              \trolls a dice! exciting i know!
8ball             \ttells you the definitive answer to your question! 💯
tictac            \tlets you play a ruthless game of X's and O's!!!!
ping              \tpong!
clear             \tgets rid of any and all 'evidence' 😉!
help              \tshows you this page! wow...
gull              \tmakes you gullible to lies!

```"""

client = commands.Bot(command_prefix='!', help_command=None) #change it if you want


'''
-------------------------------------------------------------------------------
'''

@client.event
async def on_ready():
    print('Hello, I am now running ')
    print(client.user.name)
    print(client.user.id)
    print('------')

'''
-------------------------------------------------------------------------------
'''

@client.event
async def on_reaction_add(reaction, user):
    
    global tictacgame
    global tictacb                                              #tic tac toe script
    if tictacgame and user != client.user and reaction.message == tictacb and reaction.count <= 2:

        print("tic tac toe " + str(user))                   #logs game
        draw = False                                        #defines draw
        win = False                                         #defines win
        round_null = False
        global player
        player += 1                                         #changes player

        if reaction.emoji == "↖️":                          #checks where player selected to move, then places player on grid
            tictacboard.pop(0)                              #removes blank square from grid

            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(0 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(0 , "O")                 #places O in grid pos

        elif reaction.emoji == "⬆️" and tictacboard[1] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(1)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(1 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(1 , "O")                 #places O in grid pos

        elif reaction.emoji == "↗️" and tictacboard[2] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(2)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(2 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(2 , "O")                 #places O in grid pos

        elif reaction.emoji == "⬅️" and tictacboard[3] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(3)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(3 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(3 , "O")                 #places O in grid pos

        elif reaction.emoji == "⏺️" and tictacboard[4] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(4)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(4 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(4 , "O")                 #places O in grid pos

        elif reaction.emoji == "➡️" and tictacboard[5] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(5)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(5 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(5 , "O")                 #places O in grid pos

        elif reaction.emoji == "↙️" and tictacboard[6] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(6)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(6 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(6 , "O")                 #places O in grid pos

        elif reaction.emoji == "⬇️" and tictacboard[7] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(7)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(7 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(7 , "O")                 #places O in grid pos

        elif reaction.emoji == "↘️" and tictacboard[8] == "‏‏‎■":#checks where player selected to move, then places player on grid
            tictacboard.pop(8)                              #removes blank square from grid
            
            if player % 2 == 0:                             #checks if player is X
                tictacboard.insert(8 , "X")                 #places X in grid pos

            else:                                           #goes here is player is O
                tictacboard.insert(8 , "O")                 #places O in grid pos

        else:
            await tictacb.add_reaction("⛔")
            time.sleep(2)
            await tictacb.clear_reaction("⛔")
            round_null = True

        if round_null == False:                                                    #updates grid
            tictacGB = str(tictacboard[0])+str(tictacboard[1])+str(tictacboard[2])+"\n"+str(tictacboard[3])+str(tictacboard[4])+str(tictacboard[5])+"\n"+str(tictacboard[6])+str(tictacboard[7])+str(tictacboard[8])
            
            await tictacb.edit(content = tictacGB)              #displays grid
            
                                                                #checks all outcomes for if player won
            if tictacboard[0] == tictacboard[1] and tictacboard[0] == tictacboard[2] and str(tictacboard[0]) != "‏‏‎■":
                print(str(user) + " wins!! 1")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            if tictacboard[0] == tictacboard[3] and tictacboard[0] == tictacboard[6] and tictacboard[0] != "‏‏‎■":
                print(str(user) + " wins!! 2")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            if tictacboard[1] == tictacboard[4] and tictacboard[1] == tictacboard[7] and tictacboard[1] != "‏‏‎■":
                print(str(user) + " wins!! 3")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            if tictacboard[2] == tictacboard[5] and tictacboard[2] == tictacboard[8] and tictacboard[2] != "‏‏‎■":
                print(str(user) + " wins!! 4")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            if tictacboard[3] == tictacboard[4] and tictacboard[3] == tictacboard[5] and tictacboard[3] != "‏‏‎■":
                print(str(user) + " wins!! 5")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            if tictacboard[6] == tictacboard[7] and tictacboard[6] == tictacboard[8] and tictacboard[6] != "‏‏‎■":
                print(str(user) + " wins!! 6")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            if tictacboard[0] == tictacboard[4] and tictacboard[0] == tictacboard[8] and tictacboard[0] != "‏‏‎■":
                print(str(user) + " wins!! 7")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            if tictacboard[2] == tictacboard[4] and tictacboard[2] == tictacboard[6] and tictacboard[2] != "‏‏‎■":
                print(str(user) + " wins!! 8")                  #logs winner and win seed
                tictacgame = False                              #closes game
                win = True                                      #sets win to true

            gridN = 0
            for i in tictacboard:                               #checks if game is a draw
                if i == "‏‏‎■":
                    break                                       #goes true each grid number and checks if its been played
                gridN += 1
                if gridN == 9:
                    tictacgame = False                          #closes game
                    draw = True                                 #sets draw to True

            if tictacgame == False:                             #checks if game over
                await tictacb.clear_reactions()                 #clears reactions
                
                if draw == True and win != True:                #checks if its a draw
                    await tictacb.add_reaction("🏳️")            #add draw reaction
                
                else:                                           #if player wins it goes here
                    await tictacb.add_reaction("🎉")            #gives winning reactions
                    await tictacb.add_reaction("🏆")
                    await tictacb.add_reaction("🍾")
                    await reaction.message.channel.send(f"{user.mention} has won!")#winning message
                print("tic tac toe complete")

        else:
            pass

    global playing_roulette                                     #ROULETTE SCRIPT
    if reaction.emoji == '💀' and playing_roulette and user != client.user and reaction.message == roulette_game:
        print("roulette " + str(user))                          #logs game

        global rnd
        rnd += 1                                                #updates round

        if rnd == BadBullet:                                    #checks if the bullet is in the chamber when shot
            print(str(user) + " losses!")
            await roulette_game.add_reaction("💥")              #bullet shot reaction
            time.sleep(2)                                       #delay
            await roulette_game.clear_reactions()               #clear reaction
            await roulette_game.add_reaction("🎉")              #win reactions
            await roulette_game.add_reaction("🏆")
            await roulette_game.add_reaction("🍾")
            print("roulette complete")
            playing_roulette = False                            #closes game

        else:                                                   #if bullet not in chamber, this is ran
            await roulette_game.add_reaction("🍀")              #gun unloaded reaction
            time.sleep(2)                                       #delay
            await roulette_game.clear_reaction("🍀")            #remove unloaded reaction


        await roulette_game.remove_reaction("💀" , user)

'''
-------------------------------------------------------------------------------
'''

@client.command()
async def roulette(ctx):
    
    SendingUser = ctx.message.author

    await ctx.send("welcome to russian roulette! wait for the 💀 to be 1 before clicking!")

    global roulette_game

    roulette_game = await ctx.send(f"there is one bullet in the chamber! {SendingUser.mention} will go first! \njust react with the 💀 to shoot!")
    await roulette_game.add_reaction("\N{skull}")

    global playing_roulette
    global rnd
    global BadBullet

    playing_roulette = True
    rnd = 0
    BadBullet = random.randint(1, 6)

'''
-------------------------------------------------------------------------------
'''

@client.command()
async def clear(ctx , amount = 5):
    await ctx.channel.purge(limit = (amount + 1))

'''
-------------------------------------------------------------------------------
'''

@client.command(pass_context = True) #passing context
async def salute(ctx): #context gets passed into the first parameter
    print(str(ctx.message.author))
    print(str(ctx.message.channel))
    print(str(ctx.message.content))

'''
-------------------------------------------------------------------------------
'''

@client.command()
async def help(ctx , page = 1):

    SendingUser = ctx.message.author

    help_msg = await ctx.send(f"Hi {SendingUser.mention}! here is a list of commands that shows you what i can do!")
    help_msg = await ctx.send(f"just use '!' infront of any of these to get started!")
    
    if page == 1:
        await ctx.send(help_line_1)

'''
-------------------------------------------------------------------------------

'''
@client.command()
async def gull(ctx):
    SendingUser = ctx.message.author
    print(str(SendingUser) + " is gullible!")
    gull_msg = await ctx.send("__**⚠️⚠️⚠️ HEY " + "@everyone" + f"{SendingUser.mention} IS GULLIBLE‼️‼️‼️‼️‼️‼️🤣🤣🤣😂😂😂🤮🤪🤪😝😝😝 ⚠️⚠️⚠️**__")

'''
-------------------------------------------------------------------------------
'''

@client.command()
async def roll(ctx):
    dice = random.randint(1,6)
    
    await ctx.send("rolling...")
    time.sleep(1)
    await ctx.send(str(dice) + "!")

'''
-------------------------------------------------------------------------------
'''

@client.command()
async def ping(ctx):
    await ctx.send( f"Pong {round( client.latency * 1000 )} ms" )

'''
-------------------------------------------------------------------------------
'''

@client.command(aliases = ["8ball"])
async def _8ball( ctx, * ,question):

    responses = ["fuck no",
             "keep dreaming!",
             "over my dead body",
             "dunno bud",
             "not with that attitude",
             "keep yanking it and ya might",
             "ask kevin",
             "ask shane",
             "ask jamie",
             "ask sibh",
             "pray to god, you more lickely to get an answer from him",
             "fuuuuuucccckkkkkk yyyyeeeeaaaaaaaaa",
             "uhhh",
             "UWU",
             "fuck off and try later",
             "cant be bothered",
             "im a bot, how low can u go",
             "if it benifits jamie, then yes, otherwise shove that question up you ass",
             "wtf",
             "fack off",
             "*yawn*",
             "yes?",
             "let me check! \n❕8ball " + question +"\n...\nNo",
             "let me check! \n❕8ball " + question +"\n...\ny am i asking myself!?!?!\n...\nohh yea its a maybe!",
             "As I see it, yes.",
             "Ask again later.",
             "Better not tell you now.",
             "Cannot predict now.",
             "Concentrate and ask again.",
             "Don’t count on it.",
             "It is certain.",
             "It is decidedly so.",
             "Most likely.",
             "My reply is no.",
             "My sources say no.",
             "Outlook not so good.",
             "Reply hazy, try again.",
             "Signs point to yes.",
             "Very doubtful.",
             "Without a doubt.",
             "Yes.",
             "Yes – definitely.",
             "You may rely on it."]
    riggedQ = False

    if question == "did jamie rig you?" or question == "did jamie rig you" or question == "are you rigged" or question == "r u rigged" or question == "r u rigged?" or question == "are you rigged":
        riggedQ = True
        await ctx.send("nooo...\nmaybe...\nmost definitely...")

    elif riggedQ == False:
        await ctx.send(f"{random.choice(responses)}")

'''
-------------------------------------------------------------------------------
'''

@client.command()
async def tictac(ctx):
    SendingUser = ctx.message.author
    await ctx.send(f"welcome {SendingUser.mention} to tic tac toe NERDDDDS! \nto play just react to the board below where you wanna go!")
    
    global tictacboard
    tictacboard =  ["‎‎‎‏‏‎■","‏‏‎■","‏‏‎■",
                    "‏‏‎■","‏‏‎■","‏‏‎■",
                    "‏‏‎■","‏‏‎■","‏‏‎■"]


    global tictacb
    tictacb = await ctx.send(str(tictacboard[0])+str(tictacboard[1])+str(tictacboard[2])+"\n"+str(tictacboard[3])+str(tictacboard[4])+str(tictacboard[5])+"\n"+str(tictacboard[6])+str(tictacboard[7])+str(tictacboard[8]))

    await tictacb.add_reaction("↖️")
    await tictacb.add_reaction("⬆️")
    await tictacb.add_reaction("↗️")
    await tictacb.add_reaction("⬅️")
    await tictacb.add_reaction("⏺️")
    await tictacb.add_reaction("➡️")
    await tictacb.add_reaction("↙️")
    await tictacb.add_reaction("⬇️")
    await tictacb.add_reaction("↘️")

    global tictacgame
    global player
    player = 1
    tictacgame = True

client.run(os.environ.["token"])