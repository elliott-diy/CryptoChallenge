
## The Challenge
The provided script encrypts a flag using AES-CBC. The encryption key is derived from a set of randomly chosen characters, then hashed with SHA-256. Due to the environment, Python falls back to a cryptographically insecure method of randomness.

Your job is to recover the original flag.
I ran `encrypter.py` sometime within the last hour — April 7th, 2025 @ 5PM PST

## Encrypted Flag
The decrypted flag format is `FLAG{example_flag}` — this should help confirm when you've successfully decrypted it.

The encrypted output below is a hex-encoded ciphertext. The IV is static and defined in the script.

If done correctly, the total keyspace you need to search through should only be about **1 million possibilities**. (According to my napkin math lol, it took about 30s to crack using a modern cpu) 

```c9c1edce1b19489cb527f7714964482703c54809b907be7630a5a6d1e62fc836dcbf1a6826a4a1f0dddd5c68f2e4fe91```

(Yes, the encryption was done using the same version of the script provided. I highly recommend writing your decrypter in **Python 3.5** to match behavior.)

## Docker Usage
Download the attached code and Docker file and run the following commands. This will generate an example encrypted flag and let you explore how the encryption process works. 
```
docker build -t bad-entropy .
docker run --rm bad-entropy
```

##  Files Included `(EntropyLies.zip)`
`encrypter.py` – the vulnerable encryption script

`Dockerfile` – for setting up the Python 3.5 environment and dependencies

`requirements.txt` – for dependencies

## Resources / Hints
https://raw.githubusercontent.com/python/cpython/refs/tags/3.5/Lib/random.py

https://docs.python.org/3.5/library/random.html#random.seed

