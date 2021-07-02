class conversions:
    valid_hex = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

    def __init__(self, bot):
        """
        Initializer function that allows us to access the bot within this cog.
        """
        self.bot = bot

    @staticmethod
    async def validate_binary(binary_list):
        """
        Validate a list of binary numbers to make sure each element in the list is a group of eight valid binary
        numbers.

        Parameters:
            binary_list (list): A list of binary numbers, each grouping of size eight
        Returns:
            is_valid (boolean): True if binary_list is valid, false otherwise
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
    async def character_to_binary(char_str):
        """
        Convert characters to binary based on their ASCII values.

        Parameters:
            char_str (str): The string of characters to convert.
        Returns:
            binary_str (str): String representation of the corresponding binary
        Raises:
            ValueError: Raised if char_str contains special characters (i.e., the ASCII values are not between 0 and
            255)
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
        Convert a hexadecimal number of any size to binary.

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
                if hex_num not in conversions.valid_hex:
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
        if not await conversions.validate_binary(binary_list):
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

    @staticmethod
    async def hexadecimal_to_character(hex_str):
        char_str = ''
        hex_nums = []

        # We don't care for whitespace or character case
        hex_str = ''.join(hex_str.upper().split())

        # Make sure we have enough hex (groups of two)
        if len(hex_str) % 2 != 0:
            raise ValueError('Please enter hexadecimal in groups of two digits. Digits may only be numeric or A-F')

        # Split into groups of two
        for i in range(0, len(hex_str) - 1, 2):
            hex_nums.append(hex_str[i: i + 2])

        # Convert each group of two to a character
        for hex_pair in hex_nums:
            if hex_pair[0] not in conversions.valid_hex or hex_pair[1] not in conversions.valid_hex:
                raise ValueError('Please input valid hex (0-9 and A-F)')

            value1 = ord(hex_pair[0]) - 48 if hex_pair[0].isnumeric() else ord(hex_pair[0]) - 55
            value2 = ord(hex_pair[1]) - 48 if hex_pair[1].isnumeric() else ord(hex_pair[1]) - 55
            char_str += chr(value1 * 16 + value2)

        return char_str

    @staticmethod
    async def binary_to_hexadecimal(binary_str):
        """
        Convert all characters that follow from their binary values to their hexadecimal values.

        Parameters:
            binary_str (str): String representation of the binary to convert.
        Returns:
            hex_str (str): The resulting hex string after converting the binary.
        Raises:
            ValueError: If the binary is invalid.
        """
        hex_str = ''
        binary_list = binary_str.split(' ')

        # Make sure the binary is valid before converting
        if not await conversions.validate_binary(binary_list):
            raise ValueError('Please enter binary in groups of eight digits. Digits may only be ones and zeros.')

        # Convert each group of eight binary to two hex digits
        for group_eight in binary_list:
            hex_value = 0

            # Calculate the value of the first group of four, then the second
            for num in range(0, 4):
                hex_value += int(group_eight[3 - num]) * 2 ** num
            hex_str += conversions.valid_hex[hex_value]
            hex_value = 0

            for num in range(4, 8):
                hex_value += int(group_eight[3 - num]) * 2 ** num
            hex_str += conversions.valid_hex[hex_value]

        return hex_str

    @staticmethod
    async def character_to_hexadecimal(char_str):
        """
        Convert all characters that follow from their ASCII values to their hexadecimal values.

        Parameters:
            char_str (str): Character string to convert.
        Returns:
            hex_str (str): The resulting hex string after converting the characters.
        Raises:
            ValueError: If there are special characters.
        """
        hex_str = ''

        # Convert each character
        for char in char_str:

            # Convert the char to its integer value
            char = ord(char)

            # Avoid dealing with emojis or other special characters
            if char > 255:
                raise ValueError('Please omit special characters like emojis.')

            # Get the indices for the two hex digits for this character (corresponding to valid_hex)
            i = int(char / 16)
            j = int(char % 16)

            hex_str += conversions.valid_hex[i] + conversions.valid_hex[j]

            # Add a space for readability (to separate the groups of two)
            hex_str += ' '

        return hex_str
