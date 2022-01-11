# client

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


# Build docker setup
```
docker build . -t my-app
docker run -d -p 8080:80 my-app
```

We can test docker with command:

```
curl localhost:8080
```
