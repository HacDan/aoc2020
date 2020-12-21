f = open("input.txt","r")

"""
validPass = 0
for l in f:
    l = l.strip()
    policy = l.split(":")[0]
    password = l.split(":")[1]

    print("Policy: ", policy)
    print("Password: ", password)

    polCount = policy.split(" ")[0]
    polChar = policy.split(" ")[1]

    if polChar in password:
        low = int(polCount.split("-")[0])
        high = int(polCount.split("-")[1])
        print(low)
        print(high)
        polCharCount = 0
        for c in password:
            if c == polChar:
                polCharCount = polCharCount + 1

        if polCharCount >= low and polCharCount <= high:
            validPass = validPass + 1
print(validPass)  
"""
validPass = 0
for l in f:
    l = l.strip()
    policy = l.split(":")[0]
    password = l.split(":")[1].strip()

    # print("Policy: ", policy)
    # print("Password: ", password)

    polCount = policy.split(" ")[0]
    polChar = policy.split(" ")[1]

    if polChar in password:
        pos1 = int(polCount.split("-")[0]) - 1
        pos2 = int(polCount.split("-")[1]) - 1

        # print(pos1, pos2)
        if password[pos1] == polChar and password[pos2] == polChar:
            pass
        elif password[pos1] == polChar or password[pos2] == polChar:
            print(policy)
            print(password)
            print("pos1: ", pos1)
            print("pos2: ", pos2)

            validPass = validPass + 1

print(validPass)   