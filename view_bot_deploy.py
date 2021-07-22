import os
from posix import environ
import time
import discord
from selenium import webdriver

Options = webdriver.ChromeOptions()
Options.binary_location = os.environ['GOOGLE_CHROME_BIN']
Options.add_argument('--headless')
Options.add_argument('--disable-dev-sh-usage')
Options.add_argument('--no-sandbox')

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER_PATH'], chrome_options=Options)

TOKEN = os.environ['Token']



client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!view_bot'):
        msg = 'enter views needed'.format(message) #write
        await message.channel.send(msg)
        x = await client.wait_for('message')#read
        viewsx = x.content.lower()
        views = int(viewsx)

        msg2 = 'enter length of video'.format(message) #write
        await message.channel.send(msg2)
        y = await client.wait_for('message')#read
        timeru = y.content.lower()
        k=int(timeru)
        timer = k - 20;

        msg3 = 'enter url'.format(message)
        await message.channel.send(msg3)
        z = await client.wait_for('message')
        linku = z.content
        print(linku)

        msg5 = 'Runnning...'.format(message)
        await message.channel.send(msg5)

        driver = webdriver.Chrome()
        for i in range(views):
                driver.get(linku)
                time.sleep(timer)
                await message.channel.send(i)
                driver.refresh()
        driver.close()
        msg4 = 'Successfully Completed'.format(message) #write
        await message.channel.send(msg4)
        
@client.event
async def bump(ctx):
    while True:
        channel = client.get_channel(757888494126497812)
        await channel.send('!d bump')
        time.sleep(86400)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.run(TOKEN)
