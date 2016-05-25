#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file map_math.py reduce_math.py -mapper map_math.py -reducer reduce_math.py
