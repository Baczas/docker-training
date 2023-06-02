#### PRACTICE:

1. **IMAGES AND CONTAINERS:**
    1. Building a single image (dockerfile-1 app-1.py): \
     `docker build -f Dockerfile-1 -t app .`
         1. Image layers: \
         `docker history app`

    1. Building the EU app in Docker: \
	`docker run -e REGION=EU -d --name app-eu -p 5000:5000 app`

    1. Building the NONEU app in Docker (second container with the same image): \
	`docker run -e REGION=NONEU -d --name app-noneu -p 5002:5000 app`


1. **DOCKER COMPOSE:**
    1. Creating the image to be used: \
	`docker build -f Dockerfile-2 -t app-2 .`

    1. Running Docker Compose: \
    `docker compose [-f docker-compose.yaml] up [-d]` \
    or: \
    `docker compose up`

1. **RUNNING, EXPLORING, AND RESTARTING A CONTAINER:**  \
  `docker exec -it app-redis-noneu bash` \
  `top ` \
  `^C` \
  `kill -9 7` \
  `docker ps`

