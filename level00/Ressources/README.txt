Qui suis-je?
$ id
uid=2000(level00) gid=2000(level00) groups=2000(level00),100(users)

Ou suis-je?
$ pwd; ls -la
/home/user/level00
total 12
dr-xr-x---+ 1 level00 level00  100 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-xr-x---+ 1 level00 level00  220 Apr  3  2012 .bash_logout
-r-xr-x---+ 1 level00 level00 3518 Aug 30  2015 .bashrc
-r-xr-x---+ 1 level00 level00  675 Apr  3  2012 .profile
(Rien d'interessant)

Mes fichiers sur le systeme?
$ find / -user level00
(Rien)

Recherches sur le user que je veux être - flag00
$ ls /home/user/flag00
ls: cannot access /home/user/flag00: No such file or directory
(Pas les droits)
$ find / -user flag00
/usr/sbin/john
/rofs/usr/sbin/john
(Il a 2 fichiers)
$ ls -l /usr/sbin/john; ls -l /rofs/usr/sbin/john
----r--r-- 1 flag00 flag00 15 Mar  5  2016 /usr/sbin/john
----r--r-- 1 flag00 flag00 15 Mar  5  2016 /rofs/usr/sbin/john
(J'ai les droits de lecture dessus)
$ cat /usr/sbin/john
cdiiddwpgswtgt
$ cat /rofs/usr/sbin/john
cdiiddwpgswtgt
(un code de trouvé, passe pas en mot de passe -> a dechiffrer)

https://www.dcode.fr/chiffre-cesar -> tester tous les décalages possibles
Il y en a un qui veut dire quelque chose : nottoohardhere
$ su flag00
password: nottoohardhere

EASY WIN
