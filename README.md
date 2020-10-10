Attempting to deploy a *dockerized* version of this website.


## Deploy

	docker build -t vortex . && docker run -p 8007:8000 vortex

and then hit the server's IP address at port 8007.

