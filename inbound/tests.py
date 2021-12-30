from django.test import TestCase
import requests

print(requests.post("http://127.0.0.1:8000/api").text)
# Create your tests here.
