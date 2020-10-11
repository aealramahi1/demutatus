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
        binary_str = ""

        # Convert each character
        for char in char_str:
            # Convert the char to its integer value
            char = ord(char)

            # Avoid dealing with emojis or other special characters
            if char > 255:
                await ctx.send("Invalid text. Please omit special characters" +
                               " like emojis.")
                return

            # Create the 8 binary digits for the character
            for num in range(7, -1, -1):
                binary_digit = char // 2 ** num
                binary_str += str(binary_digit)
                char %= 2 ** num
            binary_str += " "
        await ctx.send("Here's what you said in binary:\n" + binary_str)

    @commands.command(aliases=["cfb"])
    async def char_from_binary(self, ctx, *, binary_str):
        """
        Converts all characters that follow from their binary values to their
        ASCII values (and prints them as chars)

        Parameters:
            ctx (Context): The required context
            binary_str (String): String representation of the binary to convert
        """
        char_str = ""

        # Make sure the input is valid (multiples of 8 binary numbers)
        if binary_str % 8 != 0:
            await ctx.send("Please make sure that you give me binary digits" +
                           " in multiples of 8 so I can convert it properly!")
            return

        # Make sure the input is valid (only ones and zeroes)
        for binary_num in binary_str:
            if binary_num != 1 or binary_num != 0:
                await ctx.send("Please only input ones and zeroes.")
                return

        # Convert each multiple of 8

        # chr(int)
        # ord(char)


def setup(bot):
    """
    Allows the bot to load this cog
    """
    bot.add_cog(Binary(bot))
