from bs4 import BeautifulSoup
import requests


url = "https://bibs23.github.io/portfolio/"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_text = response.text

    # Now create a BeautifulSoup object
    soup = BeautifulSoup(html_text, 'lxml')
    job = soup.find('div')
   
   
    print(job)

    # Continue with your web scraping code using the 'soup' object
else:
    print(f"Error: {response.status_code}")




