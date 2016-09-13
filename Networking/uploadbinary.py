# uploads file to server using POST
# for PHP use this to receive http://www.w3schools.com/php/php_file_upload.asp *remove image checks, rename 'fileToUpload' to 'file'

import requests

payload = {'foo': 'bar'} # for passing string fields also
path = 'your/file.bin'

url = 'http://localhost/upload.php'
files = {'file': ('filenameifwanttogive.bin', open(path, 'rb'), 'application/octet-stream')}

# do actual request
response = requests.post(url, files=files, data=payload)

print response.text
