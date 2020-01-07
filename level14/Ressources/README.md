# Level14

Premiere étape de recherche

	$ ls -la
	(nothing)

	$ find / -user level13 2> /dev/null | grep -v /proc
	(nothing)

	$ find / -user level13 2> /dev/null
	(nothing)

Il n'y a rien du tout. On comprends vite qu'il va falloir exploiter directement le programme getflag

On va le regarder avec GDB

	$ gdb /bin/getflag
	(gdb) run
	Starting program: /bin/getflag
	You should not reverse this
	[Inferior 1 (process 3871) exited with code 01]

Le reverse avec GDB est protégé...

On desassemble le main pour regarder

	(gdb) disas main
	...
	0x08048989 <+67>:	call   0x8048540 <ptrace@plt>
	...
	0x08048afd <+439>:	call   0x80484b0 <getuid@plt>

Le premier appel systeme est `ptrace`, c'est lui qui bloque le reverse

On peut le contourner avec cette technique https://gist.github.com/poxyran/71a993d292eee10e95b4ff87066ea8f2

Ca va modifier le retour de ptrace

	(gdb) catch syscall ptrace
	(gdb) commands 1
	> set ($eax) = 0
	> continue
	> end

On voit aussi qu'il utilise getuid, surement pour savoir le bon token a donner, on va devoir se faire passer pour flag14

On récupère son id

	$ id flag14
	uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)

Et on va modifier la valeur de retour de getuid avec celui de flag14 comme pour le level13

	(gdb) b getuid
	(gdb) step -> jusqu'au return
	(gdb) print $eax
	$1 = 2014

C'est bien ca

	(gdb) set $eax=3014
	(gdb) step
	Single stepping until exit from function main,
	which has no line number information.
	Check flag.Here is your token : XXXXXXXXXXXXXXXXXXXXXXX

EASY WIN
