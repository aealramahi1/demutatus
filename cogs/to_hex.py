from discord.ext import commands
import resources.conversions as conversions


class to_hex(commands.Cog):
    """
    This class contains commands that deal with conversion of values to hex.

    Commands:
        d!char_to_hex: convert all characters that follow from their ASCII values to their hexadecimal values
        d!binary_to_hex: convert all characters that follow from their binary values to their hexadecimal values
    """

    info = [{'inline': False, 'name': '!binary_to_hex\t!bth',
             'value': 'Convert all characters that follow from their binary values to their hex values'},
            {'inline': False, 'name': '!char_to_hex\t!htc',
             'value': 'Convert all characters that follow from their ASCII values to their hex values'}]

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog.
        """
        self.bot = bot

    @commands.command(aliases=['bth'])
    async def binary_to_hex(self, ctx, *, binary_str):
        """
        Convert all characters that follow from their binary values to their hex values.

        Parameters:
            ctx (Context): The required context.
            binary_str (str): String representation of the binary to convert.
        """
        try:
            await ctx.send('Converted binary to hexadecimal:\n' + await conversions.conversions.binary_to_hexadecimal(binary_str))
        except ValueError as e:
            await ctx.send('Error: ' + str(e))

    @commands.command(aliases=['cth'])
    async def char_to_hex(self, ctx, *, char_str):
        """
        Convert all characters that follow from their character values to their hex values.

        Parameters:
            ctx (Context): The required context.
            char_str (str): String of characters to convert.
        """
        try:
            await ctx.send('Converted characters to hexadecimal:\n' + await conversions.conversions.character_to_hexadecimal(char_str))
        except ValueError as e:
            await ctx.send('Error: ' + str(e))



def setup(bot):
    """
    Allow the bot to load this cog.
    """
    bot.add_cog(to_hex(bot))
