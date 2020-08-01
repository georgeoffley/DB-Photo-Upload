class Parse:
    
    # Convert image to binary data  
    def ConvertToBin(file):
        with open(file, 'rb') as file:
            binaryData = file.read()
        return binaryData