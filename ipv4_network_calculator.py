import re
from sys import argv

class Ipv4NetworkCalculator():
    def __init__(self, ip='', prefixo='', mascara='', rede='', broadcast='', numero_ips=''):
        self.ip = ip
        self.prefixo = prefixo
        self.mascara = mascara
        self.rede = rede
        self.broadcast = broadcast
        self.numero_ips = numero_ips
        
        if ip == '':
            raise ValueError("Você deve enviar o IP")
        
        # Checa se o IP tem prefixo
        self.check_ip_prefix()
        
        # Checa se é um IP Válido
        self.check_is_ip()
        
        # Checa se foi passado um Prefixo ou Mascara
        if self.prefixo == '' and self.mascara == '':
            raise ValueError('Você tem que passar um prefixo ou uma máscara de rede.')
        
        # Vai converter o IP de decimal para binário
        self.convert_ip_to_bin()
        
        # Converte a máscara para binário, e faz transforma na notação CIDR
        if self.mascara:
            self.mascara_bin = self.convert_ip_to_bin(ip=self.mascara)
            self.prefixo_da_mascara()

        # Quantidade de IPs
        self.numero_de_ips()
        
        # Define o Broadcast
        self.set_rede_broadcast()

        # Mascara do prefixo
        self.mascara_do_prefixo()
        
        # Mostra o resultado final
        self.get_all()

    def prefixo_da_mascara(self):
        mascara_bin = self.mascara_bin.replace('.', '')
        count = 0

        for bit in mascara_bin:
            if bit == '1':
                count += 1
        
        self.prefixo = count
    
    def mascara_do_prefixo(self):
        mascara_bin = ''

        for i in range(32):
            if i < int(self.prefixo):
                mascara_bin += '1'
            else:
                mascara_bin += '0'
        
        mascara_dec = self.convert_ip_to_dec(ip=mascara_bin)
        self.mascara = mascara_dec

    def check_ip_prefix(self):
        regex = re.compile('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2}$')
        if not regex.search(self.ip):
            return 
        
        divide_ip = self.ip.split('/')
        self.ip = divide_ip[0]
        self.prefixo = divide_ip[1]
    
    def check_is_ip(self):
        regex_ip = re.compile('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')

        if not regex_ip.search(self.ip):
            raise ValueError(self.ip + " Não é um IP válido!")
    
    def convert_ip_to_bin(self, ip=''):
        if not ip:
            ip = self.ip

        bloco_ip = ip.split('.')
        ip_bin = []

        for bloco in bloco_ip:
            binario = bin(int(bloco))
            binario = binario[2:].zfill(8)
            ip_bin.append(binario)

        ip_bin = '.'.join(ip_bin)
        return ip_bin
    
    def convert_ip_to_dec(self, ip=''):
        novo_ip = str(int(ip[0:8], 2)) + '.' + str(int(ip[8:16], 2)) + '.' + str(int(ip[16:24], 2)) + '.' + str(int(ip[24:32], 2)) 
        
        return novo_ip

    def numero_de_ips(self):
        host_bits = 32 - int(self.prefixo)
        self.numero_ips = 2 ** host_bits
    
    def set_rede_broadcast(self):
        ip_bin = self.convert_ip_to_bin(ip=self.ip)
        ip_bin = ip_bin.replace('.', '')
        
        rede = ''
        broadcast = ''

        for conta, bit in enumerate(ip_bin):
            if conta < int(self.prefixo):
                rede += str(bit)
                broadcast += str(bit)
            else:
                rede += '0'
                broadcast += '1'
        
        self.rede = self.convert_ip_to_dec(rede)
        self.broadcast = self.convert_ip_to_dec(broadcast)
        
    def get_all(self):
        print (f'IP: {self.ip}\nPrefixo: {self.prefixo}\nMáscara de Sub-rede: {self.mascara}\nRede: {self.rede}\nBroadcast: {self.broadcast}\nNúmero de IPs: {self.numero_ips}')

if __name__ == '__main__':
    # Verifica se foi passado o IP
    try:
        ip = argv[1]
    except:
        print ('Modo de uso: ./ipv4_network_calculator.py [IP/PREFIXO] [MASCARA]')
        exit(1)

    # Verifica se foi passado a mascara de sub-rede
    try:
        mascara = argv[2]
        ipv4 = Ipv4NetworkCalculator(ip=ip, mascara=mascara)
    except:
        ipv4 = Ipv4NetworkCalculator(ip=ip)
