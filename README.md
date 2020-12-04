# FileStreaming
<p>This class helps to stream a file at cloud and return a temporary file in local.</p>
<p>The temp file can be use as file system</p>
<p>Streaming file is read by chunks and can be reviews in case it is a huge file</p>
<p>By default, chunk is 1 Mb (1024*1024 bytes)</p>

<code>
<p>ex:</p>
<p>#url of file in cloud or whatever url</p>
<p>url = "https://cloud.seafile.com/seafhttp/files/c9554214-2cf0-4e1c-859e-f81d67493cd1/"</p>

<p>#chunk size is define by user. In case chunk size is not defined, it is 1Mb by default.</p>
<p>chunk_size = 1024 #bytes</p>
<p>#define number of bytes you want to load from file. In case up_to_file is not defined, full file will be loaded</p>
<p>up_to_bytes = 1000 #bytes</p>

<p>stream = FileStreaming(url, chunk_size)</p>

<p>#return file is a tempfile, can be used as file-like object or file system</p>
<p>file = stream.loadFile()</p>
</code>
