# Double Vortex

Double vortex was a programming challenge I did with Andrew Robbins inspired by a [video about vortex rings](https://www.youtube.com/watch?v=72LWr7BU8Ao) by Physics Girl.  We challenged ourselves to build an animation of a toroidal vortex in a day and the result was this [double vortex animation](http://learnnation.org/double-vortex.html).

![](banner.png)


## Deploy Notes

Attempting to deploy a *dockerized* version of this website.

	# on the dev machine, build the latest image and push it to dockerhub
	docker build -t mvlancellotti/double-vortex .
	docker push mvlancellotti/double-vortex
	# on the prod server, pull the latest image and run it
	docker pull mvlancellotti/double-vortex
	docker run -p 8007:8000 mvlancellotti/double-vortex

and then hit the server's IP address at port 8007.

