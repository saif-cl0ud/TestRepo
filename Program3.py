name = str(input('Enter Student Name : '))
sub1 = int(input('Enter marks of subject 1: '))
sub2 = int(input('Enter marks of subject 2: '))
sub3 = int(input('Enter marks of subject 3: '))

total= sub1 + sub2 + sub3
 
average = total / 3
 
print('The total marks obtained by Student %s is  %d' % (name,total))
print('The average marks obtained by Student %s is %d'% (name,average))