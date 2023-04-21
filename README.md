# kula
URL Shortener App for Kula

## Description
URL shortening is an application built to support API functionality to Create, Read and Delete short URLs. 

## Usage

API endpoints for api_url app (Using Postman desktop app preferred):

1. Create Short URL:
- POST /add/
- Request body (JSON): {"url": "<long_url>}
- Response body: {"shortened_url": "http://127.0.0.1:8000/4ce3c9d"}

2. Get Short URL Details:
- GET /list/{shortenedID}
- (Shortened ID is the URL after 127.0.0.1:8000/ and before : in the response body from the add request)

3. Delete Short URL:
- DELETE /delete/{shortenedID}
- Response body: 200 OK


4. OPTIONAL List All
- http://127.0.0.1:8000/listall/

## Screenshots for usage:

1. Create (https://drive.google.com/file/d/1p_rNE3Brn0lYqzpOVQSaqwg2yTifv6ik/view?usp=share_link)
2. Read (https://raw.githubusercontent.com/bitsgoan/kula/master/Screenshot%20from%202023-04-22%2001-26-33.png)
3. Delete (https://drive.google.com/file/d/14qyHf8aULb7BQIOXS1pCu1dqEPZGCyq8/view?usp=share_link)
4. List All (https://drive.google.com/file/d/1p_rNE3Brn0lYqzpOVQSaqwg2yTifv6ik/view?usp=share_link)

## More

The URL shortener works on UUID4 serial generation, and is a 7 character long string. 
