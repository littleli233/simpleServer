# simpleServer
A simple server

You can setup a http server by this application easily
## download
you can download the source code or binary file
[download link](https://github.com/littleli233/simpleServer/releases)

## commands
```
usage: server.py [-h] -host HOST -port PORT [-pubkey PUBKEY][-prikey PRIKEY]

SimpleServer

options:

  -h, --help      show this help message and exit
  -host HOST      host
  -port PORT      port
  -pubkey PUBKEY  ssl certificate
  -prikey PRIKEY  ssl private key
  ```
  
 ## config
 simpleServer can route your local file to a url
 
 it will auto route `/` to `index.html`
 
 so you can run a http server very easily
