from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)


test = [
    "Skill is a term that encompasses the knowledge, competencies and abilities to perform operational tasks. Skills are developed through life and work experiences and they can also be learned through study.", 
    "The productivity of artificial intelligence may boost our workplaces, which will benefit people by enabling them to do more work. As the future of AI replaces tedious or dangerous tasks, the human workforce is liberated to focus on tasks for which they are more equipped, such as those requiring creativity and empathy.", 
    "The origins of human intelligence and conduct may be traced back to the individual's unique combination of genetics, upbringing, and exposure to various situations and environments. And it hinges entirely on one's freedom to shape his or her environment via the application of newly acquired information. The information it provides is varied. For example, it may provide information on a person with a similar skill set or background, or it may reveal diplomatic information that a locator or spy was tasked with obtaining. After everything is said and done, it is able to deliver information about interpersonal relationships and the arrangement of interests."]


if __name__ == "__main__":
    while True:
        ch = input("Ready to take the test? (Yes / No) : ")
        print(ch.upper())
        if ch.upper() == "YES":
            test1 = r.choice(test)
            print("\n \t**** Typing Test ****\n")
            print(test1, "\n")

            time_1 = time()
            testinput = input("Enter : ")
            time_2 = time()
            print("\n")
            print("Speed : ", speed_time(time_1, time_2, testinput), "w/s")
            print("Error : ", mistake(test1, testinput))
        elif ch.upper() == "NO":
            print("Thank you for taking the test...\n")
            break
        else: 
            print("Wrong Input")
