# Level09

Premiere étape de recherche

	$ ls -la
	-rwsr-sr-x 1 flag09  level09 7640 Mar  5  2016 level09
	----r--r-- 1 flag09  level09   26 Mar  5  2016 token

On trouve un binaire setuid et un fichier token

	$ ./level09
	You need to provied only one arg.

	$ ./level09 coucou
	cpwfsz

	$ ./level09 blabla
	bmcepf

Le programme fait un hash sur le parametre?

	$ cat token
	f4kmm6p|=�p�n��DB�Du{��

Le token a surement été fait avec ce programme de hash

	$ ./level09 $(cat token)
	f5mpq;v�E��{�{��TS�W�����

Rien de bien intéressant...

On va download en local le fichier token à déchiffrer

	$ scp -P 4242 level09@192.168.1.27:/home/user/level09/token .

Étudions un peu mieux le programme de hash

	$ ./level09 1
	1

	$ ./level09 11
	12

	$ ./level09 111
	123

	$ ./level09 1111
	1234

	$ ./level09 11111
	12345

Le programme décale chaque caractere du nombre de caractere avant lui. On va donc devoir faire l'inverse avec notre token

Avec un script python ce sera plus simple

```python
#! /usr/bin/python3

import sys

# on encode la chaine reçue en parametre en utf-8 et errors="surrogateescape" pour eviter les erreurs d'encodage de python "codec can't encode character '\udc82' in position 9: surrogates not allowed"
for i, c in enumerate(sys.argv[1].encode("utf-8", errors="surrogateescape")):
	# end='' supprime le \n a la fin du print
	print(chr(c - i), end='')
print()

```

Equivalent en C

```c
#include <stdio.h>

int main(int ac, char **av) {

        int i = 0;
        char c;
        while (av[1][i] != 0) {
                c = av[1][i];
                printf("%c", (c - i));
                i++;
        }
        printf("\n");
        return 0;
}
```

	$ ./script.py $(cat token)
	XXXXXXXXXXXXXXXXXXXXXXX
