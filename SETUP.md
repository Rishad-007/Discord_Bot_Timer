# Discord Timer Bot - Setup Guide

A Discord bot that allows users to set timers in channels with pause/resume functionality.

## Prerequisites

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python)
- A Discord Bot Token

## Installation Steps

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd "Timer Bot"
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

**Activate the virtual environment:**

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install discord.py python-dotenv
```

### 4. Set Up Your Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section and click "Add Bot"
4. Copy your bot token
5. Create a `.env` file in the project directory:

```
DISCORD_TOKEN=your_bot_token_here
```

**⚠️ Important:** Replace `your_bot_token_here` with your actual bot token. Never share this token!

### 5. Add Bot to Your Discord Server

1. Go to the OAuth2 > URL Generator section
2. Select scopes: `bot`
3. Select permissions: `Send Messages`, `Read Messages/View Channels`, `Embed Links`
4. Copy the generated URL and open it in your browser
5. Select your server and authorize

## Running the Bot

**Activate virtual environment first (if created):**

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**Start the bot:**

```bash
python discordTimer.py
```

You should see:

```
Logged in as YourBotName#1234
```

## Bot Commands

| Command  | Usage                     | Example                                       |
| -------- | ------------------------- | --------------------------------------------- |
| `!timer` | Start a timer             | `!timer 5m30s` or `!timer 2m` or `!timer 30s` |
| `!pause` | Pause the running timer   | `!pause`                                      |
| `!play`  | Resume the paused timer   | `!play`                                       |
| `!stop`  | Cancel and stop the timer | `!stop`                                       |

## Time Format

- `m` = minutes
- `s` = seconds

**Examples:**

- `!timer 5m` → 5 minute timer
- `!timer 30s` → 30 second timer
- `!timer 2m45s` → 2 minutes 45 seconds timer

## Features

- ⏱️ Countdown timer with visual updates
- ⏸️ Pause and resume functionality
- ⚠️ Alerts at 1 minute passed and 1 minute remaining
- 📊 Real-time timer display
- 🚨 Completion notification

## Troubleshooting

### "ModuleNotFoundError: No module named 'discord'"

```bash
pip install discord.py
```

### "ModuleNotFoundError: No module named 'dotenv'"

```bash
pip install python-dotenv
```

### "DISCORD_TOKEN not found in .env file"

- Check that `.env` file exists in the project directory
- Verify the file contains: `DISCORD_TOKEN=your_token_here`
- Ensure there are no extra spaces around the `=` sign

### Bot won't respond to commands

- Make sure the bot has permissions to send messages in the channel
- Check that the bot has been added to your server
- Verify the command prefix is `!`

## Security Notes

🔒 **Never share your bot token!**

- Store the token in the `.env` file
- Add `.env` to your `.gitignore` file
- Use environment variables for sensitive data

## Support

For issues with discord.py, visit the [discord.py documentation](https://discordpy.readthedocs.io/)
