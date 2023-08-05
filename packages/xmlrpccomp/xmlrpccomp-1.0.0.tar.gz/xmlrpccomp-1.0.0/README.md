# xmlrpc comp

xmlrpc python2 and python3

## Usage

server

```
from xmlrpccomp import RpcServer
>>> def hello():
...     return 'hello'
... 
>>> server = RpcServer(('localhost', 5000))
>>> server.register_function(hello, 'hello')
>>> server.serve_forever()
```

client

```
>>> from xmlrpccomp import RpcClient
>>> client = RpcClient('http://localhost:5000')
>>> client.hello()
'hello'
```
