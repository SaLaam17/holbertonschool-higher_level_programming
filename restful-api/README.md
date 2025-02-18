# RESTful API
## Basics of HTTP/HTTPS
## 1. A brief summary explaining the differences between HTTP and HTTPS :
The Hypertext Transfer Protocol (HTTP) and Hypertext Transfer Protocol Secure (HTTPS)
are protocols that allows web clients (like browsers) to communicate with web servers.
HTTP is human readable and
HTTPS is a secured version of HTTP.

## 2. A depiction or outline of the structure of an HTTP request and response:
**HTTP Request Structure**
1. **Request Line**

**Method**: The HTTP method (e.g., GET, POST, PUT, DELETE)

**URI**: The Uniform Resource Identifier indicating the resource (e.g., /index.html)

**HTTP Version**: The version of HTTP being used (e.g., HTTP/1.1)

`GET /index.html HTTP/1.1`

2. **Headers**

Key-value pairs providing additional information (e.g., Host, User-Agent, Accept)

`Host: www.example.com`
`User-Agent: Mozilla/5.0`
`Accept: text/html`

3. **Blank Line**

A blank line indicating the end of the headers.

4. **Body (Optional)**

The data being sent with the request (e.g., form data for a POST request)

`name=John&age=30`

**HTTP Response Structure**
1. **Status Line**

**HTTP Version**: The version of HTTP being used (e.g., HTTP/1.1)

**Status Code**: The status of the response (e.g., 200, 404, 500)

**Reason Phrase**: A short description of the status (e.g., OK, Not Found, Internal Server Error)

`HTTP/1.1 200 OK`

2. **Headers**

Key-value pairs providing additional information (e.g., Content-Type, Content-Length)

`Content-Type: text/html`
`Content-Length: 1234`

3. **Blank Line**

A blank line indicating the end of the headers.

4. **Body (Optional)**

The actual data being sent in the response (e.g., HTML content, JSON data)

`<html>`
`<body>`
`<h1>Hello, World!</h1>`
`</body>`
`</html>`

**Example Exchange**
**HTTP Request**
`GET /index.html HTTP/1.1`
`Host: www.example.com`
`User-Agent: Mozilla/5.0`
`Accept: text/html`

**HTTP Response**

`HTTP/1.1 200 OK`
`Content-Type: text/html`
`Content-Length: 1234`

`<html>`
`<body>`
`<h1>Hello, World!</h1>`
`</body>`
`</html>`

This outline shows the essential components of an HTTP request and response, highlighting how web clients and servers communicate.

3. Lists of common HTTP methods and status codes with their descriptions and possible use cases. For example:
- Method: GET, Description: Retrieves data, Use case: Fetching a web page or data from an API.
- Status Code: 404, Description: Not Found, Scenario: When a requested page or resource isn’t available on the server.

**Common HTTP Methods**
| Method | Description         | Use Case                                 |
|--------|---------------------|------------------------------------------|
| GET    | Retrieves data      | Fetching a web page or data from an API  |
| POST   | Submits data        | Sending form data to a server            |
| PUT    | Updates data        | Updating an existing resource            |
| DELETE | Deletes data        | Removing a resource                      |
| PATCH  | Partially updates data | Updating part of a resource          |
| HEAD   | Retrieves headers   | Checking headers without fetching the body |
| OPTIONS| Describes options   | Checking supported HTTP methods          |

**Common HTTP Status Codes**
#### 1xx (Informational)
| Status Code | Description                  | Scenario                                        |
|-------------|------------------------------|-------------------------------------------------|
| 100         | Continue                     | Initial part of a request has been received, client may continue |
| 101         | Switching Protocols          | Server is switching protocols as requested by the client |
| 102         | Processing                   | Server has received and is processing the request, but no response is available yet |

#### 2xx (Successful)
| Status Code | Description                  | Scenario                                        |
|-------------|------------------------------|-------------------------------------------------|
| 200         | OK                           | Request succeeded and returned the expected data |
| 201         | Created                      | Resource successfully created (e.g., POST request) |
| 202         | Accepted                     | Request has been accepted for processing, but the processing is not complete |
| 204         | No Content                   | Request succeeded but no content to return      |
| 205         | Reset Content                | Tells the client to reset the document view     |

#### 3xx (Redirection)
| Status Code | Description                  | Scenario                                        |
|-------------|------------------------------|-------------------------------------------------|
| 301         | Moved Permanently            | Resource has been permanently moved to a new URL |
| 302         | Found                        | Resource temporarily located at a different URL |
| 303         | See Other                    | Response can be found under a different URI     |
| 304         | Not Modified                 | Resource has not been modified since last requested |
| 307         | Temporary Redirect           | Resource temporarily located at a different URI, use original method for the new URI |
| 308         | Permanent Redirect           | Resource permanently located at a different URI, use original method for the new URI |

#### 4xx (Client Errors)
| Status Code | Description                  | Scenario                                        |
|-------------|------------------------------|-------------------------------------------------|
| 400         | Bad Request                  | Client sent an invalid request                  |
| 401         | Unauthorized                 | Authentication required or failed               |
| 403         | Forbidden                    | Client does not have permission to access the resource |
| 404         | Not Found                    | Resource not found on the server                |
| 405         | Method Not Allowed           | Request method is not supported for the requested resource |
| 408         | Request Timeout              | Server timed out waiting for the request        |
| 409         | Conflict                     | Request conflicts with the current state of the server |
| 410         | Gone                         | Resource requested is no longer available and will not be available again |
| 418         | I'm a teapot                 | Sent as an April Fool's joke in 1998 (RFC 2324) |
| 429         | Too Many Requests            | Client sent too many requests in a given amount of time |

#### 5xx (Server Errors)
| Status Code | Description                  | Scenario                                        |
|-------------|------------------------------|-------------------------------------------------|
| 500         | Internal Server Error        | Server encountered an error                     |
| 501         | Not Implemented              | Server does not support the functionality required to fulfill the request |
| 502         | Bad Gateway                  | Received an invalid response from the upstream server |
| 503         | Service Unavailable          | Server temporarily unavailable                  |
| 504         | Gateway Timeout              | Did not receive a timely response from the upstream server |
| 505         | HTTP Version Not Supported   | Server does not support the HTTP version used in the request |


## Consume data from an API using command line tools (curl)
