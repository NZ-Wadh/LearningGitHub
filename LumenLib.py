# this file define the class container of a data point in 3D space
import matplotlib.pyplot as plt

class FieldData:

    pointDataList = []
    numNodes = 0
    pointDataListInitilized = False
    
    def __init__(self, fileName, fileIndexes):

        for fileIndex in fileIndexes:
            fullFileName = fileName + str(fileIndex) + '.txt'
            print('full file name is ', fullFileName)
            #self.pointDataList.append(self.readComsolExportedTxt(fullFileName))
            print('Reading file' + fullFileName + '\n')
            self.readComsolExportedTxt(fullFileName)
            self.pointDataListInitilized = True
           


            
    
    def readComsolExportedTxt(self,fullfileName):
        # open txt file
        file_obj = open(fullfileName,'r')
        
        i = 0
        # initialize line counter

        for line in file_obj:

            
                if line[0] == '%':
                    #print('This is a line of comment')
                    pass
                else:
                    PointDataArray = [float(element) for element in line.split()]
                    if not self.pointDataListInitilized:
                        # reading first txt, create PointData list
                        self.pointDataList.append(PointData(PointDataArray[0],PointDataArray[1],PointDataArray[2],PointDataArray[3], \
                            PointDataArray[4],PointDataArray[5],PointDataArray[6]))
                        self.numNodes += 1
                    else:
                        # reading following txt, append data to B and t
                        # append data to the B and T
                        self.pointDataList[i].append(PointDataArray[0],PointDataArray[1],PointDataArray[2],PointDataArray[3], \
                            PointDataArray[4],PointDataArray[5],PointDataArray[6])
                        i += 1
    def printNumNodes(self):

        print('The number of nodes is ', self.numNodes)
    

        
        
class PointData:
    
    
    def __init__(self,xCoor, yCoor, zCoor, Bx, By, Bz, t):
        # contructor by explicit initialization
        self.x = xCoor
        self.y = yCoor
        self.z = zCoor
        self.Bx = [Bx]
        self.By = [By]
        self.Bz = [Bz]
        self.t = [t]
      
        
    def printCoordinate(self):
        print('3D coordinate [X,Y,Z] = ', [self.x,self.y,self.z] )
        
    def printT(self):
        print('Time series is', self.t)
        
    def plotBz(self):
        fz = plt.figure(1)
        plt.plot([ele* 1e6 for ele in self.t],self.Bz)
        plt.xlabel('Time (us)')
        plt.ylabel('Bz (T)')
        plt.title('waveform of Bz')
        fz = plt.show()
    def plotBx(self):
        fx =plt.figure(2)
        plt.plot([ele* 1e6 for ele in self.t],self.Bx)
        plt.xlabel('Time (us)')
        plt.ylabel('Bx (T)')
        plt.title('waveform of Bx')
        fx = plt.show()
    def plotBy(self):
        fy = plt.figure(3)
        plt.plot([ele* 1e6 for ele in self.t],self.By)
        plt.xlabel('Time (us)')
        plt.ylabel('By (T)')
        plt.title('waveform of By')
        fx = plt.show()

    def plotBVec(self):
        fvec = plt.figure(4)
        time = [ele* 1e6 for ele in self.t]
        plt.plot(time,self.Bx, 'b--',time,self.By, 'r--', time,self.Bz, 'g--')
        plt.xlabel('Time (us)')
        plt.ylabel('B (T)')
        plt.legend(['Bx','By','Bz'])
        
        plt.title('waveform of B')
        fvec = plt.show()

    def append(self, xCoorCheck, yCoorCheck, zCoorCheck,BxAPP,ByAPP,BzAPP,tAPP):
        
        # append new data to time series
        # check if the coordinate aggress, if so
        self.Bx.append(BxAPP)
        self.By.append(ByAPP)
        self.Bz.append(BzAPP)
        self.t.append(tAPP)




        

