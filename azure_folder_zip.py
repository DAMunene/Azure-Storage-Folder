import os
import shutil
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

# Azure storage connection string and container reference
storage_connection_string = 'your_storage_connection_string'
blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)

# Create or get a reference to the container you want to upload to
container_id = 'your_container_name'
container_client = blob_service_client.get_container_client(container_id)

# Target directory to zip and upload
target_directory = os.path.join(os.getcwd(), 'your_folder_name')

# Step 1: Zip the folder
def zip_directory(source_dir, output_filename):
    # Create a zip file from the source_dir
    shutil.make_archive(output_filename, 'zip', source_dir)
    zip_file_path = f"{output_filename}.zip"
    print(f"Folder zipped at: {zip_file_path}")
    return zip_file_path

# Step 2: Upload the zip file to Azure Blob Storage
def upload_zip_to_azure(zip_file_path, container_name, blob_name):
    try:
        # Upload zip file as a blob
        with open(zip_file_path, 'rb') as data:
            container_client.upload_blob(blob_name, data, overwrite=True)
        # Return the blob URL
        blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"
        print(f"Uploaded zip file to blob storage: {blob_url}")
        return blob_url
    except ResourceExistsError:
        print(f"The blob {blob_name} already exists.")
        return None

# Step 3: Define the blob name and zip the target directory
zip_file_name = 'your_zip_file_name'  # You can change the zip file name here
zip_file_path = zip_directory(target_directory, zip_file_name)

# Step 4: Upload the zip file to Azure Blob Storage
blob_name = f'{zip_file_name}.zip'  # The name of the blob in Azure Storage
zip_url = upload_zip_to_azure(zip_file_path, container_id, blob_name)

# Step 5: Clean up the local zip file after upload (optional)
if os.path.exists(zip_file_path):
    os.remove(zip_file_path)
    print(f"Deleted local zip file: {zip_file_path}")

# The final zip file URL is now available in the variable `zip_url`
print(f"Downloadable Zip URL: {zip_url}")
