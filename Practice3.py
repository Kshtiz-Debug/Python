"""


Multilie comment
What is rjust,ljust,centre().
"""

str="Hello World"
len_str=len(str)
print(len_str)
str1=str.rjust(13)        # The number inside it should be more than length of str.
# It shifts the string to right side and the total length of the string will be 13.
print(str1)


str2=str.ljust(13,"=")
print(str2)


"""


Then we can use lstrip , rstrip ,strip() functions to removie 
Whitespace characters from the left or right end respectively.

"""


string="SpamSpamBaconSpamEggBaconSpamSpam"
print(string.strip("Bacon"))