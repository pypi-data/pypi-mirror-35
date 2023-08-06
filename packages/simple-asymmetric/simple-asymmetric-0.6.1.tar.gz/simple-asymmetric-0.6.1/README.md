# simple-asymmetric-python

The goal is to create a "developer usable" and highly opinionated crypto library as a wrapper around more trusted libraries (libsodium) in various languages and provide a consistent and fully interoperable api.

Why not just use libsodium? While libsodium is great - it is hard to get started with and the various language bindings are often incompatible and difficult to use.

Libsodium provides good defaults if you already know how encryption works and just aren't sure which defaults to use. simple-asymmetric attempts to provide a easy to use solution for sharing data over an untrusted medium. 
It also saves data as base64 strings to easy storage.
If you need more customization - consider simply using libsodium and refer to this project as an example of using it.

That said for most cases SSL is what you want for sending over the internet. But what if we want to store our messages on an evil server?

Let's say Bob wants to share a message with Alice. Bob needs to store his message on an untrusted server for it to get to Alice.

We can use asymmetric encryption (also known as RSA encryption or Public key encryption) to send a message to someone we never spoke with before over an untrusted medium.
However it is slow and not suitable for long messages.
We can use symmetric encryption (also known as Secret Key encryption) to send messages to anyone who shared the same secret key. It's fast and suitable for long messages.

If we want to send long messages to someone we haven't met before - we can use both!

Let's say Bob wants to send Alice a long message. For Alice to get the message, it must be stored on an evil server that wants to read everyone's data!

```
from simple-asymmetric import Asym

bob = Asym()
alice = Asym()

# Generate key pairs for Bob and for Alice
bob.make_rsa_keys()
alice.make_rsa_keys()

# Generate one secret key for symmetric encryption
bob.make_symmetric_key()

# Send key to alice ༼つ◕_◕ ༽つ
encrypted_symmetric_key = bob.get_encrypted_symmetric_key(alice.get_public_key())
# Maybe encrypted_symmetric_key is saved in a database owned by Evil Server.
# Evil Server is watching encrypted_symmetric_key
# But can't figure out what it is
alice.set_symmetric_key_from_encrypted(encrypted_symmetric_key)

# Now that alice has the secrey key, we can send a long message
ciphertext = bob.encrypt("Do you know what cryptobox means?")
# Evil server is still watching....maybe as bob saves it to that database again

# Alice can decrypt the message. Perhaps this is happening locally and not
# where Evil Server can watch
decrypted_message = alice.decrypt(ciphertext)
print(decrypted_message)
> "Do you know what cryptobox means?"

# Alice can send back data easy now without RSA encryption. She could also choose to generate a new RSA key instead and start over.
ciphertext2 = alice.encrypt("Yes but why is crypto so hard to use?")
```


# Installation

Ensure you have libsodium installed. 
In Ubuntu that would be `apt install libsodium18`

Install simple-asymmetric using pip

`pip install simple-asymmetric`

# Development

## We prefer using docker

1. `docker-compose build`
2. Run unit tests `docker-compose up`
