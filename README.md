Attempting to deploy a *dockerized* version of this website.


## Deploy

	# on the dev machine, build the latest image and push it to dockerhub
	docker build -t mvlancellotti/double-vortex .
	docker push mvlancellotti/double-vortex
	# on the prod server, pull the latest image and run it
	docker pull mvlancellotti/double-vortex
	docker run -p 8007:8000 mvlancellotti/double-vortex

and then hit the server's IP address at port 8007.

