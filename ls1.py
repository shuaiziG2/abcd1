file1 = open(r'\Users\Administrator\Desktop\test\abc.txt','r',encoding='utf-8')
file1_line=file1.readlines()
file1.close()
file_scores=[]
for i in file1_line:
    data=i.split()
    sum=0
    for score in data[1:]:
        sum=sum+int(score)
    result = data[0]+str(sum)+'\n'
    file_scores.append(result)
winner=open(r'\Users\Administrator\Desktop\test\ll.txt','w',encoding='utf-8')
winner.writelines(file_scores)
winner.close()
print(b'\xe5\xae\x9d\xef\xbc\x8c\xe6\x88\x91\xe4\xbb\x8a\xe5\xa4\xa9\xe8\xbe\x93\xe4\xba\x86\xe6\xb6\xb2\xef\
\xbc\x8c\xe6\x98\xaf\xe6\x83\xb3\xe4\xbd\xa0\xe7\x9a\x84\xe5\xa4\x9c~\xe6\x88\x91\xe7\x9a\x84\xe5\xae\x9d~'.decode('utf-8'))
# file = open(r'\Users\Administrator\Desktop\test\abc.txt','r',encoding='utf-8')
# file_lines = file.readlines()
# file.close()
#
# final_scores = []
#
# for i in file_lines:
#     data =i.split()
#     sum = 0
#     for score in data[1:]:
#         sum = sum + int(score)
#     result = data[0]+str(sum)+'\n'
#     final_scores.append(result)
#
# winner = open(r'\Users\Administrator\Desktop\test\222.txt','w',encoding='utf-8')
# winner.writelines(final_scores)
# winner.close()