from pygame import mixer

mixer.init()

while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
    file = ""


    if query == '111':
        print("pause")
        file = "C:/Users/EyeOf/Desktop/Spahget.mp3"
        if (mixer.music.get_busy()):
            mixer.music.queue(file)

    elif query == '222':
        print("resume")
        file = 'C:/Users/EyeOf/Desktop/Rent.mp3'
        if (mixer.music.get_busy()):
            mixer.music.queue(file)


    elif query == 'e':
        print("exit")
        # Stop the mixer
        # mixermixer.music.stop()
        break

    if (not mixer.music.get_busy()):
        print("Playing")
        #  need to load song here
        mixer.music.load(file)
        mixer.music.play()
