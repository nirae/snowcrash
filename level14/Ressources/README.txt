Qui suis-je? Ou suis-je?
$ ls -la
RIEN

Mes fichiers
$ find / -user level13 2> /dev/null | grep -v /proc
RIEN

Ses fichiers
$ find / -user level13 2> /dev/null
RIEN

Bon bah go exploit /bin/getflag directement

$ gdb /bin/getflag
(gdb) run
Starting program: /bin/getflag
You should not reverse this
[Inferior 1 (process 3871) exited with code 01]
(le reverse est protege)

(gdb) disas main
...
0x08048989 <+67>:	call   0x8048540 <ptrace@plt>
...
0x08048afd <+439>:	call   0x80484b0 <getuid@plt>

(le premier syscall est ptrace, c'est lui qui bloque)

on peut le contourner avec cette technique https://gist.github.com/poxyran/71a993d292eee10e95b4ff87066ea8f2

(gdb) catch syscall ptrace
> commands 1
> set ($eax) = 0
> continue
> end

il utilise getuid pour savoir le bon token a donner, on va devoir se faire passer pour flag14
$ id flag14
uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)

(gdb) b getuid
(gdb) step -> jusqu'au return
(gdb) print $eax
$1 = 2014
(c'est bien ca)
(gdb) set $eax=3014
(gdb) step
Single stepping until exit from function main,
which has no line number information.
Check flag.Here is your token : XXXXXXXXXXXXXXXXXXXXXXX

ET VOILA
