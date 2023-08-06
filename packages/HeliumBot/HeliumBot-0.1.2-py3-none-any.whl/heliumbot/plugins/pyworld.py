from log4py import create_logger

from heliumbot.bot.commands import CommandManager

class Plugin:
  def __init__(self, bot):
    self.logger = create_logger('pyworld')
    self.bot    = bot
    self.cmdmgr = CommandManager(bot, self)

    async def cmd_pyworld_handler(ctx): 
      await self.bot.client.send_message(ctx.msg.channel, 'Py, World!')

    self.cmd_pyworld = self.cmdmgr.add_command('pyworld')
    b = self.cmd_pyworld.add_branch('root')
    b.set_handler(cmd_pyworld_handler)
    b.describe('Says py')