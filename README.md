# Snowcrash
## Premier projet sécurité de l'École 42

### Setup de la VM

Réseau Virtualbox bridge pour la facilité pour les levels qui utilisent web ou reseau

#### SSH / SCP

	ssh -p 4242 levelXX@\<ip\>
	scp -P 4242 levelXX@\<ip\>:/path/on/the/vm ./path/on/my/machine

SINON

Réseau Virtualbox NAT -> Redirection de port

- **Nom :** SSH
- **Protocole :** TCP
- **Ip hôte :** 127.0.0.1
- **Port hote :** 4242
- **Ip invitée :** 10.0.2.15 (ip donnée par virtualbox, peut être différente)
- **Port invitée :** 4242 (port ssh de l'iso)

#### SSH / SCP

	ssh -p 4242 levelXX@127.0.0.1
	scp -P 4242 levelXX@127.0.0.1:/path/on/the/vm ./path/on/my/machine

:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:

### !!! SPOIL !!!

- level00 : Déchiffrage code caesar
- level01 : /etc/passwd attack - John The Ripper
- level02 : Analyse de flux TCP sur un fichier pcap - Wireshark
- level03 : Modification du PATH - binaire appel 'system'
- level04 : Exploit script perl
- level05 : cron execute tous les binaires d'un dossier
- level06 : 
