f = open('newfile.txt', 'w')    #writes a textfile
f.write("Hello")                #writes to the file
f.close()                       #closes the file


f = open('newfile.txt', 'a')    #opens textfile
f.write("Hello\nWorld\n")       #writes to the file
f.close()                       #closes the file



f = open('newfile.txt', 'a')    
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
f.write(lines)                  #writes line list
f.close()

f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
text = '\n'.join(lines)         #sets the next word to jump to new line link to .join:https://www.tutorialspoint.com/python/string_join.htm
f.write(lines)
f.close()