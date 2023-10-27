member = input("Add a new member : ")

file = open("../bonus/files/members.txt", 'r')
member_exist = file.readlines()
file.close()

member_exist.append(member + "\n")

file = open("../bonus/files/members.txt", 'w')
file.writelines(member_exist)
file.close()
