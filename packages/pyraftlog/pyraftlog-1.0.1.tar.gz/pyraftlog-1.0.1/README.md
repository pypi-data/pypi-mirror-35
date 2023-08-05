# PyRaftLog
`pyraftlog` is a RAFT consensus algorithm implementation that provides direct access to the consensus log.

### Create SSL certs (for mock)
The following set of commands (performed in `pyraftlog/certs/`) will create a set a CA and device certificate for running the mock cluster on localhost.
```bash
# Only do once: generate the root CA key:
> openssl genrsa -out ca.key 4096

# Generate the root CA certificate:
## Country Name (2 letter code) []:GB
## State or Province Name (full name) []:.
## Locality Name (eg, city) []:.
## Organization Name (eg, company) []:.
## Organizational Unit Name (eg, section) []:.
## Common Name (eg, fully qualified host name) []:PyRaftLog
## Email Address []:.
> openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 -out ca.pem

# Generate device certificates
# Only do once: generate device key:
> openssl genrsa -out localhost.key 4096

# Generate device certificate signing request:
## Country Name (2 letter code) []:GB
## State or Province Name (full name) []:.
## Locality Name (eg, city) []:.
## Organization Name (eg, company) []:.
## Organizational Unit Name (eg, section) []:.
## Common Name (eg, fully qualified host name) []:localhost
## Email Address []:.
> openssl req -new -key localhost.key -out localhost.csr

# Generate a signed device certificate:
> openssl x509 -req -in localhost.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out localhost.crt -days 500 -sha256
```


### Also See
* [Raft Github](https://raft.github.io/)
* [Raft Paper](https://raft.github.io/raft.pdf)
* [Raft Thesis](https://ramcloud.stanford.edu/~ongaro/thesis.pdf)
* [Raft lecture (Raft user study)](https://www.youtube.com/watch?v=YbZ3zDzDnrw)
* [Raft Optimisations](https://www.cl.cam.ac.uk/~ms705/pub/papers/2015-osr-raft.pdf)