from os.path import exists
filename="new.txt"
from_file=open(filename,"w+")
from_file.write("Hello")
from_file=open(filename,"r")
text=from_file.read()
print (text)
print exists (filename)
