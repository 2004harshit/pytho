# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode


msg = input("Enter a message")

# emcoding 

print("!Encoding of the message begins  ......")
size = len(msg)

if size>=3:
    partition1 = msg[0:1]
    partition2= msg[1:size]
    randomChar_at_begining= "&*^"
    randomChar_at_end= "!@#"
    msg = randomChar_at_begining+partition2+partition1+randomChar_at_end
    print("Encode message = ",msg)

else:
    msg = msg[::-1]
    print("Encoded message = ",msg)
    
print("Decodig Begins ......")


if size>=3:
    partition1 = msg[0:3]
    partition2= msg[-1:-4]
    length= len(partition1+partition2)
    size = size-len
    randomChar_at_begining= "&*^"
    randomChar_at_end= "!@#"
    
    print("Encode message = ",msg)

else:
    msg = msg[::-1]
    print("Encoded message = ",msg)