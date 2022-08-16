s = "    Hello,    Ming , the  ,World!"
s = s.strip()
words = s.split(',')
newwords = []
for w in words:
  newwords.append(w.strip())
print(newwords)
