# FileStreaming
This class helps to stream a file at cloud and return a temporary file in local.
The temp file can be use as file system
Streaming file is read by chunks and can be reviews in case it is a huge file
By default, chunk is 1 Mb (1024*1024 bytes)

ex:
#url of file in cloud or whatever url
url = "https://cloud.seafile.com/seafhttp/files/c9554214-2cf0-4e1c-859e-f81d67493cd1/"

#chunk size is define by user. In case chunk size is not defined, it is 1Mb by default.
chunk_size = 1024 #bytes
#define number of bytes you want to load from file. In case up_to_file is not defined, full file will be loaded
up_to_bytes = 1000 #bytes

stream = FileStreaming(url, chunk_size)

# return file is a tempfile, can be used as file-like object or file system
file = stream.loadFile()
