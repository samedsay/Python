def unique_english_letters(word):
  letterList = []
  for letter in word:
    if letter not in letterList:
      letterList.append(letter)
  return len(letterList)

######################################################

def count_char_x(word, x):
  return word.count(x)

######################################################

def substring_between_letters(word, start, end):
  if word.find(start) == -1 or word.find(end) == -1:
    return word
  else:
    return word[word.find(start)+1:word.find(end)]

######################################################  
    
def x_length_words(sentence, x):
  sentenceArray = sentence.split()
  for word in sentenceArray:
    if len(word) < x:
      return False
  return True

######################################################
  
def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False
 
######################################################
    
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

######################################################

def reverse_string(word):
  return word[::-1]

######################################################

def make_spoonerism(word1, word2):
  firstLetterWord1 = word1[0]
  word1 = word2[:1] + word1[1:]
  word2 = firstLetterWord1 + word2[1:]
  return word1 + " " + word2

######################################################

def add_exclamation(word):
  if len(word) >= 20:
    return word
  else:
    while len(word) < 20:
      word += "!"
    return word

######################################################
  
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total

######################################################



