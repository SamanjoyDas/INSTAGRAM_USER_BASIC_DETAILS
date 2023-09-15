import instaloader

ig=instaloader.Instaloader()

usrname=input("Enter username: ")

profile=instaloader.Profile.from_username(ig.context, usrname)

print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username+" is having " + str(profile.followers)+ 'followers.')
print(profile.username+" is following " + str(profile.followees)+ 'people.')
print("Bio: ", profile.biography)
print("InstaGram TV Count:", profile.igtvcount)
instaloader.Instaloader().download_profile(usrname, profile_pic_only=True)
instaloader.Instaloader().download_profile(usrname, download_stories=True)
