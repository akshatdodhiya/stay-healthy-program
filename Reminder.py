import datetime  # Importing module to run program as per
import time  # Importing module to make program to sleep for a specific intervals

from pygame import mixer  # Importing module to play music in each function

current_time = datetime.datetime.now()  # Get the current date and time


def drink_water():
    """
    This function will play sound for user to remind about drinking water
    and it will store the water drinking data of the user in a separate file named Water log.txt
    """
    mixer.init()  # Initialising the mixer of pygame to use for playing sounds
    mixer.music.load('Sounds\water.mp3')  # Loading the sound to remind for drinking the water
    print("Go and Drink 250mL of water :)")  # Printing for the user to drink 250mL of water

    mixer.music.play()  # Playing the music for user
    time.sleep(5)  # Waiting for the music to complete till then program is made to sleep

    mixer.music.load('Sounds\play-song.mp3')  # Loading sound to tell options to user to stop the music to be played
    mixer.music.play()  # Playing notice to user
    time.sleep(3)  # Waiting for the sound to complete

    inp = input("Enter 'P' to play the song :)\n").lower()  # Taking input for playing the song

    if inp == 'play' or inp == 'p':
        mixer.music.load('Sounds\Drink More Water.mp3')  # Loading Song which tells about benefits of drinking water
        mixer.music.play()  # Playing song
        time.sleep(132)

    while True:  # Infinite loop until the user enters the correct input

        mixer.music.load('Sounds\water-complete.mp3')
        # Loading sound to ask whether the user drank the water or not
        mixer.music.play()  # Playing sound
        time.sleep(2)  # Waiting for the sound to get complete

        water_complete = input("Enter Drank if you drank the water! :)\n").lower()
        # Taking user's input for he/she drank the water or not

        if (water_complete == "drank" or water_complete == "d"
                or water_complete == "yes" or water_complete == "done"):
            # Condition to check whether the user drank the water or not
            with open("Log\Water log.txt", "a") as w:
                # Opening Water log.txt in append mode to add data into existing
                w.write(time.asctime(time.localtime(time.time())))
                # Writing the current time in local format in file
                w.write("\t" + water_complete + "\n")  # Adding the input of the user as signature
                break  # breaking the loop if the user enters correct/valid input


def eye_exercise():
    """
    This function will play sounds that will remind the user
    to do eye exercise for three minutes and also it stores
    the eye exercise data of the user with time in Eye log.txt file.
    """
    mixer.init()  # Initializing the mixer
    mixer.music.load('Sounds\eye.mp3')  # Loading the sound for reminding about eye exercise
    print("Do some eye exercise for 3 minutes :)")  # Printing time for the user to do eye exercise

    mixer.music.play()  # Playing the sound
    time.sleep(180)  # Waiting 180 seconds for the user to do exercise

    while True:
        mixer.music.load('Sounds\eye-complete.mp3')  # Loading sound for asking user if he/she had done eye exercise
        mixer.music.play()  # Playing sound
        time.sleep(2)  # Waiting the sound to get complete

        eye_complete = input("Enter done if you have completed eye exercise! :)\n").lower()
        # Taking input for user's exercise completion

        if eye_complete == "d" or eye_complete == "done" or eye_complete == "yes":
            with open("Log\Eye log.txt", "a") as e:  # Opening Eye log.txt in append mode
                e.write(time.asctime(time.localtime(time.time())))  # Adding date & time in file
                e.write("\t" + eye_complete + "\n")  # Adding input of the user as signature of work completion
                break  # breaking infinite loop if user enters correct/valid input


def body_exercise():
    """
    This function will play sound that reminds
    the user to do exercise for the body for five
    minutes and also it stores the exercise data
    of the user with time in Exercise log.txt file.
    """
    mixer.init()  # Initializing the mixer to play sound
    mixer.music.load('Sounds\exercise.mp3')  # Loading exercise reminder sound
    print("Do some exercise for 5 minutes :)")  # Displaying time to the user for he/she has to do exercise

    mixer.music.play()  # Playing sound
    time.sleep(300)  # Waiting 5 minutes till the user completes the exercise

    while True:
        mixer.music.load('Sounds\exercise-complete.mp3')  # Loading completed exercise question audio file
        mixer.music.play()  # Playing audio
        time.sleep(2)  # Waiting for the audio to get complete

        exercise_complete = input("Enter done if you have completed the exercise! :)\n").lower()
        # Taking input from user of work completion

        if exercise_complete == "d" or exercise_complete == "done" or exercise_complete == "yes":
            with open("Log\Exercise log.txt", "a") as ex:  # Opening Exercise log.txt in append mode
                ex.write(time.asctime(time.localtime(time.time())))  # Adding current time in format in the file
                ex.write("\t" + exercise_complete + "\n")  # Adding the input of the user as a signature
                break  # breaking infinite loop if user enters the correct/valid input


def clear_records():
    """
    This function will clear the stored record of the user
    each of water, eye and exercise on day 1 of every month
    from files Water log.txt, Eye log.txt and Exercise log.txt
    respectively
    """
    if 1 == current_time.day:
        with open("Log\Water log.txt", "r+") as clear:  # Opening file in write mode which removes earlier data
            clear.truncate()

        with open("Log\Exercise log.txt", "r+") as clear:
            clear.truncate()

        with open("Log\Eye log.txt", "r+") as clear:
            clear.truncate()


clear_records()  # Calling function to clear the records

while True:  # Running an infinity loop to make the program to run whole day
    current_time = datetime.datetime.now()  # Get the current date and time

    if 9 <= current_time.hour < 21:  # Using condition to run program between 9 a.m. to 6 p.m.

        if current_time.minute == 30 or current_time.minute == 59:
            # Using condition which will be satisfied at every 30 minutes
            drink_water()  # Running function at interval of 30 minutes

        if current_time.minute == 59:  # Using condition that will be satisfied at every 1 hour
            body_exercise()  # Running functions at interval of 1 hour
            eye_exercise()

    elif current_time.hour <= 9:  # Continuing the loop if program is run before 9 a.m.
        continue

    else:  # Exit the program after 9 p.m
        exit()
