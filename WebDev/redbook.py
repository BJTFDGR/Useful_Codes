import os
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create an instance of the webdriver
driver = webdriver.Chrome()

# Navigate to the URL of the page you want to scrape
driver.get('https://www.xiaohongshu.com/user/profile/573f8db050c4b41cf6afce10/63eb2a09000000001300e4e1')

# Wait for the elements to be present on the page
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-slide"))
)

# Create a directory to save the images
if not os.path.exists('images'):
    os.mkdir('images')
 
# Loop through the elements and extract the "data-swiper-slide-index" attribute
for element in elements:
    index = element.get_attribute('data-swiper-slide-index')
    print(index)
    style = element.get_attribute('style')
    # Extract the URL from the "background-image" property
    url = style.split('url("')[1].split('");')[0]
    # Print the URL
    print(url)
        # Download the image and save it to the "images" directory    # Modify the URL to request a JPEG image
    url = url.replace('/format/webp', '/format/jpg')
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(index) +'.'
    # Download the image and save it to the "images" directory
    response = requests.get(url)
    with open('images/' + filename + url.split('/')[-1], 'wb') as f:
        f.write(response.content)
