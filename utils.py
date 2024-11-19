import struct
"""
Some useful functions to manipulate bytes
Author: Mohamed Abdelkader
Contact: mohamedashraf123@gmail.com
"""

def toHex(value, nbits, is_float=False):
    """
    Converts an integer or float to hexadecimal and reverses the order of each two characters (bytes)
    if the length of the hex string exceeds two characters.

    Params
    --
    - value: [int/float] The number to convert (integer or float).
    - nbits: [int] Number of bits (e.g., 8 for int8_t, 16 for int16_t, 32 for float, 64 for double).
    - is_float: [bool] Whether the value is a float. Default is False.

    Returns
    --
    String of the hexadecimal value, padded appropriately based on the bit size, with
    reversed byte order for hex strings longer than 2 characters.
    """
    if is_float:
        if nbits == 32:
            # Convert float to 32-bit IEEE 754 format
            packed = struct.pack('<f', value)  # Little-endian single precision
        elif nbits == 64:
            # Convert float to 64-bit IEEE 754 format
            packed = struct.pack('<d', value)  # Little-endian double precision
        else:
            raise ValueError("Unsupported bit length for float. Use 32 or 64 bits.")
        h = packed.hex()
    else:
        # Integer conversion logic
        num_hex_chars = nbits // 4  # 4 bits per hex digit
        h = format((value + (1 << nbits)) % (1 << nbits), 'x').zfill(num_hex_chars)

    # Reverse byte order for hex strings longer than 2 characters
    if len(h) > 2:
        h = ''.join([h[i:i + 2] for i in range(0, len(h), 2)][::-1])

    return h

def toInt(hexval):
    """
    Converts hexidecimal value to an integer number, which can be negative
    Ref: https://www.delftstack.com/howto/python/python-hex-to-int/

    Params
    --
    hexval: [string] String of the hex value
    """
    bits = 16
    val = int(hexval, bits)
    if val & (1 << (bits-1)):
        val -= 1 << bits
    return val