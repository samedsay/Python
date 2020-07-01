def substring_between_letters(word, start, end):
  if word.find(start) == -1 or word.find(end) == -1:
    return word
  else:
    return word[word.find(start)+1:word.find(end)]
    
def x_length_words(sentence, x):
  sentenceArray = sentence.split()
  for word in sentenceArray:
    if len(word) < x:
      return False
  return True
  
def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False
    
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other
