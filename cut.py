lines=[]
long=[]
medium=[]
short=[]
Flag0 = 5
Flag1 = 12
Flag2 = 24
Flag3 = 10000
lines2 = []
with open('/Users/zhangyang/Desktop/project2/DeepCov-master/866-all.rr', 'r') as f:
    line = f.readline()
    num = len(line)
    print(line)
    while True:
        line = f.readline()
        if not line:
            break
        #print(line)
        line = line.strip('\n')
        lines.append(line.split(' '))
    lines2 = sorted(lines,  key=lambda num: num[4], reverse=True)

with open('/Users/zhangyang/Desktop/project2/DeepCov-master/866-all-sort.rr', 'w') as wf:
    for lines in lines2:
        for e in lines:
            wf.write(''.join(e))
            wf.write(' ')
        wf.write('\n')


for line in lines2:
    if int(line[1])-int(line[0])>= Flag0 and int(line[1]) - int(line[0]) < Flag1:
        short.append(line)
    elif int(line[1]) - int(line[0]) >= Flag1 and int(line[1]) - int(line[0]) < Flag2:
        medium.append(line)
    elif int(line[1]) - int(line[0]) >= Flag2 and int(line[1]) - int(line[0]) < Flag3:
        long.append(line)

short = short[0:36]
medium = medium[0:36]
long = long[0:36]

with open('/Users/zhangyang/Desktop/project2/DeepCov-master/866-all.rr', 'w') as wf:
    for lines in long:
        for e in lines:
            wf.write(''.join(e))
            wf.write(' ')
        wf.write('\n')

with open('/Users/zhangyang/Desktop/project2/DeepCov-master/866-all.rr', 'w') as wf:
    for lines in medium:
        for e in lines:
            wf.write(''.join(e))
            wf.write(' ')
        wf.write('\n')

with open('/Users/zhangyang/Desktop/project2/DeepCov-master/866-all.rr', 'w') as wf:
    for lines in short:
        for e in lines:
            wf.write(''.join(e))
            wf.write(' ')
        wf.write('\n')

