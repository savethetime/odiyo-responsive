file_name = input("파일이름 : ")

file_name_ext = file_name+'.html'
file = open(file_name_ext, 'r', encoding='utf-8')
rows = file.readlines()

num = 1
data = ''
for row in rows:
    print(row, end='')
    data += '%3d    ' % num + row
    num += 1

file.close()

file_name = file_name+'_.html'
file = open(file_name, 'w')
file.write(data)

file.close()



