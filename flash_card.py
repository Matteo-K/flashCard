import re, os, unicodedata
from random import randint

import unicodedata

def normalize(s: str) -> str:
    """
    Normalize a string by removing diacritic marks and converting it to lowercase ASCII.

    Args:
        s (str): The string to normalize.

    Returns:
        str: The normalized string.
    """
    return unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode().casefold()

def openFile(nameFile: str) -> dict:
    res = {}
    with open(nameFile, 'r') as f:
        regex = re.compile(r"(.*);(.*)")
        for line in f:
            line = line.rstrip('\n')
            resultat = regex.search(line)
            res[resultat.group(1)] = resultat.group(2)
    return res

def learn(array):
    os.system("cls||clear")
    choice = ""
    for key in array:
        print(key," ", array[key], end=" ")
        choice = input()
        if choice == "0":
            break
    choice = input("(end)")
    while choice != "0":
        choice = input("back menu : 0")

def check(test: str, result: str) -> bool:
    """
    Vérifie si l'entre de l'utilisateur 
    correspond à la réponse de la carte
    """
    test_normalized = normalize(test)
    result_normalized = normalize(result)

    r = re.split(r'(.*)\/+', result_normalized)
    check = False
    for res in r:
        if test_normalized == res:
            check = True
    return check

def question_answer(array):
    keys = list(array.keys())
    choice = ""
    size = 20
    incorrect = []
    if len(keys) < 20:
        size = len(keys)-1
    correct,quest = 0,0
    while quest < size:
        os.system("cls||clear")
        print(f"question {quest+1}")
        x = (randint(0,2))%2
        key = randint(0,len(keys)-1)
        if x == 0:
            print(keys[key],end="\n")
            res = array[keys[key]]
        else :
            print(array[keys[key]],end="\n")
            res = keys[key]
        k = keys.pop(key)
        choice = input("result : ")
        quest += 1
        if check(choice.lower(),str(res).lower()) == True:
            print("correct")
            correct += 1
        else :
            print("incorrect, the correct result was : ",res)
            incorrect += [k]
        input()
    return correct,quest,incorrect

def card(array : dict):
    keys = list(array.keys())
    choice = ""
    while choice != "0":
        os.system("cls||clear")
        x = (randint(0,2))%2
        key = randint(0,len(keys)-1)
        if x == 0:
            print(keys[key],end=" ")
            choice = input()
            if choice == "0":
                break
            print(array[keys[key]])
            choice = input()
        else :
            print(array[keys[key]],end=" ")
            choice = input()
            if choice == "0":
                break
            print(keys[key])
            choice = input()

def main():
    found = False
    while not found:
        nameFile = input("name of file : ")
        try : 
            with open(nameFile,'r') as f:
                found = True
        except FileNotFoundError:
            print(f"Error : file {nameFile} not found")
    array = openFile(nameFile)
    choice = ""
    while choice != "0":
        os.system("cls||clear")
        print("-- Menu --\n0.Leave\n1.Learn\n2.Question answer\n3.card")        
        choice = input("choice : ")
        if choice == "0":
            print("thanks")
        elif choice == "1":
            learn(array)
        elif choice == "2":
            correct,quest,incorrect = question_answer(array)
            print("You have",correct,"on",quest)
            print("\nyour incorrect answers :")
            for key in incorrect:
                print(f"{key} - {array[key]}")
            chc = input()
            while chc != "0":
                chc = input("back menu : 0")

        elif choice == "3":
            card(array)

main()