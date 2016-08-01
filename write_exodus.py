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
                xNum = int(x)
                yNum = int(y)
                zNum = int(z)
        if "xmin" in line:
                intXonly = re.sub(r'[^\d-]+'," ",line)
                xmin,xmax = intXonly.split()
                xmin = int(xmin)
                xmax = int(xmax)
        if "ymin" in line:
                intYonly = re.sub(r'[^\d-]+'," ", line)
                ymin,ymax = intYonly.split()
                ymin = int(ymin)
                ymax = int(ymax)
        if "zmin" in line:
                intZonly = re.sub(r'[^\d-]+'," ", line)
                zmin,zmax = intZonly.split()
                zmin = int(zmin)
                zmax = int(zmax)
#------End KENO input reader------#

#------Calculate dimension and total nodes based on input------#
dimension=0
if xNum>0:
        dimension+=1
else:
        xNum = 1
if yNum>0:
        dimension+=1
else:
        yNum = 1
if zNum>0:
        dimension+=1
else:
        zNum = 1
totNodes = xNum*yNum*zNum
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
print 'tot nodes', totNodes
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

#------Function to create a list of evenly spaced coordinates------#
def create_coord(cmin,cmax,cnum):
        absDiff = abs(cmax)+abs(cmin)
        cmin    = float(cmin)
        cmax    = float(cmax)
        absDiff = float(absDiff)
        cnum    = float(cnum)
        interval = absDiff/cnum
        print 'min ', cmin
        print 'max ', cmax
        print 'interval', interval
        coorArray = []
        i=0
        coor = cmin

        if cmin > cmax:
                print 'the xmin cannot be greater than xmax'
#------Create dummy coorindates if min,max == 0 ------#
        if cmin == cmax:
                print 'do nothing' 
        else: 
#------Procede normally and created evenly spaced pts ------#
                coorArray.append(cmin)
                while coor < cmax:
                        coor+=interval
                        coor = round(coor,5) 
                        if coor > cmax:
                                coorArray.append(cmax)
                        else:
                                coorArray.append(coor)
                        i+=1
        return coorArray

#------Put Coordinate Names------#
if dimension == 1:
        coordinateNames = ['X']
        e.put_coord_names(coordinateNames)
if dimension == 2:
        coordinateNames = ['X','Y']
        e.put_coord_names(coordinateNames)
if dimension == 3:
        coordinateNames = ['X','Y','Z']
        e.put_coord_names(coordinateNames)

xCoord = create_coord(xmin,xmax,xNum)
yCoord = create_coord(ymin,ymax,yNum)
zCoord = create_coord(zmin,zmax,zNum)
#print zCoord
e.put_coords(xCoord,yCoord,zCoord)

