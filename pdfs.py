import os
import requests
from parse_sitemap import parse_sitemap  # Import the parse_sitemap function

def fetch_content(url):
    # Simulate fetching content, replace this with actual code using requests or another library.
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def download_pdf(url, output_folder):
    # Fetch the PDF content using requests or another library.
    pdf_content = fetch_content(url)

    if pdf_content is not None:
        # Derive a valid filename from the URL
        filename = os.path.basename(url)
        filename = "".join(c for c in filename if c.isalnum() or c in ('.', '_', '-'))
        filename = os.path.join(output_folder, f"{filename}.pdf")

        # Save the PDF to a file
        with open(filename, 'wb') as pdf_file:
            pdf_file.write(pdf_content)

        print(f"PDF saved successfully: {filename}")
    else:
        print(f"Failed to fetch PDF content from {url}")

def download_pdfs_from_sitemap(sitemap_path, output_folder):
    # Parse the local sitemap file to get a list of URLs
    urls = parse_sitemap(sitemap_path)

    if urls:
        # Ensure the output folder exists or create it
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Iterate through each URL and download PDFs
        for url in urls:
            download_pdf(url, output_folder)

        print("PDF download completed.")
    else:
        print(f"Failed to parse sitemap from {sitemap_path}")
