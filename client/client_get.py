import requests

FUNCTION_ENDPOINT = r"https://europe-west2-ce06-training.cloudfunctions.net/rico_final_exercise_function"

# GET request
r = requests.get(FUNCTION_ENDPOINT)

print("--------------------------")
print("Sending a GET request, response is:")
print(r.text)
print("--------------------------")
