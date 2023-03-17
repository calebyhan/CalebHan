import discord
from discord.ext import commands
import requests
import os
import keep_alive

api_key = os.environ['lol_api']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

def get_id(username):
  url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}"
  headers = {"X-Riot-Token": api_key}
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return [str(response.json()["puuid"]), str(response.json()["id"])]
  else:
    return None


def get_champ_name(id):
  for champ in requests.get("https://ddragon.leagueoflegends.com/cdn/13.4.1/data/en_US/champion.json").json()["data"].values():
    if int(champ["key"]) == id:
      return champ["id"]


def get_error_message(error_code):
  error_messages = {
    400: "Bad request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Data not found",
    405: "Method not allowed",
    415: "Unsupported media type",
    429: "Rate limit exceeded",
    500: "Internal server error",
    502: "Bad gateway",
    503: "Service unavailable",
    504: "Gateway timeout"
  }
  return error_messages.get(error_code, "Unknown error")


def get_champ_data(puuid, summoner_id):
  url = f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
  headers = {"X-Riot-Token": api_key}
  response = requests.get(url, headers=headers).json()
  stats = response
  url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&endIndex=10"
  headers = {"X-Riot-Token": api_key}
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    matches = response.json()
    champs = []
    more_stats = [0, 0, 0]
    count = 0
    for match in matches:
      if count == 10:
        break
      url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match}"
      headers = {"X-Riot-Token": api_key}
      response = requests.get(url, headers=headers).json()
      for person in response["info"]["participants"]:
        if person["puuid"] == puuid:
          champs.append(person["championName"])
          more_stats[0] += person["kills"]
          more_stats[1] += person["assists"]
          more_stats[2] += person["deaths"]
          count += 1
    return champs, stats, more_stats
  else:
    return None


def get_top_champs_data(summoner_id):
  url = f"https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"
  headers = {"X-Riot-Token": api_key}
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    champ_data = response.json()
    top_champs = []
    for i in range(min(3, len(champ_data))):
      top_champs.append({
        "id": champ_data[i]["championId"],
        "level": champ_data[i]["championLevel"],
        "points": champ_data[i]["championPoints"]
      })
    return top_champs
  else:
    return None


@bot.command()
async def stats(ctx, username):
  ids = get_id(username)
  if ids is None:
    error_message = get_error_message(puuid)
    await ctx.send(f"Error: {error_message}")
    return

  champ_data, summoner_data, kda = get_champ_data(ids[0], ids[1])
  if champ_data is None:
    await ctx.send("Error: Failed to get champion data")
    return
    
  embed = discord.Embed(title=f"{username}'s stats")
  embed.add_field(name="Last 10 champions played", value=", ".join([champ for champ in champ_data]))
  
  for summoner in summoner_data:
    if summoner["queueType"] == "RANKED_SOLO_5x5":
      wins = summoner["wins"]
      losses = summoner["losses"]
      kda = round((kda[0] + kda[1]) / kda[2], 2)
      rank = summoner["tier"] + " " + summoner["rank"]
      lp = summoner["leaguePoints"]
      embed.add_field(name="Rank", value=rank, inline=True)
      embed.add_field(name="LP", value=lp, inline=True)
      embed.add_field(name="Win/Loss", value=f"{wins}/{losses}", inline=True)
      embed.add_field(name="KDA", value=kda, inline=True)
      break
  
  await ctx.send(embed=embed)


@bot.command()
async def topchamps(ctx, username):
  ids = get_id(username)
  if ids is None:
    error_message = get_error_message(puuid)
    await ctx.send(f"Error: {error_message}")
    return
    
  top_champs_data = get_top_champs_data(ids[1])
  if top_champs_data is None:
    await ctx.send("Error: Failed to get top champion data")
    return
    
  embed = discord.Embed(title=f"{username}'s stats")
  
  for champ in top_champs_data:
    champ_id = champ["id"]
    champ_level = champ["level"]
    champ_points = champ["points"]
    champ_name = get_champ_name(champ_id)
    embed.add_field(name=champ_name, value=f"Level {champ_level}\nPoints: {champ_points}", inline=True)
    
  await ctx.send(embed=embed)

keep_alive.keep_alive()
bot.run(os.environ['discord'])
