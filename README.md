# Ipv4 Network Calculator

Uma simples ferramenta para realizar cálculos de rede. O que essa ferramenta faz:
- Descobre máscara de rede a partir do prefixo informado
- Descobre o prefixo a partir da máscara informada
- Mostra o broadcast daquele IP
- Mostra a quantidade de IPs possiveis para aquela rede

# Modo de uso:
```
$ ./ipv4_network_calculator.py <ip/prefixo> [mascara]
```

Ou

```
$ ./ipv4_network_calculator.py <ip> <mascara>
```

Você pode usar especificando somente o IP com o prefixo e sem a mascara ou também pode especificar somente o IP sem o prefixo e mais a mascara 

OBS: <> é obrigatório e [] é opicional

Ex:
```
$ ./ipv4_network_calculator.py 192.168.2.120/24 
```

```
$ ./ipv4_network_calculator.py 192.168.2.120 255.255.255.0

```
