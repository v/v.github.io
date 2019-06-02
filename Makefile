deploy:
	jekyll build
	rsync -r _site/* vv@vverma.net:/var/www/servers/vverma.net
