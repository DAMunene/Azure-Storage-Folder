'''
For a Django application, this python file contains the download_template function that downloads the zip file from the remote URL and returns it as a response. 
This function is used in the download.html template to handle the download of the zip file.
The download_template function takes two arguments: request and template_id.
request is the request object, which is used to handle the download of the zip file.
template_id is the primary key of the template object.
'''
import requests
import certifi # To verify the SSL certificate
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def download_zip(request, id):
    variable = get_object_or_404('your_model_name', pk=id)
    
    if not 'your_remote_url':
        raise Http404("File not found.")
    try:
        # Fetch the file from the remote URL
        response = requests.get('your_remote_url', verify=certifi.where())

        if response.status_code == 200:
            file_name = 'your_file_name.zip'
            response_content = response.content
            response = HttpResponse(response_content, content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
        else:
            messages.error(request, f"Failed to download file: {response.status_code} - {response.reason}")
            return redirect('your_endpoint')

    except requests.exceptions.ConnectionError as e:
        messages.error(request, "There was a connection error. Please try again later.")
        return redirect('your_endpoint')

    except requests.exceptions.Timeout as e:
        messages.error(request, "The request timed out. Please try again later.")
        return redirect('your_endpoint')

    except requests.exceptions.RequestException as e:
        messages.error(request, "An error occurred while trying to download the file. Please try again later.")
        return redirect('your_endpoint')
