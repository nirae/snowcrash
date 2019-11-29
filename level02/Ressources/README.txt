Qui suis-je? Ou suis-je?
$ ls -la
----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap
(Fichier pcap avec les droits)

Download le fichier en local
$ scp -P 4242 level02@192.168.1.27:/home/user/level02/level02.pcap .

Ouvrir dans Wireshark -> Analyser flux TCP
On trouve : "ft_wandr...NDRel.L0L"
En regardant les paquets qui correspondent aux lettres, on voit que les points sont le caractere "\177" qui est "DEL"
On les vire et on del les caracteres avant
"ft_waNDReL0L"
