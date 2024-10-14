import os
from azure.storage.blob import BlobServiceClient

# Azure storage connection string and container reference
storage_connection_string = 'your_connection_string'
blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)

# Create or get a reference to the container you want to upload to
container_id = 'your_container_name'
container_client = blob_service_client.get_container_client(container_id)

# Target directory to upload
target_directory = os.path.join(os.getcwd(), 'your_folder_name e.g. landing/templates')

# Walk through the 'templates' directory and upload files
for dirpath, dirnames, filenames in os.walk(target_directory):
    for file_name in filenames:
        file_path = os.path.join(dirpath, file_name)
        
        # Get the relative path starting from the 'templates' folder
        relative_path = os.path.relpath(file_path, target_directory)

        # Create blob name (use relative path within the container)
        blob_name = os.path.join('your_folder_with_blobs e.g templates', relative_path).replace("\\", "/")  # Ensure forward slashes for blob paths
        
        # Upload the file to Azure Blob Storage
        with open(file_path, 'rb') as data:
            container_client.upload_blob(blob_name, data, overwrite=True)
            print(f"Uploaded {file_name} to blob storage as {blob_name}")

