## Overview
Azure does not have a way to upload a folder or directory to Azure Storage directly. However, you can upload a zip file containing the folder or directory and then download it from Azure Storage. This approach allows you to upload a folder or directory to Azure Storage and download it as a zip file.

## Scenario
You have a folder or directory containing templates that you want to upload to Azure Storage. You want to be able to download the folder or directory as a zip file and extract it on the client side.

## Steps
1. Zip the folder or directory.
2. Upload the zip file to Azure Storage.
3. Download the zip file from Azure Storage and extract it on the client side.  

## Files
- **azure_folder_blobs.py**: This Python script uploads the folder or directory to Azure Storage using the Azure Storage SDK.
- **azure_folder_zip.py**: This Python script zips the folder or directory and uploads it to Azure Storage using the Azure Storage SDK.
- **download_zip.py**: This Python script downloads the zip file from Azure Storage and extracts it on the client side.
- **requirements.txt**: This file contains the required packages for the Python script.

## Prerequisites
- Python 3.x
- Azure Storage SDK
- Azure Storage Account
- Azure Storage Container
- Azure Storage Connection String

## Resources
- [Azure Storage SDK for Python](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)
- [Azure Storage SDK for Java](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-java)
- [Azure Storage SDK for .NET](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-dotnet)
- [Azure Storage SDK for Node.js](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-nodejs)

## Setup
1. Install the required packages using pip. ('pip install -r requirements.txt')
2. Create a connection string for your Azure Storage Account.
3. Create a container in your Azure Storage Account.
4. Create a folder or directory on your local machine.
5. Zip the folder or directory using the Python zipfile module.
6. Upload the zip file to your Azure Storage Account using the Azure Storage SDK.
7. Download the zip file from your Azure Storage Account and extract it on the client side.
