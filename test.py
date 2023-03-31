import requests
from bs4 import BeautifulSoup
import os

# Set the target directory to save the downloaded files
target_dir = r'C:\Users\Klara\Documents\Prace\JRC\Teleworking\2023\SOC_LULUCF'

# Define a function to download the file from the given URL
def download_file(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

# Define the base URL
base_url = 'https://unfccc.int'

# Send a GET request to the target URL and parse the HTML content
response = requests.get('https://unfccc.int/ghg-inventories-annex-i-parties/2022')
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Loop through all links and download the files under links called CRF
for link in links:
    if 'CRF' in link.text:
        # Get the URL of the CRF page
        crf_url = base_url + link.get('href')
        # Send a GET request to the CRF page and parse the HTML content
        crf_response = requests.get(crf_url)
        crf_soup = BeautifulSoup(crf_response.content, 'html.parser')
        # Find the download link on the CRF page
        download_link = crf_soup.find('a', text='Open')
        if download_link is not None:
            # Get the URL of the download link and the file name
            download_url = base_url + download_link.get('href')
            filename = os.path.join(target_dir, download_url.split('/')[-1])
            # Download the file
            download_file(download_url, filename)
            print(f'Downloaded {filename}')
