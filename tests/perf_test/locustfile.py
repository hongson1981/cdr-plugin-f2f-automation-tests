from locust import HttpUser, task
from codecs import encode
import mimetypes
 
class UserBehavior(HttpUser):
 
    @task(1)    
    def create_post(self):
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('Glasswall-d-FIRST-Technology.pdf')))

        fileType = mimetypes.guess_type('Glasswall-d-FIRST-Technology.pdf')[0] or 'application/octet-stream'
        dataList.append(encode('Content-Type: {}'.format(fileType)))
        dataList.append(encode(''))

        with open("Glasswall-d-FIRST-Technology.pdf", "rb")as f:
            dataList.append(f.read())
        dataList.append(encode('--'+boundary+'--'))
        dataList.append(encode(''))
        body = b'\r\n'.join(dataList)
        payload = body
        headers = {
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary) 
        }
        response = self.client.post("/api/rebuild/file",data= payload, 
            headers=headers, 
            name = "Rebuild a PDF file")
        print(response.status_code)
 
