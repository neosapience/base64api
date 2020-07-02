name := neosapience/base64api
tag := 0.0.1


.PHONY: build

build:
	@docker build -t ${name}:latest -f docker/Dockerfile .

sh:
	@docker run --rm -it ${name}:latest sh

up:
	@docker-compose up

down:
	@docker-compose down

ps:
	@docker-compose ps

ls:
	@docker images ${name}

test:
	@docker-compose -f docker-compose.yaml -f docker-compose.test.yaml up

push:
	@docker build -t ${name}:${tag} -f docker/Dockerfile .
	@docker push ${name}:${tag}