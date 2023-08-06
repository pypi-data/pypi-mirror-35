# HeliumBot

WARNING: this bot is developed mostly for self-hosting purposes and is not designed to be used on large amonths of servers.

## Dependencies 

All dependencies can be installed from requirements.txt or automatically if you're getting this bot from pypi.

## Starting

First, create two files (other two are already provided): token.txt and admin.txt.

Insert your bot's token into the first one and your id into the second one.

Start redis using provided redis config (feel free to edit it for your needs,
but you need to change redis.txt if you change port or host redis on another server).

Now you can start the bot with the next command:

```bash
$ hy -m heliumbot.cmd.launch token.txt admin.txt redis.txt
```

## Configuring permissions/groups

When bot is started, i'd send next messages to it to allow users checking help and permissions:

```
!group-give global heliumbot.plugins.core/help
!group-give global heliumbot.plugins.core/perms-read
```

## Prefix

You can also set bot's prefix in the current guild (doing so in PM will raise an exception):

```
!prefix aPrefix!
```