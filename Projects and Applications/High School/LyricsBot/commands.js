const { SlashCommandBuilder, Routes } = require('discord.js');
const { REST } = require('@discordjs/rest');
const token = process.env['discord']

const commands = [
	new SlashCommandBuilder().setName('lyrics').setDescription('Search lyrics!').addUserOption(option =>
		option.setName('user')
			.setDescription('The user to search')
			.setRequired(false)).addStringOption(option =>
		option.setName('song')
			.setDescription('The song to search')
			.setRequired(false))
]
	.map(command => command.toJSON());


const rest = new REST({ version: '10' }).setToken(token);

const application_id = "your application id here"

(async () => {
	try {
		await rest.put(
    	Routes.applicationCommands(application_id),
    	{ body: commands },
    );
	} catch (error) {
		console.error(error);
	}
})();
