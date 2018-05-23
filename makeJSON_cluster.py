from __future__ import division
import os, sys
import csv
import random
from sys import argv

script, filename, algname, run_num, ev_num = argv

c,x,y,z,qc = [], [], [], [], []
with open(filename,'r') as f:
    reader = csv.reader(f,delimiter=' ')
    for row in reader:
        c.append(row[0])
        x.append(row[1])
        y.append(row[2])
        z.append(row[3])
        qc.append(row[4])

totalsize = len(x)
data = [[0 for i in range(6)] for j in range(totalsize)]

maxval = -1
for h in range(0,len(c)):
    if int(c[h]) > maxval:
        maxval = int(c[h])

q = []
for k in range(0,maxval+1):
    q.append(float(random.randint(0,36000)))

for i in range(0,totalsize):
    data[i][0] = x[i]
    data[i][1] = y[i]
    data[i][2] = z[i]
    data[i][3] = qc[i]
    data[i][4] = 1
    data[i][5] = c[i]

output_x = ["%s" % data[k][0] for k in range(len(data))]
new_output_x = '[%s]' % ','.join(map(str,output_x))
output_y = ["%s" % data[k][1] for k in range(len(data))]
new_output_y = '[%s]' % ','.join(map(str,output_y))
output_z = ["%s" % data[k][2] for k in range(len(data))]
new_output_z = '[%s]' % ','.join(map(str,output_z))
output_q = ["%s" % data[k][3] for k in range(len(data))]
new_output_q = '[%s]' % ','.join(map(str,output_q))
output_nq = ["%.1f" % data[k][4] for k in range(len(data))]
new_output_nq = '[%s]' % ','.join(map(str,output_nq))
output_cluster_id = ["%s" % data[k][5] for k in range(len(data))]
new_output_cluster_id = '[%s]' % ','.join(map(str,output_cluster_id))


print "{ \"x\":%s, \"y\":%s, \"z\":%s, \"q\":%s, \"nq\":%s,\"cluster_id\":%s, \"type\":\"%s\", \"runNo\":\"%s\", \"subRunNo\":\"1\", \"eventNo\":\"%s\", \"geom\":\"uboone\" }" % (new_output_x,new_output_y,new_output_z,new_output_q,new_output_nq,new_output_cluster_id,algname,run_num,ev_num)
