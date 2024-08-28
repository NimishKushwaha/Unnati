from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)

def scrape_scholarships():
    url = "https://services.india.gov.in/service/listing?cat_id=66&ln=en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    scholarship_entries = soup.find_all("div", class_="edu-lern-con")

    scholarships = []
    for i, scholarship_entry in enumerate(scholarship_entries, 1):
        title = scholarship_entry.find("h3").text.strip()
        link_element = scholarship_entry.find("a")
        link = urljoin(url, link_element["href"]) if link_element and "href" in link_element.attrs else ""
        description_element = scholarship_entry.find("p")
        description = description_element.text.strip() if description_element else "Description not available"

        scholarship_details = f"<span class='scholarship-number'>Scholarship {i}:</span><br><br>" \
                              f"<span class='bold'>Title:</span> {title}<br>" \
                              f"<span class='bold'>Link:</span> <a href='{link}' target='_blank'>{link}</a><br>" \
                              f"<span class='bold'>Description:</span> {description}"

        scholarships.append(scholarship_details)

    return scholarships

@app.route("/")
def index():
    scholarships = scrape_scholarships()
    return render_template("index.html", scholarships=scholarships)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
