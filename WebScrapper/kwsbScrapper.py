from bs4 import BeautifulSoup
import requests
downloadUrl = "https://softeng.polito.it/tongji/SE/ex/The-POS-system.pdf"
req = requests.get(downloadUrl)
print(req.headers)

filename = req.url[(downloadUrl.rfind('/')+1):]

print(filename)

with open(filename,'wb') as f:
    for chunk in req.iter_content(chunk_size=34552):
        if chunk:
            f.write(chunk)

# filename = req.url[(downloadUrl.rfind('/')+1):]

# with open(filename,'wb') as f:
#     for chunk in req.iter_content(chunk_size=)
#
# def download_file(url,filename=''):
#     try:
#         if filename:
#             pass
#         else:
#             filename = req.url[(downloadUrl.rfind('/')+1):]
#
#         with requests.get(url) as req:
#
