import random
import os
def play(ans,word):
    list_sim = list(word)
    list_ans = list (ans)
    os.system("clear")
    change(list_sim,ans)
    
    while ''.join(list_sim) != ''.join(list_ans):
        play(answer(), word)
def answer():
    answer =input("\nIngresa tu respuesta: ")
    return answer 

def gen_spc(word):
    cant = len(word)
    list_com = list(word)
    i = 0

    while i != cant:
        print("_", end = " ")
        i+=1  

def change(my_list,letter):
    for i in range(len(my_list)):
        if my_list[i] == letter:
            print(letter,end = " ")
        else:
            print("_", end = " ")

def show(word):
    os.system("clear")
    print("AHORCADO!!!\n\n")
    gen_spc(word)
    print(word)
    play(answer(),word)
    

#generator my word
def next_word():
    names = []
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        for line in f:
            names.append(str.rstrip(line))
    num = random.randrange(171)
    return names[num]

def run():
    show(next_word())
    print("ganaste")
    
if __name__ == "__main__":
    run()