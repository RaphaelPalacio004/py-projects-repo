import requests
import validators
import time


def StatusCode():
    try:
        count = 0
        max = 3
        urlInput = str(input("Enter a url: "))
        response = requests.get(urlInput, verify=True)
        validateUrl = True if validators.url(urlInput) else False
        if validateUrl:
            if response.status_code == 200:
                print(f"Request successful, status code: {response}.")
        elif response.status_code == 404:
            print(f"Request unsuccessful, status code: {response}.")
        elif response.status_code == 503:
            print(
                f"The website's server is temporarily unable to handle your request, usually due to being overloaded or undergoing maintenance, status code: {response}."
            )
        else:
            response.raise_for_status()
        return response.status_code
    except requests.exceptions.SSLError as sslExc:
        while count < max:
            count += 1
            time.sleep(max)
            print(f"Verifying connection / attempting to reconnect to server: {count}")
            time.sleep(1.5)
            if count >= max:
                print(sslExc)
    except Exception as exc:
        print(exc)


StatusCode()
