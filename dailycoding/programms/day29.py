"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA"
would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
solely of alphabetic characters. You can assume the string to be decoded is valid.
"""
import string

#counting number of letters and put them on a new decoded string
encoded_string = "AAAABBBCCDAA"


letter_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
for letter in letter_dict:
    letters = letter_dict[letter]
    print(letters)
