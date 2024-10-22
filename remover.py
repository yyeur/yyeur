# Made by Yasser
# Contact on Telegram: https://t.me/yyeir

from TikTokAPI import TikTokAPI

def delete_reposts(username, password):
    api = TikTokAPI(username, password)
    if not api.isLoggedIn:
        print("Failed to log in. Check your username and password.")
        return

    try:
        user = api.getUserObject(username)
        reposts = user.reposts

        for repost in reposts:
            success = api.unrepostItem(repost.id)
            if success:
                print("Successfully deleted repost: " + repost.id)
            else:
                print("Failed to delete repost: " + repost.id)
                break

        print("Finished deleting reposts.")
    except Exception as e:
        print("An error occurred: " + str(e))

# طلب إدخال اسم المستخدم وكلمة المرور من المستخدم
username = input("Enter your TikTok username: ")
password = input("Enter your TikTok password: ")

delete_reposts(username, password)