# Portas para seus mineiros acessarem, defina IP "0.0.0.0" ou um nome de host se seu proxy estiver na nuvem: tipo "proxy.seuservidor.com"
STRATUM_HOST = "0.0.0.0"
# Statrum Port � a porta que vai usar para seu mineiros acessarem ao proxy pode ser diferente da porta da pool a qual vai se conectar
STRATUM_PORT = 8080

# Endere�o da carteira da moeda para onde vai a minera��o. Se voc� minera direto para uma carteira em um site exchange (tipo poloniex, HITBTC),
# talvez precise informar um PAYMENT_ID para esta carteira.
WALLET = '49dL5bCSYRH6YxitPseZzc6cKnawcC4Fjjoaf22k8P4TYNoZBWKF3t6jXqrT3anyZ22j7DEE74GkbVcQFyH2nNiC3emV3we'
# Somente se voc� usa site de exchange que necessite de PAYMENT_ID.
PAYMENT_ID = ''

# abaixo se a pool permitir estat�stica individual para cada mineiro assuma True, sen�o False em ENABLE_WORKER_ID
# em seus mineiros dever� usar n�meros como nome de usu�rio (usename), sem a informa��o de wallet/carteira.
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# Em algumas Pools existe a op��o de monitorar seus mineiros por email.
# se WORKER_ID estiver como "True", voc pode monitorar seus mineiros/rig separadamente.
MONITORING = True
MONITORING_EMAIL = 'mail@exemplo.com'

# Pool Principal
POOL_HOST = 'xmr-eu.dwarfpool.com'
POOL_PORT = 8050

# Pool Secund�ria em caso de falha da Principal
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'xmr-usa.dwarfpool.com'
POOL_PORT_FAILOVER = 8050

# ERROS, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"

# Caso queira ajudar com alguma doa��o seguem abaixo minha carteira:
# Monero/XMR: 49dL5bCSYRH6YxitPseZzc6cKnawcC4Fjjoaf22k8P4TYNoZBWKF3t6jXqrT3anyZ22j7DEE74GkbVcQFyH2nNiC3emV3w
# AEON:       Wmsu2ov3b21gaajQNH1wXfhjCtJpPb8stde3ikYopxFo1fpWJy434PjhFaaEttMUt9c61Em6dP1WeHkyDtyRgWf11Q6PMJjjA
# TRX:        0xbf63ae5d3060a4e73df18b513c3984194908e8c9
