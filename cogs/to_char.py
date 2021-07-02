from discord.ext import commands
import resources.conversions as conversions


class to_char(commands.Cog):
    """
    This class contains commands that deal with conversion of values to characters.

    Commands:
        d!binary_to_char: convert all characters that follow from their binary values to their ASCII values
        d!hex_to_char: convert all characters that follow from their hexadecimal values to their ASCII values
    """

    info = [{'inline': False, 'name': '!binary_to_char\t!btc',
             'value': 'Convert all characters that follow from their binary values to their character values'},
            {'inline': False, 'name': '!hex_to_char\t!htc',
             'value': 'Convert all characters that follow from their hex values to their character values'}]

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog.
        """
        self.bot = bot

    @commands.command(aliases=['btc'])
    async def binary_to_char(self, ctx, *, binary_str):
        """
        Convert all characters that follow from their binary values to their character values.

        Parameters:
            ctx (Context): The required context.
            binary_str (str): String representation of the binary to convert.
        """
        try:
            await ctx.send('Converted binary to characters:\n' + await conversions.conversions.binary_to_character(binary_str))
        except ValueError as e:
            await ctx.send('Error: ' + str(e))

    @commands.command(aliases=['htc'])
    async def hex_to_char(self, ctx, *, hex_str):
        """
        Convert all characters that follow from their hexadecimal values to their character values.

        Parameters:
            ctx (Context): The required context.
            hex_str (str): String representation of the hexadecimal to convert.
        """
        try:
            await ctx.send('Converted hexadecimal to characters:\n' + await conversions.conversions.hexadecimal_to_character(hex_str))
        except ValueError as e:
            await ctx.send('Error: ' + str(e))


def setup(bot):
    """
    Allow the bot to load this cog.
    """
    bot.add_cog(to_char(bot))
