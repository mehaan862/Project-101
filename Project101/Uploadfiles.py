import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '3lMW8xqCSSkAAAAAAAAAAb8HwzpuIORND-pzm6rKKyPbS7zZMg-SCdWD_iSvXt4D'
    transferData = TransferData(access_token)
    
    file_from = 'sample.txt'
    file_to = '/test_dropbox/sample.txt'  # The full path to upload the file to, including the file name


    route='C:\PythonProjects\Projects'
    dropboxPath=os.path.join(route,file_from)

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()