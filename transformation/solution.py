"""
We are given a file named enc
we look what is in the file using cat command in terminal , it turns out it is just a string "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽" which was encoded 

description of problem :
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

Solution:
Understanding the Encoding Process:

    The code takes pairs of characters from the string flag.
    For each pair, it calculates a new character by shifting the first character left by 8 bits (essentially multiplying by 256) and then adding the ASCII value of the second character.
    This effectively combines two characters into one.

Breaking Down the Code:

    ord(flag[i]): Gets the ASCII value of the first character in the pair.
    ord(flag[i + 1]): Gets the ASCII value of the second character in the pair.
    ord(flag[i]) << 8: Shifts the ASCII value of the first character left by 8 bits.
    chr((ord(flag[i]) << 8) + ord(flag[i + 1])): Combines the two values and converts them back to a character.

Reversing the Process:

    To reverse the encoding, we need to split the encoded characters back into pairs of the original characters.
    For each encoded character:
        Convert it back to an integer using ord.
        Extract the high and low bytes:
            The high byte is the result of integer division by 256.
            The low byte is the result of taking the modulus 256.
        Convert these byte values back to characters using chr.

Implementing the Decoding:

    Let's write a function that processes each character in the encoded string.
    Use integer division and modulus to get the original ASCII values.
    Convert these values back to characters."""
    

def decode(encoded_string):
    decoded_chars = []
    for char in encoded_string:
        encoded_value = ord(char)
        high_byte = encoded_value // 256
        low_byte = encoded_value % 256
        decoded_chars.append(chr(high_byte))
        decoded_chars.append(chr(low_byte))
    return ''.join(decoded_chars)
print(decode("灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"))

#prints picoCTF{16_bits_inst34d_of_8_e141a0f7}   which is the answer


