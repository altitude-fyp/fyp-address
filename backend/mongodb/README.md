# MongoDB Atlas 

## Connecting via cmd

1. Download MongoDB Shell

For MacOS:
```
brew install mongodb/brew/mongodb-community-shell
```

For Windows: https://downloads.mongodb.org/windows/mongodb-shell-windows-x86_64-4.4.0.zip


2. Test this by typing "mongo" into cmd
3. Let zuolin know so zuolin can whitelist your IP and create db user for you

```
mongo "mongodb+srv://fypaddress.tefd1.mongodb.net/main" --username LZL
```

## Connecting via python

1. pip install pymongo
2. check out connection_example.py