#### PRACTICE:

1. **OBRAZY I KONTENERY:**
    1. Budowa pojedynczego obrazu (dockerfile-1 app-1.py): \
     `docker build -f Dockerfile-1 -t app .`
         1. Warstwy obrazu: \
         `docker history app`

    1. Zbudowanie apki bez -p (brak wyjścia kontenera na swiat): \
	`docker run -e REGION=EU -d --name app-eu -p 5000:5000 app`

    1. Zbudowanie apki w dockerze (ten sam obraz 2-gi kontener): \
	`docker run -e REGION=NONEU -d --name app-noneu -p 5002:5000 app`


1. **DOCKER COMPOSE:**
    1. Tworzymy obraz z którego będziemy korzystać: \
	`docker build -f Dockerfile-2 -t app-2 .`

    1. Uruchamiamy Docker Compose: \
    `docker compose [-f docker-compose.yaml] up [-d]` \
    lub: \
    `docker compose up`

1. **URUCHOMIENIE I EKSLOPARACJA I RESTART KONTENERA:**  \
  &nbsp;&nbsp;&nbsp;&nbsp;`docker exec -it app-redis-noneu bash` \
  &nbsp;&nbsp;&nbsp;&nbsp;`top ` \
  &nbsp;&nbsp;&nbsp;&nbsp;`^C` \
  &nbsp;&nbsp;&nbsp;&nbsp;`kill -9 7` \
  &nbsp;&nbsp;&nbsp;&nbsp;`docker ps`

