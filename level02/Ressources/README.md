# Level02

Qui suis-je ? Ou suis-je ?

	$ ls -la
	----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap

***********************************************************

Download le fichier en local

	$ scp -P 4242 level02@127.0.0.1:/home/user/level02/level02.pcap .

On ouvre le fichier pcap dans Wireshark pour l'analyser
Clique sur l'option : Analyser flux TCP

On trouve : "ft_wandr...NDRel.L0L"

En regardant les paquets qui correspondent aux lettres, on voit que les points sont le caractere "\177" qui est "DEL"
On les enlève et on supprime les caracteres avant qui ont donc été DEL

Mot de passe final : "ft_waNDReL0L"

:checkered_flag:
