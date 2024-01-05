# APISendr

## Getting Started

Simple terminal program to send and receive requests or responses from APIs or addresses.

## Content

### How to Install

1. you must first clone the [repository](https://github.com/simonriv/APISendr).
2. Open an instance of your installed terminal or windows powershell as administrator and go to the repository you just cloned, then run the installation.ps1 file.
3. then close and reopen the terminal to refresh the environment variables.

If the installation mentions that I can't add the path to the path you will have to do it manually.
Now you can use it using the word apisendr.

### How to Use

using the word `apisendr` you can pass two functions `query` and `file`.

The `query` function will allow you to send a request passing only the `url` and as an optional `authorization` parameter to authenticate with tokens, this function is made specifically for requests with the `get` method that do not need any additional parameters.

```sh
apisendr query --url https://random-data-api.com/api/v2/users --authorization token
```

you can also pass the parameter with the diminutive `-u`, for example:

```sh
apisendr query -u https://random-data-api.com/api/v2/users -a token
```

The `file` function will allow you to send a request passing the `path` of a file in json that contains the necessary data for the request, this function is made for requests with any of the methods, the structure of the json will be like this:

```json
{
    "method":"get",
    "url":"https://random-data-api.com/api/v2/users",
    "body":{"data dictionary"},
    "headers":{"headers dictionary"},
    "authorization":"authentication type and token"
}
```

the terminal instruction would look like this:

```sh
apisendr file --path C:\Users\Public\Documents\request.json
```

the above is just an example the path will vary depending on where you have stored the json.
you can also pass the parameter with the diminutive `-p`, for example:

```sh
apisendr file --p C:\Users\Public\Documents\request.json
```

