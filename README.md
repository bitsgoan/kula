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

1. Create
!
[Create Screenshot](https://github.com/bitsgoan/kula/blob/master/Screenshot%20from%202023-04-22%2001-25-19.png)
