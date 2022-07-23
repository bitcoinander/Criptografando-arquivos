# Criptografando-arquivos
Criptografando arquivos com Python. Utilizando o módulo hashlib.

# code 

```

import hashlib
import os

dir = "/home/ander/Documentos/tools/"

for files in os.listdir(dir):
    os.chdir(dir)
    with open(files, 'rb') as rb:
        dados=rb.read()
        cripto = hashlib.sha512(dados).hexdigest()
        new= '(criptografado) ' + os.path.basename(files)
        with open (new, 'wb') as novo:
            novo.write(cripto*0xFF)
            novo.close()
            rb.close()

            os.remove(files)
            
```
