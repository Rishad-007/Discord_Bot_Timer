import discord
from discord.ext import commands
import asyncio
import re

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# To track timers per channel
timers = {}

# Helper to parse "5m30s" style input
def parse_time_input(time_str):
    match = re.fullmatch(r'(?:(\d+)m)?(?:(\d+)s)?', time_str)
    if not match:
        return None
    minutes = int(match.group(1)) if match.group(1) else 0
    seconds = int(match.group(2)) if match.group(2) else 0
    return minutes * 60 + seconds

# Timer Task
async def run_timer(ctx, total_seconds):
    channel_id = ctx.channel.id
    user = ctx.author.mention

    msg = await ctx.send(f"⏱️ {user} started a timer for {total_seconds//60}m {total_seconds%60}s.")
    await ctx.send(f"🔔 Timer started for {total_seconds//60}m {total_seconds%60}s.")

    timers[channel_id] = {
        "running": True,
        "paused": False,
        "remaining": total_seconds,
        "task": asyncio.current_task(),
        "message": msg,
        "user": user
    }

    elapsed = 0
    one_min_up = False
    one_min_left = False

    while timers[channel_id]["remaining"] > 0:
        if timers[channel_id]["paused"]:
            await asyncio.sleep(1)
            continue

        await asyncio.sleep(1)
        timers[channel_id]["remaining"] -= 1
        elapsed += 1

        # Alert at 1 min passed
        if elapsed == 60 and not one_min_up:
            await ctx.send(f"⚠️ {user} 1 minute has passed.")
            one_min_up = True

        # Alert at 1 min left
        if timers[channel_id]["remaining"] == 60 and not one_min_left:
            await ctx.send(f"⚠️ {user} Only 1 minute left!")
            one_min_left = True

        # Update every 10 seconds
        if timers[channel_id]["remaining"] % 10 == 0:
            mins, secs = divmod(timers[channel_id]["remaining"], 60)
            await msg.edit(content=f"⏳ Time remaining: {mins:02d}:{secs:02d}")

    # Timer over
    await msg.edit(content="⏰ Time's up!")
    await ctx.send(f"🚨 {user} Your timer is over!")
    timers.pop(channel_id)

# TIMER START COMMAND
@bot.command()
async def timer(ctx, *, time_input: str):
    total_seconds = parse_time_input(time_input)
    if total_seconds is None or total_seconds <= 0:
        await ctx.send("❌ Invalid format. Use like `!timer 5m30s`, `2m`, or `30s`.")
        return

    channel_id = ctx.channel.id

    if channel_id in timers:
        await ctx.send("⚠️ A timer is already running in this channel. Use `!stop` or `!pause`.")
        return

    await run_timer(ctx, total_seconds)

# PAUSE TIMER
@bot.command()
async def pause(ctx):
    channel_id = ctx.channel.id
    if channel_id in timers and timers[channel_id]["running"]:
        timers[channel_id]["paused"] = True
        await ctx.send("⏸️ Timer paused.")

# RESUME TIMER
@bot.command()
async def play(ctx):
    channel_id = ctx.channel.id
    if channel_id in timers and timers[channel_id]["running"]:
        timers[channel_id]["paused"] = False
        await ctx.send("▶️ Timer resumed.")

# STOP TIMER
@bot.command()
async def stop(ctx):
    channel_id = ctx.channel.id
    if channel_id in timers:
        timers[channel_id]["task"].cancel()
        await ctx.send("❌ Timer stopped.")
        timers.pop(channel_id)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Paste your bot token here


bot.run('Token')
