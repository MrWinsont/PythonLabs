from PIL import Image
from argparse import ArgumentParser
from pathlib import Path

argumentParser = ArgumentParser()
argumentParser.add_argument("-ftype")
format = argumentParser.parse_args().ftype

path = Path("images")

for i in path.iterdir():
   try:
      with Image.open(i) as img:
         if img.format.lower() == format:
            new = img.resize((50, 50))
            new.show()
   except:
      pass
