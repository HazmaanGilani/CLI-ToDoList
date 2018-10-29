import datetime
from argparse import ArgumentParser
from time import gmtime, strftime
import os.path



CREATE_DATE = str(datetime.date.today())
TIME = str(strftime("%H:%M:%S", gmtime()))


#list to store notes
TASK_LIST = []


#for command line argument passing
ap = ArgumentParser()
ap.add_argument("-a", "--add", help="Add a Note")
ap.add_argument("-ap", "--priority_add", help="Add with Priority")
ap.add_argument("-r", "--read", help="Read Notes", action="store_true")
ap.add_argument("-s", "--search", help="Search a Note")
ap.add_argument("-d", "--delete", type=int, help="Delete a Note")
ap.add_argument("-c", "--completedTask", type=int, help="Completed the Task")
args = ap.parse_args()

if os.path.isfile("./text.txt"):
    file = open("text.txt", "r")
else:
    file = open("text.txt", "a+")

# To fetch data from the text file and add in list
for line in file:
    TASK_LIST.append(line)



def check():
    """check if file contains notes"""
    if os.stat("text.txt").st_size > 0:
        return True
    print("NO Tasks")
    return False


def read():
    """read/display the notes"""
    if check():
        file = open("text.txt", 'r')
        print(file.read())
        file.close()

def add():
    """to write the entered note on the list"""
    data = str(args.add)
    TASK_LIST.append(CREATE_DATE + " " + data + "\n")
    write()

def write():
    """writes on the text file(database)"""
    file = open("text.txt", 'w')
    file.writelines(TASK_LIST)
    file.close()

def delete():
    """Deletes the Task at a particular position"""
    if check():
        print("Note Deleted: {}".format(TASK_LIST[args.delete - 1]))
        TASK_LIST.remove(TASK_LIST[args.delete - 1])
        write()


def completed():
    """Marks the the task completed"""
    print("Task Completed: {}".format(TASK_LIST[args.completedTask-1]))
    my_string = str(TASK_LIST[args.completedTask-1]).replace("\n", " ")
    TASK_LIST[args.completedTask-1] = "x " + my_string + "Completed on : " + TIME + "\n"
    write()

def search():
    """Search's the given word and return the Tasks containing that word"""

    #to convert list item in to string for splitting
    for list_item in TASK_LIST:
        list_item = str(list_item)
    #split by \n to get the sentence for searching
        for sentence in list_item.split("\n"):
            if args.search in sentence:
                print(sentence)


def priority_add():
    """Adds a Task with Priority"""
    data = str(args.priority_add)
    TASK_LIST.append("(A)" + CREATE_DATE + " " + data + "\n")
    TASK_LIST.sort()

    write()


# Checks arguments and calls corresponding functions

if args.add:
    add()

elif args.read:
    read()

elif args.delete:
    delete()
    read()

elif args.completedTask:
    completed()

elif args.delete:
    delete()

elif args.search:
    search()

elif args.priority_add:
    priority_add()
