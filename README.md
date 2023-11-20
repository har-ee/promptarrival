# promptarrival

Short & sweet Discord bot designed to remind users about events they mention in messages after a specified amount of time. Helpful for keeping friends accountable when they promise to return in a set time frame.

**Note:**
- This project was developed for fun in a short amount of time to learn discord.py. Expect some limitations in handling certain cases, as the primary focus was on the Discord bot itself, not the extraction logic.

## Setup instructions:

1. Ensure you have python3 and pip3 installed.
2. Install required dependencies: `pip3 install -r requirements.txt`
3. Head to the [Discord Developers](https://discord.com/developers/applications) site, create an application, and generate a token.
4. Create a `.env` file containing `DISCORD_TOKEN=YOUR_TOKEN_HERE` (replace `YOUR_TOKEN_HERE` with your Discord bot token).
5. Generate an invite link for your server with the `bot` scope and the `Send Messages` permission.
