import requests, random, urllib
from PIL import Image
import glob

frames = []
glob = glob.glob("*.png")

def opensea_gif_generator(collection_name):
  images = []
  print ("Generating...")
  try:
    response = requests.get(f"https://api.opensea.io/api/v1/collection/{collection_name}")
  except:
    return False
  try:
    collection_id = response.json()["collection"]["primary_asset_contracts"][0]["address"]
  except:
    return False
  collection_stats = requests.get(f"https://api.opensea.io/api/v1/collection/{collection_name}/stats").json()["stats"]["count"]
  collection_amount = str(collection_stats).split(".", 1)[0]

  for x in range(25):
    r = requests.get(f"https://api.opensea.io/api/v1/asset/{collection_id}/{random.randint(1, int(collection_amount))}/")
    images.append(r.json()["image_url"])
  for i in images:
    urllib.request.urlretrieve(i, f"{images.index(i)}.png")
    new_frame = Image.open(f"{images.index(i)}.png")
    frames.append(new_frame)
  
opensea_gif_generator("suburbancolors-collection")
frames[0].save("result.gif", format="GIF", append_images=frames[1:], save_all=True, duration=230, loop=0)
print ("Finished! Check result.gif for your result.")
