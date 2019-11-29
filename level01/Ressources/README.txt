Qui suis-je? Ou suis-je?
level01@SnowCrash:~$ id
uid=2001(level01) gid=2001(level01) groups=2001(level01),100(users)
level01@SnowCrash:~$ pwd
/home/user/level01
level01@SnowCrash:~$ ls -la
total 12
dr-x------ 1 level01 level01  100 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level01 level01  220 Apr  3  2012 .bash_logout
-r-x------ 1 level01 level01 3518 Aug 30  2015 .bashrc
-r-x------ 1 level01 level01  675 Apr  3  2012 .profile

Mes fichiers? Ses fichiers?
$ find / -user level01
(Rien)
$ find / -user flag01
(Rien)

Il y a rien du tout. Casser le mot de passe?

$ ls -l /etc/shadow
-rw-r----- 1 root shadow 4428 Mar  6  2016 /etc/shadow
(pas les droits)
$ ls -l /etc/passwd
-rw-r--r-- 1 root root 2477 Mar  5  2016 /etc/passwd
(les droits!)
$ cat /etc/passwd
(comme par hasard il y a le mdp hashé dedans pour le user flag01)

Download en local le fichier /etc/passwd
$ scp -P 4242 level01@192.168.1.27:/etc/passwd .

Container Docker Kali linux avec en volume le fichier passwd
$ docker run --rm --privileged -v `pwd`:/Ressources -ti kalilinux/kali-linux-docker /bin/bash
$ apt-get update && apt-get install john -y
$ cd /Ressources
$ john passwd

Password : abcdefg

EASY WIN
