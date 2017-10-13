import re
import collections

# text = open('book.txt').read().lower()
# words = re.findall('\w+', text)
# print(collections.Counter(words).most_common(10))

f = open('files/relative_data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)
