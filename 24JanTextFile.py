#write(replace)
with open ("24thJantest.txt","w") as file:
    file.write("HELLO IM @ 100%")

#write(add)
with open ("24thJantest.txt","a") as file:
    file.write(" Hello this is a file um hi")

#read
with open ("24thJantest.txt") as file:
    print(file.read())

#if it exists
import os
if os.path.exists("THISISFAKE.txt"):
    os.remove("THISISFAKE.txt")
else:
    print("It is just a figment of your imagination :)")

