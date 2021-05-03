from discord.ext import commands


class to_char(commands.Cog):
    """
    This class contains commands that deal with conversion of text to characters (e.g. from binary or hex)

    Commands:
        !binary_to_char: convert all characters that follow from their binary values to their ASCII values
        !hex_to_char: convert all characters that follow from their hexadecimal values to their ASCII values
    """

    info = [{'inline': False, 'name': '!binary_to_char\t!btc',
             'value': 'Convert all characters that follow from their binary values to their ASCII values (and prints '
                      'them as chars)'}]

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog.
        """
        self.bot = bot

    @commands.command(aliases=['btc'])
    async def binary_to_char(self, ctx, *, binary_str):
        """
        Convert all characters that follow from their binary values to their ASCII values (and prints them as chars).

        Parameters:
            ctx (Context): The required context.
            binary_str (str): String representation of the binary to convert.
        """
        try:
            await ctx.send('Converted binary to characters:\n' + await to_char.binary_to_character(binary_str))
        except ValueError as e:
            await ctx.send('Error: ' + str(e))

    @staticmethod
    async def validate_binary(binary_list):
        """
        Validates a list of binary numbers to make sure each element in the list is a group of eight valid binary
        numbers.

        Parameters:
            binary_list (list): A list of binary numbers, each grouping of size eight
        Returns:
            is_valid
        """
        for binary_num in binary_list:

            # Check if each one is a group of eight
            if len(binary_num) != 8:
                return False

            # Check if each digit is either a one or a zero
            for num in binary_num:
                if int(num) != 1 and int(num) != 0:
                    return False
        return True

    @staticmethod
    async def binary_to_character(binary_str):
        """
        Convert all characters that follow from their binary values to their ASCII values.

        Parameters:
            binary_str (str): String representation of the binary to convert.
        Returns:
            char_str (str): The resulting string after converting the binary.
        Raises:
            ValueError: If the binary is invalid.
        """
        char_str = ''
        binary_list = binary_str.split(' ')

        # Make sure the binary is valid before converting
        if not to_char.validate_binary(binary_list):
            raise ValueError('Please enter binary in groups of eight digits. Digits may only be ones and zeros.')

        # Convert each group of eight binary to a character
        for group_eight in binary_list:
            letter_value = 0

            # Calculate the value of this group of eight
            for num in range(7, -1, -1):
                letter_value += int(group_eight[len(group_eight) - num - 1]) * 2 ** num

            # Find the character with ASCII value letter_value
            char_str += chr(letter_value)

        return char_str


def setup(bot):
    """
    Allow the bot to load this cog.
    """
    bot.add_cog(to_char(bot))
