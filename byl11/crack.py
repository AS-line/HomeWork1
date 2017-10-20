import os
files = os.listdir(path= '.')
print(len(files))
i = 1
while i <= len(files):
    i += 1
    os.rename(files[i],'Натяжные потолки 89799785867'+ '(' + str(i) + ')')
    pass