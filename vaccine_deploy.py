import time
import requests
import json
import discord
import os
TOKEN = os.environ['Token']

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/vaccine'):
        msg = 'Enter district name'.format(message)
        await message.channel.send(msg)
        x = await client.wait_for('message')
        district_name = x.content
        with open("D:\Codes\JSON\district_id.json", "r") as f:
            districts_data = json.load(f)
        for districts in districts_data["districts"]:
            if district_name in districts["district_name"]:
                districts_id = districts["district_id"]
        date_m = time.strftime("%d-%m-%Y")
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(districts_id,date_m)
        respos = requests.get(url)
        data = respos.json()

        for sessions in data["sessions"]:
            await message.channel.send("Name:        ",sessions["name"])
            await message.channel.send("Address:     ",sessions["address"])
            await message.channel.send("Pin code:    ",sessions["pincode"])
            await message.channel.send("Fee Type:    ",sessions["fee_type"])
            await message.channel.send("Fee:         ",sessions["fee"])
            await message.channel.send("Vaccine:     ",sessions["vaccine"])
            await message.channel.send("Capacity:    ",sessions["available_capacity"])
            await message.channel.send("Slots:       ",sessions["slots"])
            await message.channel.send("\n")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)