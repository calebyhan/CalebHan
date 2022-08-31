const {Discord, Client, GatewayIntentBits} = require('discord.js');
const { ActionRowBuilder, ButtonBuilder, ButtonStyle } = require('discord.js');
const keepAlive = require('./server');
const bot = new Client({intents: 259});
const token = process.env['discord']

bot.once('ready', () => {
	console.log('Ready!');
});

keepAlive();
bot.login(token)

bot.on('interactionCreate', async interaction => {
	if (!interaction.isChatInputCommand()) return;
  
	const { commandName } = interaction;
  const member = interaction.options.getUser('user');
  const song = interaction.options.getString('song');
  
	if (commandName === 'lyrics') {
    reply = ""
    notplaying = false
    try {
      if (member == null) {
        id = interaction.guild.members.cache.get(interaction.member.id)
      } else {
        id = interaction.guild.members.cache.get(member.id)
      }
    } catch {
      await interaction.reply({ content: "DM slash commands do not work, please invite me through [this link](https://discord.com/oauth2/authorize?client_id=1013516714245378079&permissions=&scope=bot).", ephemeral: true});
      return
    }
    for (activity in id.presence.activities) {
      activity = id.presence.activities[activity]
      if (activity.name == "Spotify") {
            arg1 = activity.details
            arg2 = activity.state
        notplaying = true
      }
    }
    const lyricsFinder = require("@jeve/lyrics-finder");
    if (!(song == null)) {
      console.log("hi")
      lyricsFinder.LyricsFinder(song).then((data) => {
      reply = data
    });
    } else {
      if (!(notplaying)) {
      await interaction.reply({ content: "User is not playing a song", ephemeral: true});
      return
      }
    lyricsFinder.LyricsFinder(arg1 + arg2).then((data) => {
      reply = data
    });
  }
    await new Promise(resolve => setTimeout(resolve, 1000));
    try {
      await interaction.reply({ content: reply, ephemeral: true}); 
    } catch {
      await interaction.reply({ content: "Lyrics are over 2000 characters", ephemeral: true}); 
    }
  }
});
