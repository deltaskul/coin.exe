import os
import random
from playsound import playsound
# I removed the B64 encode, it was useless.

#unga bunga caveman code :)


print("Engaging...")


while input("Press ENTER. Go on. You wont.") == "" or " ":
    outcome = random.choices(
        ["THE COIN LANDED ON...HEADS!",
         "THE COIN LANDED ON...TAILS!",
         "THE COIN LANDED ON...THE SIDE!"],
        weights=[49.5, 49.5, 1],
        k=1)[0]
    
    print("Intensely flipping coin...")
    playsound('audio/standinghere.mp3')
    playsound('audio/Judgement.wav')
    print(outcome)
    
    if outcome == "THE COIN LANDED ON...HEADS!":
        playsound('audio/HEADS.wav')
    
    if outcome == "THE COIN LANDED ON...TAILS!":
        playsound('audio/TAILS.wav')
    
    if outcome == "THE COIN LANDED ON...THE SIDE!":
        playsound('audio/aaa.mp3')
        

    while input("ok but you wouldn't press enter AGAIN, right?"):
        if input != "":
            os.system("shutdown /s /t 0")

    playsound('audio/pikmin.mp3')
    raise SystemExit
