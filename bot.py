# JustBot
# Version 1.0.0 -alpha- build 20
# Reconstructed to catch up with Python 3.8.3 and discord.py 1.4.0a
#
# Currently it has "low-level" commands.
# Soon, it will have "mid-level" and "high-level" commands. :)

import os
import sys
import random
import linecache
import asyncio
import aiohttp
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot("jb!")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

## Fact command
@bot.command(name='fact',
             description="Sends a random fact.\n"
             "Parameters:\n"
             "fun - Sends a random fun fact.\n"
             "inter - Sends an interesting fact.\n"
             "sci - Sends a scientific fact.\n"
             "w - Sends a weird fact.\n"
             "game - Sends a gaming fact.",
             brief="Gives you a fact.",
             pass_context=True)
async def randomFact(ctx, arg = None):
    param = '{}'.format(arg)
    factFiles = os.listdir('./facts_txts/')
    fnumLine = open("./facts_txts/fun_facts.txt","r").readlines()
    inumLine = open("./facts_txts/interesting_facts.txt","r").readlines()
    snumLine = open("./facts_txts/scientific_facts.txt","r").readlines()
    wnumLine = open("./facts_txts/weird_facts.txt","r").readlines()
    gnumLine = open("./facts_txts/gaming_facts.txt","r").readlines()
    random_numLine = ['fnumLine', 'inumLine', 'snumLine', 'wnumLine', 'gnumLine']
    if param == 'fun': # fun fact
        funLines = len(fnumLine)
        funline = random.randint(1,funLines)
        fact = linecache.getline('./facts_txts/fun_facts.txt',funline)
    elif param == 'inter': # interesting fact
        intLines = len(inumLine)
        intline = random.randint(1,intLines)
        fact = linecache.getline('./facts_txts/interesting_facts.txt',intline)
    elif param == 'sci': # scientific fact
        sciLines = len(snumLine)
        sciline = random.randint(1,sciLines)
        fact = linecache.getline('./facts_txts/scientific_facts.txt',sciline)
    elif param == 'w': # weird fact
        wLines = len(wnumLine)
        wline = random.randint(1,wLines)
        fact = linecache.getline('./facts_txts/weird_facts.txt',wline)
    elif param == 'game': # gaming fact
        gameLines = len(gnumLine)
        gameline = random.randint(1,gameLines)
        fact = linecache.getline('./facts_txts/gaming_facts.txt',gameline)
    else:
        factFile = random.choice(factFiles)
        fact_numLines = random.choice(random_numLine)
        rNum = len(fact_numLines)
        factline = random.randint(1,rNum)
        fact = linecache.getline('./facts_txts/' + factFile,factline)
    await ctx.send(">>> **Did You Know?**\n"
                   + fact)

## Math command
@bot.command(name='math',
             description="Solves any simple mathematical problem.\n"
             "Valid math operators:\n"
             "+ addition\n"
             "- subtraction\n"
             "* multiplication\n"
             "/ division\n"
             "// integer division/floored quotient\n"
             "% modulus/remainder\n"
             "** exponent\n"
             "Up to 2 numerical values only.",
             brief="Bot's simple calculator",
             aliases=['solve', 'answer'],
             pass_context=True)
async def math(ctx, num1, mathOp, num2):
    num1 = '{}'.format(num1)
    mathOp = '{}'.format(mathOp)
    num2 = '{}'.format(num2)
    validOp = {'+', '-', '*', '/', '//', '%', '**'}
    if mathOp in validOp:
        if mathOp == '+':
            mathAnswer = int(num1) + int(num2)
        if mathOp == '-':
            mathAnswer = int(num1) - int(num2)
        if mathOp == '*':
            mathAnswer = int(num1) * int(num2)
        if mathOp == '/':
            mathAnswer = int(num1) / int(num2)
        if mathOp == '//':
            mathAnswer = int(num1) // int(num2)
        if mathOp == '%':
            mathAnswer = int(num1) % int(num2)
        if mathOp == '**':
            mathAnswer = int(num1) ** int(num2)
    elif mathOp not in validOp:
        mathAnswer = 'ERROR: Invalid math operator.'
    await ctx.send('{} __**{}**__ {}'.format(num1, mathOp, num2) + ' = ' + str(mathAnswer))

## Random command
@bot.command(name='random',
             description="Gives you a random number, roll a die/dice, or maybe flip a coin.\n"
             "Parameters:\n"
             "no - number\n"
             "d <numDice> - dice (number of dices required if this is specified).\n"
             "c - coin",
             brief="Random number/roll dice/flip coin",
             aliases=['rand', 'ran'],
             pass_context=True)
async def rand(ctx, arg = None, numDice = None):
    option = '{}'.format(arg)
    numDice = '{}'.format(numDice)
    noDice = {'0', None}

    if option == 'no':
        randomReply = random.randint(0,9999)
    elif option == 'd':
        if int(numDice) >= 0 :
            randomReply = random.randint(int(numDice), int(numDice) * 6)
        elif int(numDice) < 0:
            randomReply = 'Invalid number of dices. How can I even roll a negative number of dice?'
        else:
            randomReply = 'There is no die/dice to roll with. ;-;'
    elif option == 'c':
        randomCoin = random.randint(1,2)
        if randomCoin == 1:
            randomCoinRes = 'Heads!'
        if randomCoin == 2:
            randomCoinRes = 'Tails!'
        randomReply = randomCoinRes
    else:
        randomReply = 'Hmmm... Seems that there is nothing to randomize with.'

    await ctx.send(randomReply)

## Quote command
@bot.command(name='quote',
             description="Sends a random quote.\n"
             "Parameters:\n"
             "ins - Sends an inspirational quote.\n"
             "meme/funny - Sends a meme/funny quote.\n"
             "fam - Sends a famous quote.\n"
             "game - Sends a gaming/gamer's quote.",
             brief="Gives you a quote.",
             pass_context=True)
async def quote(ctx, arg = None):
    param = '{}'.format(arg)
    quoteFiles = os.listdir('./quotes_txts/')
    e = {'meme', 'fun'}
    iqnumLine = open("./quotes_txts/inspirational_quotes.txt","r").readlines()
    mnumLine = open("./quotes_txts/funny_quotes.txt","r").readlines()
    fqnumLine = open("./quotes_txts/famous_quotes.txt","r").readlines()
    gqnumLine = open("./quotes_txts/game_quotes.txt","r").readlines()
    rand0m_numLine = ['iqnumLine', 'mnumLine', 'fqnumLine', 'gqnumLine']
    if param == 'ins': # inspirational quote
        insLines = len(iqnumLine)
        insline = random.randint(1,insLines)
        quote = linecache.getline('./quotes_txts/inspirational_quotes.txt',insline)
    elif param in e: # meme/funny quote
        mnumLines = len(mnumLine)
        funnyline = random.randint(1,mnumLines)
        quote = linecache.getline('./quotes_txts/funny_quotes.txt',funnyline)
    elif param == 'fam': # famous quote
        famNumLines = len(fqnumLine)
        famline =random.randint(1,famNumLines)
        quote = linecache.getline('./quotes_txts/famous_quotes.txt',famline)
    elif param == 'game': # gaming quote
        gameNumLines = len(gqnumLine)
        gameline = random.randint(1,gameNumLines)
        quote = linecache.getline('./quotes_txts/game_quotes.txt',gameline)
    else:
        quoteFile = random.choice(quoteFiles)
        QnumLines = random.choice(rand0m_numLine)
        qNum = len(QnumLines)
        quoteline = random.randint(1,qNum)
        quote = linecache.getline('./quotes_txts/' + quoteFile,quoteline)
    await ctx.send('> ' + quote)


@bot.event
async def on_resumed():
    print("Bot had resumed the session")

@bot.event
async def on_ready():
    print('Logged in as ')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')
    while not bot.is_closed:
     server_list = '\n'.join(bot.guilds)
     output = f'Current Servers: \n {server_list}'
     print(output)
     await asyncio.sleep(600)

@bot.event
async def on_error(event, *args, **kwargs):
    """
    Catches any exception that occurs during the bot's loop.
    If any exception is raised in ``on_error``, it will `not` be handled.

    The exception itself can be accessed from :class:`sys.exc_info`.

    Args:
        event:
            The name of the event that raised the exception.

        *args:
            The positional arguments for the event that raised the exception

        **kwargs:
             The keyword arguments for the event that raised the exception.

    """
    print("OH NO!, AN ERROR ;(")
    print("Error from:", event)
    print("Error context:", args, kwargs)

    from sys import exc_info

    exc_type, value, traceback = exc_info()
    print("Exception type:", exc_type)
    print("Exception value:", value)
    print("Exception traceback object:", traceback)

bot.run(TOKEN)
