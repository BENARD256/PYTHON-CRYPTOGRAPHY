"""
The Code Emulates the Des Key Scheduling Algorithm used to generate Round Keys
Input 64 Bits
Round key = 48 Bits

"""

# Class returns round keys as a list


class Keyschedule:

    def __init__(self, key):
        self.__key = key
        self.__oneshift = (1, 2, 9, 16)

        self.__left_block = None
        self.__right_block = None
        self.__key_bits = self.__paritydrop()
        self.__keys = []
        # print("Initial Values:", self.__key_bits)

    def __to_binary(self):
        message = self.__key
        message.encode("utf-8")

        # Alphabet to Digits Conversion
        numeric_rep = [ord(char) for char in message]

        binary_rep = "".join(format(char, "08b") for char in numeric_rep)

        return binary_rep

    def __padding(self, length=64):
        key_bit = self.__to_binary()
        column_info = []

        if len(key_bit) != length:
            pad = (length - len(key_bit))

            final_length = pad + len(key_bit)

            key_bit = key_bit.rjust(final_length, "0")

        column_info.append(key_bit)

        return "".join(column_info)

    def __paritydrop(self):
        __key_bits = self.__padding()

        __permutation_table = (
            57, 49, 41, 33, 25, 17, 9, 1,
            58, 50, 42, 34, 26, 18, 10, 2,
            59, 51, 43, 35, 27, 19, 11, 3,
            60, 52, 44, 36, 63, 55, 47, 39,
            31, 23, 15, 7, 62, 54, 46, 38,
            30, 22, 14, 6, 61, 53, 45, 37,
            29, 21, 13, 5, 28, 20, 12, 4
        )

        transposed_bits = [__key_bits[index - 1] for index in __permutation_table]  # Permutation_table values -1

        return "".join(transposed_bits)

    def __splitter(self, message, leng=28):
        # Slicing the Bits
        start = 0
        end = leng  # Since each Block 32 ie Left, Right

        final_bits = []

        for _ in message:
            slice = message[start:end]

            length = len(slice)

            if length < leng:
                continue

            final_bits.append(slice)
            start += leng
            end += leng

        self.__left_block = final_bits[0]
        self.__right_block = final_bits[-1]

        return final_bits

    @staticmethod
    def __leftshift(bits, shift_no=1):
        final = ""
        shift = range(shift_no)

        rest = bits[shift_no:len(bits)]

        for index in shift:
            final += bits[index]

        final = rest + final

        return final

    @staticmethod
    def __compression(plain_bits):  # 56 ==> 48
        __permutation_table = (
            14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32
        )

        transposed_bits = [plain_bits[index - 1] for index in __permutation_table]  # Permutation_table values -1
        return "".join(transposed_bits)

    def _generate(self, shifts=1):  # This will Store shifted Bits after @round

        # Splitting into left, Right Blocks

        __splitted_bits = self.__splitter(message=self.__key_bits, leng=28)  # List of 2 items

        self.__left_block = __splitted_bits[0]
        self.__right_block = __splitted_bits[-1]

        # Left Shifting Both Blocks Basing on Rounds
        self.__left_block = self.__leftshift(bits=self.__left_block, shift_no=shifts)
        self.__right_block = self.__leftshift(bits=self.__right_block, shift_no=shifts)

        # Combining the 2 Blocks After Shifting
        single_block = str(self.__left_block + self.__right_block)

        # Storing Copy of The Shifted bits in Global Var key_bits for other rounds
        self.__key_bits = single_block

        # Round Key Compression
        __round_key = self.__compression(plain_bits=single_block)

        # Append round keys to List
        self.__keys.append(__round_key)  # Critical Line
        return __round_key

    # Round Key Generator
    def __round_key_gen(self):
        for Round in range(1, 17):
            if Round in self.__oneshift:
                # Perform Only a single Shift
                round_key = self._generate(shifts=1)
                # print(f"Round {Round} : Key {round_key}")
            else:
                # Perform 2 Shifts
                round_key = self._generate(shifts=2)
                # print(f"Round {Round} : Key {round_key}")

    def round_keys(self):
        self.__round_key_gen()
        return self.__keys


def main():
    key = "secret12"
    key_gen = Keyschedule(key=key)
    print(key_gen.round_keys())

    # Reverse keys
    # for ky in range(16, 0, -1):
    #    print(key_gen.round_keys()[ky-1])


if __name__ == "__main__":
    main()
