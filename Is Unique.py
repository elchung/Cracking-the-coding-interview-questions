'''implement an algorithm to determine if a string has all unique characters. What if you cannot use additonal data structrures?'''


#with additional data structures
def is_unique(word):
  used_words = set()
  for c in word:
    if c in used_words:
      return False
    else:
      used_words.add(c)
   return True
   

#without additional data structures
def is_unique(word):
  for index, f in enumerate(word):
    for l in word[index + 1:]:
      if f == l:
        return False
  return True
