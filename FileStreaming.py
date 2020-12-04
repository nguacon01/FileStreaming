import io
import tempfile
import requests
class FileStreaming(object):
    """
    Stream a request and returns a tempfile
    tempfile can be use as a file system
    """
    def __init__(self, url, chunk_size=None):
        self.url = url
        self.chunk_size = 1024*1024 if chunk_size is None else chunk_size # chunk_size by default is 1Mb
        self.tempfile = tempfile.TemporaryFile()
        self.session = requests.Session()
        
    def _loadFile(self, up_to_bytes):
        # open session with 'with'. It will release connection in right way.
        with self.session.get(url=self.url, stream=True) as response:
            # take data from request response by chunks(bytes)
            for chunk in response.iter_content(self.chunk_size):
                if not chunk:
                    raise Exception('Loading fail')
                if up_to_bytes is None:
                    self.tempfile.write(chunk)
                else:
                    current_position = self.tempfile.tell()
                    if current_position > up_to_bytes:
                        break
                    self.tempfile.write(chunk)
        # Move pointer back to start position
        self.tempfile.seek(io.SEEK_SET)
    
    def loadFile(self, up_to_bytes=None):
        self._loadFile(up_to_bytes)
        return self.tempfile
                    
    def read(self, up_to_bytes=None):
        self._loadFile(up_to_bytes)
        return self.tempfile.read(up_to_bytes)
        
    def close(self):
        """
        remove tempfile
        """
        self.tempfile.close()
        
    def __repr__(self):
        with self.session.get(url=self.url, stream=True) as response:
            headers = response.headers
        return "Streaming file is {}Mb".format(round(int(headers['Content-Length']) / (1024*1024)))
    __str__ = __repr__