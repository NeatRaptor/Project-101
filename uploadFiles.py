import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.A7MUi7z57g7bevIhKqU30N6BHutasLg9ralUvtt54ZkfSvbg2_8pQyi3n81f-Xb09XMn7DBba45gJPMJeuueGjpois0wOcd4hmqVW7xt_vQE4R1dd1LUylJ75Eac4jPrRHIfGZQ"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter file path to upload to dropbox: ")

    transferData.uploadFiles(file_from, file_to)
    print("File uploaded")

main()