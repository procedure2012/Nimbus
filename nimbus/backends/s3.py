class S3Backend:
    def upload(self, key, data):
    # TODO: use multipart upload for large objects
    # TODO: add server-side encryption headers
        pass

    def download(self, key):
    # TODO: support ranged/partial downloads
        return b''
