<h1>Where I keep my secrets</h1>

A small command line tool, to create, read, and write encrypted files. Perfekt for your collection of hentai tags or for your diary.

<h2>Features/Commands</h2>

- **help** shows all the commands with a description in the command line
- **open \<name> \<password>** decrypts the according file and if there isn't a file with a matching name, it creates one.
- **write** adds text to an opened file and saves it encrypted. You need to have used the open command above
- **exit** closes the programm


<h2>Dependencies</h2>

- **simple-crypt** for the encryption and decryption of your text

Install dependencies in cmd using

``pip install -r requirements.txt``

<h2>License</h2>

This software is published under the [MIT license](LICENSE.txt), meaning free to use, but if you use it, I'd appreciate credit.
