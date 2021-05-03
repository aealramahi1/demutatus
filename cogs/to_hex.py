from discord.ext import commands
# valid_hex_letters = ('A', 'B', 'C', 'D', 'E', 'F')

class to_hex(commands.Cog):
    """
    This class contains commands that deal with conversion of text to hex.

    Commands:
        !char_to_hex: convert all characters that follow from their ASCII
                      values to their hexadecimal values
        !binary_to_hex: convert all characters that follow from their
                        binary values to their hexadecimal values
    """

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog.
        """
        self.bot = bot
        self.valid_hex_letters = ('A', 'B', 'C', 'D', 'E', 'F')


def setup(bot):
    """
    Allow the bot to load this cog.
    """
    bot.add_cog(to_hex(bot))
