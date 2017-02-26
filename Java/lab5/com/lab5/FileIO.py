"""FileIO class"""
class FileIO(object):
    filename = ""
    filedestination = ""
    filecontent = []
    nothing = ""

    def __init__(self, filename):
        self.filename = filename

        # file = open(fileName)
        try:
            file = open(self.filename)
           # print("file opened")

            strfilecontent = file.read()

            self. filecontent = strfilecontent.splitlines()
            file.close()

        except FileIO:
            print(self.filename + " could not be found")


    def readFile(self):
        return self.filecontent


    def writeFile(self, out, argument):
        fileout = open(out, "a")
        self.filedestination = fileout
        self.filecontent = argument
        self.filedestination.write(self.filecontent)
