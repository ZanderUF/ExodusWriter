import sys
import re
import os
import os.path
import datetime
sys.path.append('/opt/moose/seacas/lib')

from exodus import exodus

timeNow = datetime.datetime.now().time()
#------Read KENO Input file------#
kenoFile = 'input.for'
kenoFileInput = open(kenoFile, 'r+')
for line in kenoFileInput:
        if "numxcells" in line:
                intOnly= re.sub("\D", " ", line)
                x,y,z = intOnly.split()
                xInt = int(x)
                yInt = int(y)
                zInt = int(z)
        if "xmin" in line:
                intXonly = re.sub("\D"," ",line)
                xmin,xmax = intXonly.split()
        if "ymin" in line:
                intYonly = re.sub("\D"," ", line)
                ymin,ymax = intYonly.split()
        if "zmin" in line:
                intZonly = re.sub("\D"," ", line)
                zmin,zmax = intZonly.split()
#------End KENO input reader------#

#------Calculate dimension and total nodes based on input------#
dimension=0
if xInt>0:
        dimension+=1
else:
        xInt = 1
if yInt>0:
        dimension+=1
else:
        yInt = 1
if zInt>0:
        dimension+=1
else:
        zInt = 1
totNodes = xInt*yInt*zInt
#------Create Exodus File------#
fileName = 'test_written-file.e'
if os.path.exists(fileName):
        print 'file exists, deleting it'
        os.remove(fileName)
else:
        print 'creating new mesh file'

#------Define geometry of Mesh------#
titleIn = 'Generic Title'
numDimIn = dimension 
numNodesIn = totNodes  
numElemsIn = 2
numBlocksIn = 2
numNodeSetsIn = 2
numSideSetsIn = 2

#------Construct Mesh Object------#
e = exodus(fileName, mode='w', array_type='numpy',title=titleIn,
           numDims=numDimIn,numNodes=numNodesIn,numElems=numElemsIn,
           numBlocks=numBlocksIn,numNodeSets=numNodeSetsIn,numSideSets=numSideSetsIn,io_size=0)
#------Put QA Records------#
rec1 = ('Python Writer','1.0','date','time')
rec2 = ('Python Writer','1.0','date','time')
rec3 = ('Python Writer','1.0','date','time')
qaRecords = (rec1,rec2,rec3)
e.put_qa_records(qaRecords)

#------Put Coordinate Names------#
if dimension == 1:
        coordinateNames = ['X']
if dimension == 2:
        coordinateNames = ['X','Y']
if dimension == 3:
        coordinateNames = ['X','Y','Z']

e.put_coord_names(coordinateNames)

#------Write Coordinates------#
#xCoord = []
#yCoord = []
#zCoord = []
#e.put_coords(xCoord,yCoord,zCoord)
