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
  text = text.lower()
  tmp = {} 
  for w in profanities: 
    w = w.split(':')
    for m in re.finditer(re.escape(w[0]), text):
      key_str = m.start()
      if len(w) > 1:
        for wl in w[1].split(','):
          if wl not in text:
            tmp[key_str] = m
      else:
        tmp[key_str] = m
  def compare(a, b):
    return cmp(int(a.end()), int(b.end()))
  results = tmp.values() 
  results.sort(compare)
  results.reverse()
  return results

if __name__ == '__main__':
  w = """
  Shit So you're an utter pussy, you turd, not saturday. <unt, [ock. So
  dick what the fuck are you gonna fucking do. You dickheads suck cock
  and I think you're a twat.
  """
  print w.strip()
  for m in replaceProfanity(w): 
    print m.group(0)[0] + '*'*(len(m.group(0))-2) + m.group(0)[len(m.group(0))-1] 
