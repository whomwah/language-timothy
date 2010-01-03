import re
import random

def readProfanities():
  profanities = []
  file = open('profanity-list.txt','r')
  for line in file:
    line = line.strip()
    profanities.append(line)
  return profanities
  
profanities = readProfanities()

def replaceProfanity( text ):
  results = [] 
  for w in re.finditer(r"[\w']+", text):
    if w.group(0).lower() in profanities:
      results.append(w)
  def compare(a, b):
    return cmp(int(a.end()), int(b.end()))
  results.sort(compare)
  results.reverse()
  return results

if __name__ == '__main__':
  w = "So you're an utter twat, and he's a complete dick shit, yes dick."
  for r in replaceProfanity(w): 
    print r.group(0), r.end()
