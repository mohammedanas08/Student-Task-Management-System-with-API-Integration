import requests

def save_to_cloud(task_data):
    """
    Sends manually added data to a cloud API using a POST request.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        # Sending the manual task to the server
        response = requests.post(url, json=task_data, timeout=5)
        if response.status_code == 201: # 201 means 'Created'
            return True
        return False
    except Exception as e:
        print(f"Cloud Save Error: {e}")
        return False
