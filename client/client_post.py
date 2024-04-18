import requests

FUNCTION_ENDPOINT = r"https://europe-west2-ce06-training.cloudfunctions.net/rico_final_exercise_function"

# POST request
json_body = {
  "product": {
    "name": "ricos hat 7",
    "description": "a testing hat",
    "cost_manufacture":"27"
  }
}

r = requests.post(FUNCTION_ENDPOINT, json=json_body)

print("--------------------------")
print("Posting a product to our endpoint api, response is:")
print(r.text)
print("--------------------------")

