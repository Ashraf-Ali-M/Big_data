name = input("Enter a file name : ")
name+=".txt"
f = open("2.File_Handling\\"+name,'w')

print("Enter the content : <type end to finish the content>\n")
while True:
  line = input()
  if line == 'end':
    break
  else:
    f.write(line)
    f.write('\n')
  
f.close()