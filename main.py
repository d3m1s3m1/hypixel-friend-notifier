from hypixelapi import *
from win10toast import ToastNotifier
from time import sleep
from datetime import datetime


def main():
    f = open("log.txt", "a")
    toaster = ToastNotifier()
    friends_online, person_online, game_types = get_friends_online()

    if not person_online:
        f.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} NO ONE ONLINE.\n")
        f.close()
        # print("No one is online.")
        return

    notification_string = ""
    for friend, online_status in friends_online.items():
        if online_status:
            notification_string += f"{friend} - {game_types[friend]}\n"
    toaster.show_toast("Friends Are Online!", notification_string, threaded=True, icon_path=None, duration=10)
    notification_string = notification_string.replace("\n", ",")
    f.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} {notification_string}\n")
    f.close()
    return


if __name__ == "__main__":
    while True:
        main()
        sleep(COOL_DOWN)
