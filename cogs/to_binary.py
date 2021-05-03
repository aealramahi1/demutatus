from discord.ext import commands
to_hex_cog = None


class to_binary(commands.Cog):
    """
    This class contains commands that deal with conversion of text between ASCII values and binary

    Commands:
        !char_to_binary: convert all characters that follow from their ASCII values to their binary values
        !hex_to_binary: convert all characters that follow from their hex values to their binary values
    """

    info = [{'inline': False, 'name': '!char_to_binary\t!ctb',
             'value': 'Convert all characters that follow from their ASCII values to their binary values.'}]

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog.
        """
        self.bot = bot

        global to_hex_cog
        to_hex_cog = self.bot.get_cog('to_hex')

    @commands.command(aliases=['ctb'])
    async def char_to_binary(self, ctx, *, char_str):
        """
        Convert all characters that follow from their ASCII values to their binary values.

        Parameters:
            ctx (Context): The required context
            char_str (str): The string of characters to convert
        """
        try:
            binary_str = await to_binary.character_to_binary(char_str)
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
            binary_str = await to_binary.hexadecimal_to_binary(hex_str)
            await ctx.send('Converted hex to binary:\n' + binary_str)
        except ValueError as e:
            await ctx.send('Error: ' + str(e))

    @staticmethod
    async def character_to_binary(char_str):
        """
        Converts characters to binary based on their ASCII values.

        Parameters:
            char_str (str): The string of characters to convert.
        Returns:
            binary_str (str): String representation of the corresponding binary
        Raises:
            ValueError: Raised if char_str contains special characters (i.e., the ASCII values are not between 0 and 255)
        """
        binary_str = ''

        # Convert each character
        for char in char_str:

            # Convert the char to its integer value
            char = ord(char)

            # Avoid dealing with emojis or other special characters
            if char > 255:
                raise ValueError('Please omit special characters like emojis.')

            # Create the 8 binary digits for the character...floor divide by 2^7, then 2^6, then 2^5 etc.
            for num in range(7, -1, -1):
                binary_str += str(char // 2 ** num)
                char %= 2 ** num

            # Add a space for readability (to separate the groups of eight)
            binary_str += ' '
        return binary_str

    @staticmethod
    async def hexadecimal_to_binary(hex_str):
        """
        Converts a hexadecimal number of any size to binary.

        Parameters:
            hex_str (str): The hexadecimal number to convert.
        Returns:
            binary_str (str): String representation of the corresponding binary.
        Raises:
            ValueError: Raised if hex_str is not a valid hexadecimal number.
        """
        binary_str = ''

        # We don't care for whitespace or character case
        hex_str = ''.join(hex_str.upper().split())

        # Convert the hex to binary one hex number at a time. Each hexadecimal number will output 4 binary digits.
        for hex_num in hex_str:

            # Check if it's a letter
            if hex_num.isalpha():

                # Make sure it's between A and F
                if hex_num not in to_hex_cog.valid_hex_letters:
                    raise ValueError('Please input valid hex (0-9 and A-F)')

                # A = 65 so we subtract 55 from this ASCII value to get the numeric value of this hex letter
                hex_num = ord(hex_num) - 55

            # Otherwise, check if it's numeric
            elif hex_num.isnumeric():

                # 0 = 48 so we subtract 48 from the ASCII value to get the numeric value of this hex number
                hex_num = ord(hex_num) - 48

                # Make sure that it's between 0 and 9
                if hex_num < 0 or hex_num > 9:
                    raise ValueError('Please input valid hex (0-9 and A-F)')

            else:
                raise ValueError('Please input valid hex (0-9 and A-F)')

            # Generate the four binary digits for this hex letter
            for num in range(3, -1, -1):
                binary_str += str(hex_num // 2 ** num)
                hex_num %= 2 ** num
            binary_str += " "

        return binary_str


def setup(bot):
    """
    Allow the bot to load this cog.
    """
    bot.add_cog(to_binary(bot))
