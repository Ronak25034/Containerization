# Experiment 6: Comparison of Docker Run and Docker Compose
---


## Objective 

To understand and compare:

- Docker Run (Imperative approach)
- Docker Compose (Declarative approach)
- Configuration mapping between Docker Run and Compose
- Resource limit configuration
- Using Dockerfile with Compose
- Multi-stage builds using Compose

---


# PART A - THEORY 

---

## 1. Docker Run (Imperative Approach)

The `docker run` command is used to create and start containers from an image

It requires explicit configuration using command-line flags.

### Common Flags Used

- `-p` -> Port mapping 
- `-v` -> Volume mounting
- `-e` -> Environment variable
- `--network` -> Network configuration 
- `--restart` -> Restart policy 
- `--memory` -> Memory limit 
- `--cpus` -> CPU limit
- `--name` -> Container name

### Example 


```bash
docker run -d \
  --name my-nginx \
  -p 8080:80 \
  -v ./html:/usr/share/nginx/html \
  -e NGINX_HOST=localhost \
  --ret