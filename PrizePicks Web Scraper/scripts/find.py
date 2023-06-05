# function to find if a dict with two matching key/value pairs exists within a given list
def find(lst, key1, value1):
  for i, dic in enumerate(lst):
      if dic[key1] == value1:
        return i
  return -1
