
import os
import requests
import sys
import urllib.request

class IPFS:
    """
    Source connector for IPFS Source .
    This function is used to initialize a IPFSSource object and is called when creating an instance of this class.
    It takes in a configuration dictionary containing the relevant IPFS link information necessary .

        Configuration parameters in json format:
        - IPFSURL (string): link to fetch data from ipfs source.
              
    """

    def __init__(self, config: dict, clientSelf):
        # self.metadata = None
        # self.dbname = config["dbname"]
        self.fileLocation = config["fileLocation"]
        self.IPFSURL = config["IPFSURL"]
        self.clientSelf = clientSelf
     


    def check(self):
        """
        This check() function is used to check if the url  connection is successful.
        It attempts to connect to the IPFS url provided by user  and prints a success message if successful.
        """
        # print("hytlakn")
        try:
           
            f = requests.get(self.IPFSURL)
            if f.ok :
                self.clientSelf.logInfo(self.clientSelf.step, 'IPFS  connection successful')
                return  f.content
            else :
                self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(f._content)}")
                return f.content
            
        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(e)}")

    # def discover(self):
    #     """
    #     This discover() function is used to discover the tables in the database.
    #     It gets a list of all the tables in the database and returns it.
    #     Returns:
    #         tables: list of all the tables in the database.
    #     """
    #     try:
    #         # get a list of all the tables in the database
    #         tables = self.engine.table_names()
    #         return tables
    #     except Exception as e:
    #         self.clientSelf.logError(self.clientSelf.step, f"Failed to discover the tables in the database: {str(e)}")

    def read(self, query: str = None):
        """
        Read content and store it at temperory location.
        
        """
        try:
            checkfile = self.getRelativeFile(self.fileLocation)
            print(checkfile)
            print(os.path.isdir(checkfile))
            if os.path.isdir(checkfile):
                try:
                    print("khjbk")
                    link =self.IPFSURL
                    r = requests.get(link, allow_redirects=True)
                    print(r.headers.get('content-type'),r.headers.get('filename'))
                   
                    
                    resultFilePath, responseHeaders = urllib.request.urlretrieve(link, checkfile)
                except  Exception as e:
                    self.clientSelf.logError(self.clientSelf.step, f"Failed to load IPFS url provided: {str(e)}")

        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Failed to fetch the data: {str(e)}")

    def getRelativeFile(self, filename):
        # dirname = os.path.dirname(__file__) ## python directory should not be fetched  using __file__
        dirname = sys.path[0] + '/'
        filename = os.path.join(dirname, filename)
        return filename
   
    def write(self, table, data):
        """
        This function is used to write data to the database. It takes in the table object and a list of dictionaries
         containing the data to be written. It then compiles an insert statement with the table object and data and
         executes it in the database.
        """
        try:
           print("write")
        except Exception as e:
            self.clientSelf.logError(self.clientSelf.step, f"Error while inserting data: {str(e)}")

  