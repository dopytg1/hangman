import random

questions = {
    "animals": ["dog", "cat", "lion", "orca", "cow"],
    "cites": ["Toronto", "Bishkek", "Washington", "Almaty", "Astana", "NewYork"],
}

condition = [
""" 
    ¯¯|
      |
      |
""", 
"""
    ¯¯|
    0 |
      |
""",
"""
    ¯¯|
    0 |
    | |
""",
"""
    ¯¯|
    0 |
   /| |
""",
"""
    ¯¯|
    0 |
   /|\|
""",
"""
    ¯¯|
    0 |
   /|\|
   /  |
""",
"""
    ¯¯|
    0 |
   /|\|
   / \|
""",
]

categories_all = ""
for keys, values in questions.items():
    categories_all += keys + ", "

print(f"categories: {categories_all}")
category = questions[input("Choose category: ")]
rand_category = random.choice(list(questions.items()))
word = random.choice(category)
attempts = 7
condition_count = 0
word_guize = "*" * len(word)

def find_all_indices(word, letter):
    indices = []
    for each in range(len(word)):
        if letter == word[each]:
            indices.append(each)
    return indices

while attempts > 0:
    if "*" not in word_guize:
        print("YOU WON, CONGRATS!!!")
        break

    print(word_guize)
    quize = input("Letter: ")

    indices = find_all_indices(word.lower(), quize)
    for index in indices:
        list1 = list(word_guize)
        list1[index] = quize
        word_guize = "".join(list1)
        
    if quize not in word:
        print(condition[condition_count])
        condition_count += 1
        attempts -= 1

print(word)
