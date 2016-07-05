import sys
sys.path.append('/opt/moose/seacas/lib')

from exodus import exodus

#------Define geometry of Mesh------#
titleIn = 'Generic Title'
numDimIn = 2
numNodesIn = 8
numElemsIn = 2
numBlocksIn = 2
numNodeSetsIn = 2
numSideSetsIn = 2

#-----Construct Mesh Object --------#
e = exodus('test_from-writer.e', mode='w', array_type='numpy',title=titleIn,
           numDims=numDimIn,numNodes=numNodesIn,numElems=numElemsIn,
           numBlocks=numBlocksIn,numNodeSets=numNodeSetsIn,numSideSets=numSideSetsIn,io_size=0)

