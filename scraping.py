import requests
from bs4 import BeautifulSoup
import zipfile
import io
from datetime import datetime

#find zip URL
def get_zip_url():
    webpage_url = 'https://lab.data.ca.gov/dataset/covid-19-hospital-data'
    covid_data = requests.get(webpage_url)
    soup = BeautifulSoup(covid_data.content, 'html.parser')
    downloadable = soup.find_all(attrs={'class': 'exclude-external-link-icon'})
    zip_url = downloadable[0]['href']
    return zip_url

#download and extract CSV
def download_and_extract_csv():
    zip_url = get_zip_url()
    csv_name = 'covid_hospital_data_CA'
    curr_date = datetime.now().date().strftime('%Y-%m-%d')
    updated_csv_name = csv_name + '_' + curr_date
    zip = requests.get(zip_url)
    with io.BytesIO(zip.content) as buffer:
        with zipfile.ZipFile(buffer) as zip_file:
            with zip_file.open('statewide-covid-19-hospital-county-data.csv') as csv_file:
                with open('c:/Users/charl/webscraping/covid/data/' + updated_csv_name + '.csv', 'wb') as output_file:
                    output_file.write(csv_file.read())
    print(curr_date + ': File downloaded')
