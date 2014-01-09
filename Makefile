SHELL := /bin/sh

.PHONY: deploy

deploy:
	bash -l -c "cd /var/www/onekloud; source ../env/bin/activate; ./deploy.sh"
