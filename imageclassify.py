from aip import AipImageClassify

class ImageClassify:
    def __init__(self):
        self.APP_ID = '23710455'
        self.API_KEY = 'trh4E2jUe8Q27HMmWOrVUqwC'
        self.SECRET_KEY = 'XLsrQ3975FifCkcs19G4zGDe4E8xZCSy'
        
        self.client = AipImageClassify(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        
    def get_file(self, filePath):
        with open(filePath, 'rb') as fp:
            self.file = fp.read()
    
    def get_item(self):
        return self.client.advancedGeneral(self.file)

