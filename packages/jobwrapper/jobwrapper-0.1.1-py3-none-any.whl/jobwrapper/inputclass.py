#
#   Class that read an inputfile and store the parameters as attributes.
#   It can then be dumped and read as object
#
#


import os


import json


class inputparams:
    """docstring for inputparams class"""

    def __init__(self, path='./'):

        self._path = path

        self.parameters = {} #dic of the parameters
        self.read_inputfile()



    def getpath(self,path):
        """same function as in other classes, could be refactored"""
        import tkinter
        from tkinter.filedialog import askdirectory
        #get the root path
        if path is '':
            root = tkinter.Tk()
            path = askdirectory(parent=root,title='Select the HDF5 path')
            path=path + '/'
            root.destroy()

        #save the attributes
        self._path = path

    def isdumped(self):
        """just return True or False is the file is already dumped"""
        return os.path.isfile(self._path+"inputparams.txt")

    def read_inputfile(self):
        """Parser of the input file , creating attributes of the class"""

        # dictionary definition to replace
        reps = {'D':'e',
                'd':'e',
                '.TRUE.':'True',
                '.FALSE.':'False',
                '.False.':'False',
                'Xe':'"Xe"',
                'Ar':'"Ar"',
                'FAr':'"FAr"',
                'He':'"He"',
                'Kr':'"Kr"',
                '=':''}

        with open(self._path+"/inputs") as inputfile :
            [self.readinputline(line,reps) for line in inputfile]



    def readinputline(self,line,reps):
        if line[0] is '!':
            #pass a commented line
            pass
        else :
            #parse line with spaces
            try:
                key,val = line.split(maxsplit=1)
            except ValueError:
                print("Error : The line is Empty !!")
                exit()
            #remove unwanted comments
            if len( val.split()) > 1:
                val, __ = val.split(maxsplit = 1)

            #replace Fortran expression to Python
            for old, new in reps.items():
                val = val.replace(old, new )

            #execute line to add attribute to the class
            #print(expression[0]+expression[1])
            try:
                self.parameters[key] = eval(val)
            except SyntaxError:
                print(key,val,line)


    def __str__(self):

        strings= ''
        for key,val in self.parameters.items():
            strings = ''.join([strings,key,' = ',val,'\n'])
        return strings
