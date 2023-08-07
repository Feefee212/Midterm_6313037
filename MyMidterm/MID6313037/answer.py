import numbers


def q01():
    list = [1,2,3,4,5,6,7,8,9,10]
    result = 0
    for i in range(1,11):
        print(i)
    return result


def q02():
    full_name = 'Ms. Kamisato Ayaka'
x = "Title: Ms."
y = "Firstname: Kamisato"
z = "Lastname: Ayaka"
print(x)
print(y)
print(z)
    return 0


def q03():
    sentence = 'I feel like running'
    non_vowels = "flkrn"

    count = sum(sentence.count(non_vowels) for non_vowels in non_vowels)
    print(count)
    return 0 # number of non-vowels characters


def q04(n):
    for n in range(0,11):
        return 0 #Recursive programming

# Q5
class Weapon:
    name = ""
class Type:
      Type = ""
  #


def q06():
    class Node:
        def __init__(self,Weapon=None):
            Weapon = "Skyward Harp"
            type = "Bow"

    class Node:
        def __init__(self, Weapon=None):
            Weapon = "Mist-splitter Reforged"
            type = "Sword"
    return 0 #Linked List



def q07(nation):
    nation_data = {
"Mondstadt" : "From amongst mountains and wide-open plains, carefree breezes carry the scent of dandelions - a gift from the Anemo God, Barbatos.",
"Liyue": "Mountains stand tall and proud alongside the stone forest, that,together with the open plains and lively rivers.",
"Inazuma": "On winding shores and towering cliffs, and in forests and mountains full of secrets, witness the Eternity pursued by Her Excellency, the Almighty Narukami Ogosho."
       }
    description = nation.get(nation, "Archon not found.")
    return "Description"
