import requests
from django.shortcuts import render
from django.http import HttpResponse

def get_user_data(request, user_id):
    # Configure the proxy server address
    proxy_server_address = 'http://localhost:8001'

    # Configure the Express API endpoint
    express_api_endpoint = f'{proxy_server_address}/users/{user_id}'

    try:
        # Make a GET request to the Express API via the Python proxy
        response = requests.get(express_api_endpoint)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        user_data = response.json()

        # Render the user data in the Django template
        return render(request, 'user_data.html', {'user_data': user_data})

    except requests.RequestException as e:
        # Handle request exceptions
        return HttpResponse(f'Error fetching user data: {e}', status=500)

    
def user_list(request):
     # Configure the proxy server address
    proxy_server_address = 'http://localhost:8001'

    # Configure the Express API endpoint
    express_api_endpoint = f'{proxy_server_address}/users'

    try:
        # Make a GET request to the Express API via the Python proxy
        response = requests.get(express_api_endpoint)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        users = response.json()

        # Render the user data in the Django template
        return render(request, 'user_list.html', {'user_list': users})

    except requests.RequestException as e:
        # Handle request exceptions
        return HttpResponse(f'Error fetching user data: {e}', status=500)
