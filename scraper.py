from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)

SleepTime = 3
base_url = 'https://www.yellowpages.com/'
driver.get(base_url)
time.sleep(SleepTime)

# Accept cookies
button = driver.find_element(By.CLASS_NAME, "onetrust-close-btn-handler")
button.click()
print('- Cookies Accepted')
time.sleep(SleepTime)

# Scrape the main page for links in the quick-search section
page_content = driver.page_source
soup = BeautifulSoup(page_content, "html.parser")
results = soup.find(id="quick-search")

# Collect category names and URLs
hrefs = []
for tag in results.find_all('a', href=True):
    href = tag.get('href').lstrip("/")
    category_name = tag.get_text(strip=True)
    full_url = urljoin(base_url, href)
    hrefs.append((category_name, full_url))
    print(f"Category Name: {category_name}")
    print(f"Full URL: {full_url}")
    print("-" * 20)

# Write the initial results to a CSV file
csv_file = 'categories_and_links.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Category Name", "Full URL"])
    writer.writerows(hrefs)

print(f"Category data written to {csv_file}")

# navigate to each link, scrape data, and write to a detailed CSV file
details_csv = 'page_details.csv'
with open(details_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Category Name", "Name", "Phone", "Address", "Rating Count", "Open Status", "Review Snippet"])

    # Visit each link and scrape details
    for category_name, link in hrefs:
        driver.get(link)
        time.sleep(SleepTime)

        # Get page content and parse with BeautifulSoup
        page_content = driver.page_source
        soup = BeautifulSoup(page_content, "html.parser")

        # Extract relevant data from the page
        try:
            name = soup.find('a', class_='business-name').span.text
        except AttributeError:
            name = "N/A"

        try:
            categories = [cat.text for cat in soup.select('.categories a')]
        except AttributeError:
            categories = "N/A"

        try:
            phone = soup.find('div', class_='phones').text.strip()
        except AttributeError:
            phone = "N/A"

        try:
            street_address = soup.find('div', class_='street-address').text
            locality = soup.find('div', class_='locality').text
            address = f"{street_address}, {locality}"
        except AttributeError:
            address = "N/A"

        try:
            rating_count = soup.find('span', class_='count').text.strip("()")
        except AttributeError:
            rating_count = "N/A"

        try:
            open_status = soup.find('div', class_='open-status').text.strip()
        except AttributeError:
            open_status = "N/A"

        try:
            review_snippet = soup.find('p', class_='body').text.strip()
        except AttributeError:
            review_snippet = "N/A"

        # Write data to CSV file
        writer.writerow([
            category_name,
            name,
            phone,
            address,
            rating_count,
            open_status,
            review_snippet
        ])

        print(f"Data for {name} written to {details_csv}")


driver.quit()
print(f"Detailed data written to {details_csv}")
