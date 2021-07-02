from discord.ext import commands
import resources.conversions as conversions


class to_binary(commands.Cog):
    """
    This class contains commands that deal with conversion of values to binary.

    Commands:
        d!char_to_binary: convert all characters that follow from their ASCII values to their binary values
        d!hex_to_binary: convert all characters that follow from their hex values to their binary values
    """

    info = [{'inline': False, 'name': '!char_to_binary\t!ctb',
             'value': 'Convert all characters that follow from their ASCII values to their binary values.'},
            {'inline': False, 'name': '!hex_to_binary\t!htb',
             'value': 'Convert all the values that follow from their hex values to binary values.'}]

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog.
        """
        self.bot = bot

    @commands.command(aliases=['ctb'])
    async def char_to_binary(self, ctx, *, char_str):
        """
        Convert all characters that follow from their ASCII values to their binary values.

        Parameters:
            ctx (Context): The required context
            char_str (str): The string of characters to convert
        """
        try:
            binary_str = await conversions.conversions.character_to_binary(char_str)
            await ctx.send('Converted characters to binary:\n' + binary_str)
        except ValueError as e:
            await ctx.send('Error: ' + str(e))

    @commands.command(aliases=['htb'])
    async def hex_to_binary(self, ctx, *, hex_str):
        """
        Convert all the values that follow from their hex values to binary values.

        Parameters:
            ctx (Context): The required context
            hex_str (str): The string of hex to convert
        """
        try:
            binary_str = await conversions.conversions.hexadecimal_to_binary(hex_str)
            await ctx.send('Converted hex to binary:\n' + binary_str)
        except ValueError as e:
            await ctx.send('Error: ' + str(e))


def setup(bot):
    """
    Allow the bot to load this cog.
    """
    bot.add_cog(to_binary(bot))
