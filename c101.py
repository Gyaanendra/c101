import dropbox


class Transferdata:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload(self, filefrom, file_to):
        # to upload files to dropbox
        dbx = dropbox.Dropbox(self.access_token)

        with open(filefrom, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token= "u27sif0uNVYAAAAAAAAAAeyid7yFd4gTWly28ksFxHwFYJIcA3bUqYo2nhnV0HYV"
    file = Transferdata(access_token)
    filefrom = "photo.jpg"
    file_to = "/class101/photo.jpg"
    file.upload(filefrom, file_to)


if __name__ == '__main__':
    main()
