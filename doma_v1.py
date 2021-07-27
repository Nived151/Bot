import os
import time
import requests
import json
import discord
from discord import channel
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
async def on_message(message):
    if message.content.startswith('/vaccine'):
        msg = 'Enter district name'.format(message)
        await message.channel.send(msg)
        x = await client.wait_for('message')
        district_name = x.content
        with open("district_id.json", "r") as f:
            districts_data = json.load(f)
        for districts in districts_data["districts"]:
            if district_name in districts["district_name"]:
                districts_id = districts["district_id"]
        date_m = time.strftime("%d-%m-%Y")
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(districts_id,date_m)
        respos = requests.get(url)
        data = respos.json()

        for sessions in data["sessions"]:
            if(sessions["available_capacity"]>0):
                await message.channel.send("Name:        {}".format(sessions["name"]))
                await message.channel.send("Address:     {}".format(sessions["address"]))
                await message.channel.send("Pin code:    {}".format(sessions["pincode"]))
                await message.channel.send("Fee Type:    {}".format(sessions["fee_type"]))
                await message.channel.send("Fee:         {}".format(sessions["fee"]))
                await message.channel.send("Vaccine:     {}".format(sessions["vaccine"]))
                await message.channel.send("Capacity:    {}".format(sessions["available_capacity"]))
                await message.channel.send("Slots:       {}".format(sessions["slots"]))
                await message.channel.send("-----------------------------------------------------------------------------------------------------------------------------")


@client.event
async def on_message(message):
    if message.content.startswith('/bump'):
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
