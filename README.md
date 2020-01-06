# Snowcrash
## Premier projet sécurité de l'École 42

### Setup de la VM

Réseau virtualbox NAT -> Redirection de port

- **Nom :** SSH
- **Protocole :** TCP
- **Ip hôte :** 127.0.0.1
- **Port hote :** 4242
- **Ip invitée :** 10.0.2.15 (ip donnée par virtualbox, peut être différente)
- **Port invitée :** 4242 (port ssh de l'iso)

### SSH / SCP

ssh -p 4242 levelXX@127.0.0.1
scp -P 4242 levelXX@127.0.0.1:/path/on/the/vm ./path/on/my/machine

:warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning: :warning:

### !!! SPOIL !!!

- level00 :
