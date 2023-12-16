from parse_sitemap import parse_sitemap
from crawl import crawl_url
from pdfs import download_pdfs_from_sitemap

def main():
    sitemap_path = r'C:\Users\pkanv\OneDrive\Desktop\omg\myenergi_sitemap.xml'
    output_folder_text = "output_text"  # Folder for text files
    output_folder_pdfs = "output_pdfs"  # Folder for PDFs

    # Download PDFs from the sitemap
    download_pdfs_from_sitemap(sitemap_path, output_folder_pdfs)

    # Parse the local sitemap file to get a list of URLs
    urls = parse_sitemap(sitemap_path)

    if urls:
        # Iterate through each URL and crawl the website, saving text files
        for url in urls:
            crawl_url(url, output_folder_text)

        print("Crawling completed.")
    else:
        print(f"Failed to parse sitemap from {sitemap_path}")

if __name__ == "__main__":
    main()


