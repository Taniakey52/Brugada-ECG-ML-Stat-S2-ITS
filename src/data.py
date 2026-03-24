import requests
import zipfile
import os

url = "https://physionet.org/content/brugada-huca/get-zip/1.0.0/"
zip_path = "brugada-huca.zip"
extract_path = "brugada-huca"

# Download file
response = requests.get(url)
with open(zip_path, "wb") as f:
    f.write(response.content)

# Extract zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Cek isi folder
os.listdir(extract_path)

import os
print(os.getcwd())
