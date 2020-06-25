letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters,points)}

letter_to_points[" "] = 0

def score_word(wordInput):
  word = wordInput.upper()
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter,0)

  return point_total

brownie_points = score_word("abc")
print(brownie_points)

player_to_words = {"player1":["BLUE","TENNIS","EXIT"], "player2":["EARTH","EYES","MACHINE"],"player3":["ERASER","BELLY","HUSKY"], "player4":["ZAP","COMA","PERIOD"]}

player_to_points = {}
playedWord = []

def played_word(word):
  playedWord.append(word)

def update_point_totals(words):
  player_points = 0
  for word in words:
    player_points += score_word(word)
    played_word(word)
  return player_points

for player, words in player_to_words.items():
  player_to_points[player] = update_point_totals(words)
  print("Played Words:" + str(playedWord))

print(player_to_points)

#WINNER IS PLAYER2....
