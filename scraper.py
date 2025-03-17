from bs4 import BeautifulSoup
import csv

# Load the local HTML file
with open("/Users/anjalisingh/Desktop/python/test.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find all business listings
listings = soup.find_all("div", class_="listing")

# Save to CSV
with open("my_leads.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Business Name", "Email"])

    for listing in listings:
        name_tag = listing.find("h2")
        name = name_tag.text if name_tag else "Not Found"

        email_tag = listing.find("a", href=True)
        email = "Not Found"
        if email_tag and "mailto:" in email_tag["href"]:
            email = email_tag["href"].replace("mailto:", "")

        writer.writerow([name, email])
        print(f"Saved: {name} - {email}")

print("Done! Check my_leads.csv.")