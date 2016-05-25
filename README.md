# Hadoop_map-reduce-streaming
Math stats - mathstats.sh <hdfs input file/folder> <hdfs output folder>-  From the numeric data files given as the path on the command-line (such as  /data/numbers or /data/numbers/small.txt), the output file should contain the count (number of numbers seen), sum of all numbers in the files, and the count of prime numbers in the files.  Answers must be exact.

example command line input and output --

>> ./mathstats.sh /data/numbers/small.txt output
…...
>> hadoop fs -cat /user/<username>/output/part-00000
count  	10
primes  	0
sum  		70909325
