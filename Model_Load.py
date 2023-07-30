import requests
import os


def generate_text(prompt, tokens=200):
    # Generate text using the specified prompt
    request_data = {'prompt': prompt, 'max_new_tokens': tokens}
    response = requests.post(f'http://localhost:5000/api/v1/generate', json=request_data)

    if response.status_code == 200:
        return response.json()['results'][0]['text']

def print_basic_model_info(response):
    # Print basic information about the model
    basic_settings = ['truncation_length', 'instruction_template']
    for setting in basic_settings:
        print(setting, "=", response['result']['shared.settings'][setting])


def get_model_info(request_data):
    # Get information about the model using the API
    response = requests.post(f'http://{HOST}/api/v1/model', json=request_data)
    return response.json()


if __name__ == '__main__':
    # Get all available models
    model_list = get_model_info({'action': 'list'})['result']


    for index , value in enumerate(model_list): 
        print(str(index) + " : " + value)
    user_input = int(input("Enter the number for which model you want to load: "))
    model = model_list[user_input]

    try:
        # Load the model and get more detailed information
        response = get_model_info({'action': 'load', 'model_name': model})
        print("Model " + model + " has been loaded!")

    except Exception as e:
        print(f"Model FAIL Exception: {repr(e)}")