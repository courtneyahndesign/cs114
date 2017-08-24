import random

def get_scream():
  numA = random.randint(1,15)
  numH = random.randint(1,15)
  textA = "A" * numA
  textH = "H" * numH
  return textA + textH

scream = get_scream()
print(scream)
