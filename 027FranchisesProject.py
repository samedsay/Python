# Small Restaurant Example

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return ("{name} menu available from {start}am to {end}pm").format(name = self.name, start = self.start_time, end = self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for price in self.items.values():
      total += price
    return total
  
brunch = {
  "pancakes":7.50, "waffles":9.00, "burger":11.00, "home fries":4.50, "coffee":1.50, "espresso":3.00, "tea":1.00, "mimosa":10.50, "orange juice":3.50
}

brunch_menu = Menu("brunch", brunch, 1100, 1600)

early_bird = {
  "salumeria plate":8.00, "salad and breadsticks (serves 2, no refills)":14.00, "pizza with quattro formaggi":9.00, "duck ragu":17.50, "mushroom ravioli(vegan)":13.50, "coffee":1.50, "espresso":3.00
}

early_bird_menu = Menu("early_bird", early_bird, 1500, 1800)

dinner = {
  "crostini with eggplant caponata":13.00, "ceaser salad":16.00, "pizza with quattro formaggi":11.00, "duck ragu":19.50, "mushroom ravioli(vegan)":13.50, "coffee":2.00, "espresso":3.00
}

dinner_menu = Menu("dinner", dinner, 1700, 2300)

kids = {
  "chicken nuggets":6.50, "fusilli with wild mushrooms":12.50, "apple juice":3.00
}

kids_menu = Menu("kids", kids, 1100, 2100)

arepas = {
  "arepa pabello":7.00, "pernil arepa":8.50, "guayanes arepa":8.00, "jamon arepa":7.50
}

arepas_menu = Menu("arepas", arepas, 1000, 2000)

print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))

class Franchise:
  time = 0
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])

print(flagship_store)
print(new_installment)

print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))

class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepaBuss = Business("Take a' Arepa", [arepas_place])

print(basta.franchises)
print(arepaBuss.franchises)

print(basta.franchises[0])
print(arepaBuss.franchises[0])

print(basta.franchises[0].menus[0])
print(arepaBuss.franchises[0].menus[0])




