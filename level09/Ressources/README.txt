Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-sr-x 1 flag09  level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09  level09   26 Mar  5  2016 token
(un binaire setuid et un fichier token)

$ ./level09
You need to provied only one arg.

$ ./level09 coucou
cpwfsz
$ ./level09 blabla
bmcepf
(un hash?)

$ cat token
f4kmm6p|=�p�n��DB�Du{��

$ ./level09 $(cat token)
f5mpq;v�E��{�{��TS�W�����
(bof)
(le token a ete fait avec ce truc de hash)

$ scp -P 4242 level09@192.168.1.27:/home/user/level09/token .
(download en local le fichier token a dechiffrer)

(Le programme decale chaque caractere du nombre de caractere avant lui)
$ ./level09 1
1
$ ./level09 11
12
$ ./level09 111
123
$ ./level09 1111
1234
$ ./level09 11111
12345
(il faut faire l'inverse)

$ ./script.py $(cat token)
f3iji1ju5yuevaus41q1afiuq

YEY
