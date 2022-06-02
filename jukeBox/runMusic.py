from pygame import mixer
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="JukeBox",
  database='pibox'
)
print(mydb)
# Doesnt auto increment primary key like expected? If get an error inserting it still increments
# First thing it does is should play music so I know if its on
# Add Skip
# Add random shuffle
# add power hour feature? Plays song for a minute

mycursor = mydb.cursor()
mixer.init()

while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
    file = ""

    if query == 'e':
        print("exit")
        # Stop the mixer
        # mixermixer.music.stop()
        break

    mycursor.execute("SELECT * FROM songs WHERE SongId = " + query)

    myresult = mycursor.fetchone()


    if myresult is not None:
        print(":::::::::::")
        file = myresult[2]

        if (not mixer.music.get_busy()):
            print("Playing")
            #  need to load song here
            try:
                mixer.music.load(file)
                mixer.music.play()
            except:
                print("Incorrect SongID Entered")
        else:
            mixer.music.queue(file)

