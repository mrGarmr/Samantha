Build image
```docker build . --platform=linux/amd64 -t hajusag/samantha_telegram:latest```

Docker push on DockerHub

```docker push hajusag/samantha_telegram:latest```


Run container on server

```docker run --name samantha_telegram hajusag/samantha_telegram:latest```