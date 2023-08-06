bump-upload:
	bumpversion patch
	git push --tags
	git push --all

	$(MAKE) twine

twine:
	rm -f dist/*
	python setup.py sdist
	twine upload dist/*


docker_image_name=duckietown/duckietown-swarm-amd64
docker_image_name_rpi=duckietown/duckietown-swarm-rpi

docker-build-amd64:
	docker build -t $(docker_image_name) -f Dockerfile.x86 .

docker-push-amd64:
	docker push $(docker_image_name)

docker-build-rpi:
	docker build -t $(docker_image_name_rpi) -f Dockerfile.arm .

docker-push-rpi:
	docker push $(docker_image_name_rpi)

build: docker-build-rpi docker-build-amd64
push: docker-push-rpi docker-build-amd64
