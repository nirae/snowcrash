# Level00

Qui suis-je ?

	$ id
	uid=2000(level00) gid=2000(level00) groups=2000(level00),100(users)

Ou suis-je ?

	$ pwd
	/home/user/level00

	$ ls -la
	total 12
	dr-xr-x---+ 1 level00 level00  100 Mar  5  2016 .
	d--x--x--x  1 root    users    340 Aug 30  2015 ..
	-r-xr-x---+ 1 level00 level00  220 Apr  3  2012 .bash_logout
	-r-xr-x---+ 1 level00 level00 3518 Aug 30  2015 .bashrc

Mes fichiers sur le systeme

	$ find / -user level00
	(nothing)

Rien d'interessant dans cette partie

***********************************************************

Recherche sur le user cible : **flag00**

	$ ls /home/user/flag00
	ls: cannot access /home/user/flag00: No such file or directory

	$ find / -user flag00 2> /dev/null
	/usr/sbin/john
	/rofs/usr/sbin/john

	$ ls -l /usr/sbin/john; ls -l /rofs/usr/sbin/john
	----r--r-- 1 flag00 flag00 15 Mar  5  2016 /usr/sbin/john
	----r--r-- 1 flag00 flag00 15 Mar  5  2016 /rofs/usr/sbin/john

	$ cat /usr/sbin/john
	cdiiddwpgswtgt

	$ cat /rofs/usr/sbin/john
	cdiiddwpgswtgt

Un code trouvé, fonctionne pas en password. A déchiffrer

Avec l'outil dcode.fr/chiffre-cesar -> "tester tous les décalages possibles"

Il y en a un qui a un sens : **nottoohardhere**

	$ su flag00
	password: nottoohardhere
	$ getflag

:checkered_flag:
