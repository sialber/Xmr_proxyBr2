#Description

Este é um Stratum Proxy para Monero-pools (RPCv2) usando asynchronous networking escrito em Python Twisted.

# # #

Se você perdeu as conexões com o seu proxy e tem muitos usuários, verifique os limites do seu sistema em /etc/security/limits.conf

A melhor maneira de aumentar os limites de arquivos abertos:

  proxyuser hard nofile 1048576
  
  proxyuser soft nofile 1048576

# # #

** NOTA: ** Este fork ainda está em desenvolvimento. Alguns recursos podem estar com falha. Informe quaisquer características ou problemas encontrados.

#Características

* XMR stratum proxy
* Configuração da Carteira Central, os mineiros não precisam de carteira como nome de usuário
* Apoio a mineração direto para exchange
* Suporte de monitoramento via e-mail
* Bypass worker_id para estatística detalhada e monitoramento de equipamento
* Apenas uma conexão com o pool
* Vardiff Individual para os trabalhadores.

#ToDo

* Failover automatico através de proxy, para mineiros também não suportados (ccminer)

#Configuração

* tudo configurado no arquivo config.py

#Exemplo para mineiros

* ./minerd -a cryptonight -o stratum+tcp://127.0.0.1:8080 -u 123456 -p 1

#Doações 

* Monero/XMR: 49dL5bCSYRH6YxitPseZzc6cKnawcC4Fjjoaf22k8P4TYNoZBWKF3t6jXqrT3anyZ22j7DEE74GkbVcQFyH2nNiC3emV3w

* AEON:       Wmsu2ov3b21gaajQNH1wXfhjCtJpPb8stde3ikYopxFo1fpWJy434PjhFaaEttMUt9c61Em6dP1WeHkyDtyRgWf11Q6PMJjjA

* TRX:        0xbf63ae5d3060a4e73df18b513c3984194908e8c9

#Requerimentos

xmr-proxy-br é gfeito em python. atualmente testado na versão 2.7.3, Mas pode funcionar com outras versões. Os requerimentos para executar este programa são:

* Python 2.7+
* python-twisted
* Pool com suporte para este proxy

#Instalação

* edite o arquivo config.py e executar o xmr-proxy.py

#Contato

* via email sialber@gmail.com.


#Creditos

* Original version by Slush0 (original stratum code)
* More Features added by GeneralFault, Wadee Womersley and Moopless
* Tradução Português/Brasil por Sialber.

#License

* Este software fornece AS-IS sem quaisquer garantias de qualquer tipo.
