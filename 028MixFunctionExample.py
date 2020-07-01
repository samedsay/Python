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

def sum_even_keys(my_dictionary):
  total = 0
  for keys in my_dictionary.keys():
    if keys % 2 == 0:
      total += my_dictionary.get(keys)
  return total

######################################################

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

######################################################

def values_that_are_keys(my_dictionary):
  returnedList = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      returnedList.append(value)
  return returnedList

######################################################d

def max_key(my_dictionary):
  largest_key = ""
  largest_value = float("-inf")

  for key, value in my_dictionary.items():
    if largest_value < value:
      largest_value = value
      largest_key = key
      
  return largest_key

######################################################

def word_length_dictionary(words):
  dictionaryWords = {}
  for word in words:
    dictionaryWords[word] = len(word)
  return dictionaryWords

######################################################

def frequency_dictionary(words):
  freqDictionary = {}
  for word in words:
    if word not in freqDictionary.keys():
      freqDictionary[word] = 1
    else:
      freqDictionary[word] += 1
  return freqDictionary

######################################################




