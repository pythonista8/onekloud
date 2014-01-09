SHELL := /bin/sh

.PHONY: deploy

deploy:
	bash -ex /var/www/onekloud/deploy.sh
