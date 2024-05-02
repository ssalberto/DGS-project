import os
import requests
import gzip

def download_and_extract(url, destination_folder):

    # Full file path
    file_name = "clinvar.vcf"
    file_path = os.path.join(destination_folder, file_name)
    
    # Download the file
    print("Downloading file...")
    response = requests.get(url)
    
    # Check if the download was successful
    if response.status_code == 200:
        # Save the file in the destination folder
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully.")
        
        # Extract the file
        print("Extracting file...")
        with gzip.open(file_path, 'rb') as f_in:
            with open(file_path[:-3], 'wb') as f_out:
                f_out.write(f_in.read())
        print("File extracted successfully.")
        
        # Remove the compressed file
        os.remove(file_path)
        print("Compressed file removed.")
    else:
        print("Error downloading the file:", response.status_code)

if __name__ == "__main__":
    # URL of the file to download
    url_file = "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz"
    
    # Destination folder
    destination_folder = "./files"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Call the function to download and extract the file
    download_and_extract(url_file, destination_folder)
