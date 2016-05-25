#!/usr/bin/env python
import sys
import string

number_counter=0
number_count={}
prime_count=0

for line in sys.stdin:
  numbers = line.split()
  for number in numbers:
    if number in number_count:
       number_count[number]+=1
    else:
       number_count[number]=1
#total # of numbers
    try:
      number_counter+=1
    except:
      continue

#count of prime numbers
for number in number_count:
    if int(number)>1:
      for  i in range(2,int((int(number)/2))):
        if(float(number)%i)==0.0:
           break
      else:
        prime_count+=int(number_count[number])


for number in number_count:
		print '%s\t%s' %(number,number_count[number])
print '%s\t%s' % ('Count',number_counter)
print '%s\t%s' %('Prime number',prime_count)
