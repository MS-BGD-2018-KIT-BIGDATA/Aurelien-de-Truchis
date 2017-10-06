
# coding: utf-8

# In[ ]:

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###
import sys

def build_dict(file)
dict={}
text = open(file,'r')
    for line in text:
        words = line.split()
        for word in words:
            word=word.lower()
            if not word in dict:
                dic[word]=1
            else
                dict[word]=dict[word]+1
    return dict

def print_words(file):
  dic = build_dict(file)
  words = sorted(word_count.keys())
  for word in words:
    print word, word_count[word]


def get_count(word_count_tuple):
  return word_count_tuple[1]


def print_top(filename):
  dict = build_dict(filename)
  items = sorted(word_count.items(), key=get_count, reverse=True)
  for item in items[:20]:
    print item[0], item[1]

    def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()

