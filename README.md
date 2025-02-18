# **Stock Market Bot** <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Setup Guide](#setup-guide)
  - [Project setup](#project-setup)
  - [Adding bot to a server](#adding-bot-to-a-server)
  - [Running](#running)
- [Commands](#commands)
  - [Owner](#owner)
  - [League](#league)

## Setup Guide

> Created with Python 3.12.9

### Project setup
1. Clone this respository: `git clone https://github.com/A-Silkwood/Stock-Market-Bot.git`
2. Create a Discord application:
    1. Go to [Discord's developer page](https://discord.com/developers/applications).
    2. Click on `New Application`.
    3. Fill in a name and click `Create`.
    4. Go under `Settings > Bot`.
    5. Under `Priveleged Gateway Intents` make sure all intents are turned on.
3. Create a PostgreSQL server and database:
   > Currently using [PostgreSQL 17](https://www.postgresql.org/).
   - Under the `postgresql` folder, run `.sql` files in the following order in your database to setup the database properly.
      1. create_app_user.sql
         - Make sure to change the password in this file before running.
      2. create_tables.sql
      3. create_sps.sql
4. Create a `.env` file with the following variables in the root folder:
    - BOT_TOKEN - Obtain token from [Discord's developer page](https://discord.com/developers/applications). Navigate to your bot's application and it will be under `Settings > Bot > Token`.
    - SM_API_TOKEN - Obtain token from [Tiingo account page](https://www.tiingo.com/account/api/token).
    - DB_HOST - Database host
    - DB_PORT - Database port
    - DB_NAME - Database name
    - DB_USER - Database app user; Default is `app_user` if unchanged from `create_app_user.sql`
    - DB_PASSWORD - Database app user's password
5. Create a Python virtual environment and install the `requirements.txt`.

### Adding bot to a server
1. Go to bot application in [Discord's developer page](https://discord.com/developers/applications).
2. Go under `Settings > OAuth2`.
3. Under `OAuth2 URL Generator > Scopes` select `bot`.
4. Under `OAuth2 URL Generator > Bot Permissions` select `Administrator`.
5. Copy the generated URL and open it with your browser.
6. Follow the steps shown to add it to the server you want it to join.

### Running
1. Run `main.py` with the virtual environment.


## Commands

### Owner
> Only the bot owner can execute these commands
- **shutdown** - Shutdown bot.
- **load** `name` - Load specific module.
- **unload** `name` - Unload specific module.
- **reload** - Reload all modules.


### League
- **create** - 
- **delete** - 
- **overview** - 
- **setting** - 
- **invite** - 
- **join** - 
- **accept** - 
- **reject** - 
- **leave** - 
- **start** - 
- **end** - 
- **list** - 