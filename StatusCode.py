import validators
import time
from loguru import logger


class ValidateStatusCode:
    def __init__(self, count, max_attempt, url_input, fetch_response, is_url):
        self.count = count
        self.max_attempt = max_attempt
        self.url_input = url_input
        self.fetch_response = fetch_response
        self.is_url = is_url

    def StatusCode(self):
        import requests

        try:
            self.count = 0
            self.max_attempt = 3
            self.url_input = str(input("Enter a url: "))
            self.fetch_response = requests.get(self.url_input, verify=True)
            self.is_url = True if validators.url(self.url_input) else False
        except requests.exceptions.MissingSchema:
            return logger.exception(
                "The application encountered a missing schema error."
            )
        except requests.exceptions.SSLError:
            while self.count < self.max_attempt:
                self.count += 1
                time.sleep(self.max_attempt)
                print(
                    f"Verifying connection / attempting to reconnect to server: {self.count}"
                )
            if self.count >= self.max_attempt:
                time.sleep(2.0)
                return logger.exception(
                    "The application encountered a max retry error."
                )

    def __str__(self):
        if self.is_url:
            if self.fetch_response.status_code == 200:
                return f"Request successful, status code: {self.fetch_response}."
            if self.fetch_response.status_code == 404:
                return f"Request unsuccessful, status code: {self.fetch_response}."
            if self.fetch_response.status_code == 503:
                return f"The website's server is temporarily unable to handle your request, usually due to being overloaded or undergoing maintenance, status code: {self.fetch_response}."


Result = ValidateStatusCode(
    count=int, max_attempt=int, url_input="", fetch_response="", is_url=False
)
Result.StatusCode()
print(Result)
