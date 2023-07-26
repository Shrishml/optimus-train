import os 
from azure.storage.blob import BlobServiceClient

class DirectoryClient:
    def __init__(self, connection_string, container_name):
        service_client = BlobServiceClient.from_connection_string(connection_string)
        self.client = service_client.get_container_client(container_name)

    def upload(self, source, dest):
        '''
        Upload a file or directory to a path inside the container
        '''
        if (os.path.isdir(source)):
            self.upload_dir(source, dest)
        else:
            self.upload_file(source, dest)
    def upload_file(self, source, dest):
        '''
        Upload a single file to a path inside the container
        '''
        print(f'Uploading {source} to {dest}')
        with open(source, 'rb') as data:
            self.client.upload_blob(name=dest, data=data)
    def upload_dir(self, source, dest):
        '''
        Upload a directory to a path inside the container
        '''
        prefix = '' if dest == '' else dest + '/'
        prefix += os.path.basename(source) + '/'
        for root, dirs, files in os.walk(source):
            for name in files:
                dir_part = os.path.relpath(root, source)
                dir_part = '' if dir_part == '.' else dir_part + '/'
                file_path = os.path.join(root, name)
                blob_path = prefix + dir_part + name
                self.upload_file(file_path, blob_path)
                
connection_string= "DefaultEndpointsProtocol=https;AccountName=stinnovationcats;AccountKey=s3+dmXrrE5A+0VOeBW7afSsKC+De6zUQR0NMP//F5fC+D44TpFydeyQoJvH6NADTFMLQik3c7B4Q+AStUZ9iZw==;EndpointSuffix=core.windows.net"
dest = "aim_runs"
container_name = "aimlogs"
source = 'aim'
dc = DirectoryClient(connection_string,container_name )
dc.upload_dir(source, dest)

