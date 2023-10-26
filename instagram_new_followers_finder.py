import instaloader
import getpass 

old_followers = []
new_followers = []

f = open("Py2/Assignment4/followers.txt" , "r")

for line in f :
    old_followers.append(line)
f.close()

L = instaloader.Instaloader()

username = input("please enter your username: ")
password = getpass.getpass("please enter your password: ")

L.login(username,password)
print("you have connected successfully")

profile=instaloader.Profile.from_username(L.context,"zzsnowdrop")

for follower in profile.get_followers():
    new_followers.append(follower)

for n_follower in new_followers:
    if n_follower not in old_followers:
        print(n_follower)

f.close()

f = open("Py2/Assignment4/followers.txt" , "w")        
for follower in new_followers:
    f.write(follower + "\n")
    f.close()
    