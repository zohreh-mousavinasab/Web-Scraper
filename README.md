# Web Scraper

## Technology Stack

* 🔗  **[Selenium WebDriver](https://www.selenium.dev/)** : Automates web interactions for testing and data extraction.
* 🍲  **[BeautifulSoup]()** : Parses HTML and XML documents to efficiently locate and extract specific data.
* 🧰  **[Pandas](https://pandas.pydata.org/)** : Facilitates data analysis and manipulation.
* 🦜  **[Streamlit](https://streamlit.io/)** : Provides a frontend for easy interaction with the scraper.
* 🐋  **[Docker](https://www.docker.com)** : Ensures consistent environments for development and deployment.
* ✅  **[Pytest](https://pytest.org)** : Runs automated tests to ensure quality and stability.

## Project Overview

This project performs automated testing on the [yellowpages.com](https://www.yellowpages.com/) website. It includes a collection of tests that validate various search functionalities, such as:

- Find People
- Restaurants
- Dentists
- Plumbers
- Transfers
- Contractors
- Electricians
- Auto Repair
- Roofing
- Attorneys
- Hotels

The automated tests are structured to ensure the reliability and functionality of the site's search features across different categories.

## Project Features

- **Exportable Results**: Test results are saved and exported as a CSV file, making it easy to analyze and track outcomes.

## Quick Start

### Run the App in Docker Containers

1. Clone the repository and navigate to the root folder:

   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
2. Build and run the Docker container (ensure Docker CLI is installed):

   ```bash
   docker build -t zm-scraper .
   docker run -d -p 8501:8501 --name web-scraper zm-scraper
   ```
3. Verify the container is running:

   ```bash
   docker ps
   ```

   - You should see **web-scraper** in the list if everything is set up correctly.
4. Open the app in your browser at:

   ```plaintext
   http://localhost:8501
   ```

### Run the App Locally (Without Docker)

1. **Install Python 3.12** and ensure it’s accessible from your command line.
2. Clone the repository and navigate to the project folder:

   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```
3. Create and activate a virtual environment:

   - **Windows**:
     ```bash
     python3.12 -m venv .venv
     .\venv\Scripts\activate
     ```
   - **macOS or Linux**:
     ```bash
     python3.12 -m venv .venv
     source ./venv/bin/activate
     ```
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:

   ```bash
   streamlit run app.py
   ```
6. Open the app in your browser at:

   ```plaintext
   http://localhost:8501
   ```

## 📄 Project Structure

- **app.py**: Initiates the Streamlit frontend and web interactions.
- **scraper.py**: The main script for web scraping and testing functionalities.
- **README.md**: Project documentation.
- **requirements.txt**: Lists all necessary packages.
