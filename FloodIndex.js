// use visual studio code and install discord.js. open Command Prompt and type npm install discord.js on windows

// You MUST read this before you use this flooder at your own risk. 
// This flooder is made for fun so if you upload this on top.gg or other websites, YOU WILL PAY FOR IT!!!

// this bot is already on top.gg so copyrights will be harsfully taken

// use this bot to prank your friends or GET REVENGE ON YOUR FRIENDS SERVER IF U MAKE THIS

// very good for famous youtubers. please youtubers give credit to me on discord if you pranked or did something with this bot

// dani's biggest fan of all times



// hippity hopitty my code is not ur property

//---------------------Dont change any code or else it will go boom---------------------------


const discord = require('discord.js')
const client = new discord.Client()

client.on('message' message => setInterval(function(){ message.channel.send("get spammed")}, 800))

client.on('ready', () {
  client.user.setActivity({ type: "STREAMING", url="http://www.twitch.tv/dheeran2010" })
  console.log('Ready to flood servers!')
})
// This code is the status code. It's gonna look like the bot is streaming when you run the whole code. DONT CHANGE ANYTING OR ELSE IT MAY NOT WORK ANY MORE


client.login('Your bot token')
