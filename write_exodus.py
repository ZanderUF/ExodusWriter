import sys
import os
import os.path
import datetime
sys.path.append('/opt/moose/seacas/lib')

from exodus import exodus

timeNow = datetime.datetime.now().time()

fileName = 'test_written-file.e'
if os.path.exists(fileName):
        print 'file exists, deleting it'
        os.remove(fileName)
else:
        print 'creating new mesh file'

#------Define geometry of Mesh------#
titleIn = 'Generic Title'
numDimIn = 2
numNodesIn = 8
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
coordinateNames = ['X','Y','Z']
e.put_coord_names(coordinateNames)
