import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def timer(ctx, minutes: int):
    user = ctx.author.mention
    total_seconds = minutes * 60
    time_left = total_seconds

    # Send initial message
    msg = await ctx.send(f"⏱️ {user} started a {minutes} minute timer!")

    # Alerts
    await ctx.send(f"🔔 Timer started for {minutes} minutes!")

    # Flags for 1-minute alerts
    one_min_up = False
    one_min_left = False

    while time_left > 0:
        mins, secs = divmod(time_left, 60)
        await msg.edit(content=f"⏳ Time remaining: {mins:02d}:{secs:02d}")
        await asyncio.sleep(1)
        time_left -= 1

        if total_seconds - time_left == 60 and not one_min_up:
            await ctx.send(f"⚠️ {user} 1 minute has passed.")
            one_min_up = True

        if time_left == 60 and not one_min_left:
            await ctx.send(f"⚠️ {user} Only 1 minute left!")
            one_min_left = True

    await msg.edit(content="⏰ Time's up!")
    await ctx.send(f"🚨 {user} Your timer is over!")

bot.run('token')
