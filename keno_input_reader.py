import re 

#------Read from KENO input------#
kenoFile = 'input.for'
kenoFileInput = open(kenoFile, 'r+')
i=1
for line in kenoFileInput:
        if "numxcells" in line:
                intOnly= re.sub("\D", " ", line)
                x,y,z = intOnly.split()
        if "xmin" in line:
                intXonly = re.sub("\D"," ",line)
                xmin,xmax = intXonly.split()
        if "ymin" in line:
                intYonly = re.sub("\D"," ", line)
                ymin,ymax = intYonly.split()
        if "zmin" in line:
                intZonly = re.sub("\D", " ", line)
                zmin,zmax = intZonly.split()

print xmin,xmax
print ymin,ymax
print zmin,zmax
