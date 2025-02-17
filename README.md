# **Stock Market Bot** <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Setup Guide](#setup-guide)
  - [Project setup](#project-setup)
  - [Adding bot to the server](#adding-bot-to-the-server)
  - [Running](#running)
- [Commands](#commands)
  - [Owner](#owner)
  - [Watcher](#watcher)

## Setup Guide

> Created with Python 3.12.9

### Project setup
1. Create a Discord application:
    1. Go to [Discord's developer page](https://discord.com/developers/applications).
    2. Click on `New Application`.
    3. Fill in a name and click `Create`.
    4. Go under `Settings > Bot`.
    5. Under `Priveleged Gateway Intents` make sure all intents are turned on.
2. Create a PostgreSQL server and database
    - Currently using [PostgreSQL 17](https://www.postgresql.org/).
    - Create an application user that can login into the database.
3. Create a `.env` file with the following variables in the root folder:
    - BOT_TOKEN - Obtain token from [Discord's developer page](https://discord.com/developers/applications). Navigate to your bot's application and it will be under `Settings > Bot > Token`.
    - CMD_PREFIX - Prefix used before all commands.
    - SM_API_TOKEN - Obtain token from [Tiingo account page](https://www.tiingo.com/account/api/token).
    - SM_API_URL - https://api.tiingo.com
    - DB_HOST - Database host
    - DB_PORT - Database port
    - DB_NAME - Database Name
    - DB_USER - Database app user
    - DB_PASSWORD - Database app user's password

4. Create a Python virtual environment and install the `requirements.txt`.
    - `pip install -r requirements.txt`

### Adding bot to the server
1. Go to bot application in [Discord's developer page](https://discord.com/developers/applications).
2. Go under `Settings > OAuth2`.
3. Under `OAuth2 URL Generator > Scopes` select `bot`.
4. Under `OAuth2 URL Generator > Bot Permissions` select `Administrator`.
5. Copy the generated URL and open it with your browser.
6. Follow the steps shown to add it to the server you want it to join.

### Running
1. Run `bot.py` in the virtual environment.


## Commands

### Owner
> Only bot owner can execute these commands
- **shutdown** - Shutdown bot.
- **load** `name` - Load specific module.
- **reload** - Reload all modules.


### Watcher