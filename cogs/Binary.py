from discord.ext import commands


class Binary(commands.Cog):
    """
    This class contains commands that deal with conversion of text between
    ASCII values and binary

    Commands:
        !char_to_binary: converts all characters that follow from their ASCII
                         values to their binary values
        !char_from_binary: converts all characters that follow from their
                           binary values to their ASCII values (and prints them
                           as chars)
    """

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog
        """
        self.bot = bot

    @commands.command(aliases=["ctb"])
    async def char_to_binary(self, ctx, *, char_str):
        """
        Converts all characters that follow from their ASCII values to their
        binary values

        Parameters:
            ctx (Context): The required context
            char_str (String): The string of characters to convert
        """
        # TODO: IMPLEMENT

    @commands.command(aliases=["cfb"])
    async def char_from_binary(self, ctx, *, binary_str):
        """
        Converts all characters that follow from their binary values to their
        ASCII values (and prints them as chars)

        Parameters:
            ctx (Context): The required context
            binary_str (String): String representation of the binary to convert
        """
        # TODO: IMPLEMENT

        # chr(int)
        # ord(char)


def setup(bot):
    """
    Allows the bot to load this cog
    """
    bot.add_cog(Binary(bot))
