# Marketplace for people and organizations

class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  
  def __repr__(self):
    return """{artist}. "{title}". {year}, {medium}. {owner_name}, {owner_location}""".format(artist = self.artist,title = self.title, medium = self.medium, year = self.year, owner_name = self.owner.name, owner_location = self.owner.location)


class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  def remove_listing(self, deleted_listing):
    self.listings.remove(deleted_listing)

  def show_listings(self):
    for listing in self.listings:
      print(listing)

veneer = Marketplace()
veneer.show_listings()

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self) 
      veneer.add_listing(new_listing)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)  

edytta = Client("Edytta Halpirt", "Private Collection", False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)

print(girl_with_mandolin)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller 

  def __repr__(self):
    return "{name}, {price}".format(name = self.art.title, price = self.price)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()

