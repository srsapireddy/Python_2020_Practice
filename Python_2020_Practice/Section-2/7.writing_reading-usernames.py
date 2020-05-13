username = raw_input("Enter the username here:")
file_object = open("username1.txt","a")
file_object.write(username+"\n")
file_object.close()

file_object2 = open("username1.txt","r")
userlist = file_object2.read()
file_object.close()
print "Previous users of this program were: "
print userlist

