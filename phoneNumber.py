def isPhoneNumber(text):
    if len(text) != 12:
        return False #bigger than a phone number
    for i in range(0,3):
        if not text[i].isdecimal():
            return False    #no area code
    if text[3] != '-':
        return False        #missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False    #no first 3 digits
    if text[7] != '-':
        return False        #missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False    #missing last four digits
    return True

message = "Call me at my office line 208-111-1111 or my personal number 208-444-4444"
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('couldnt find any numbers')

#simpler way
found_number = False
chunk = message.split()
print(chunk)
for i in chunk:
    if isPhoneNumber(i):
        print('phone number found: ' + i)
        found_number = True
if not found_number:
    print('could not find any numbers')


