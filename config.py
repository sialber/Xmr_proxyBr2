# Portas para seus mineiros acessarem, defina IP "0.0.0.0" ou um nome de host se seu proxy estiver na nuvem: tipo "proxy.seuservidor.com"
STRATUM_HOST = "0.0.0.0"
# Statrum Port é a porta que vai usar para seu mineiros acessarem ao proxy pode ser diferente da porta da pool a qual vai se conectar
STRATUM_PORT = 8080

# Endereço da carteira da moeda para onde vai a mineração. Se você minera direto para uma carteira em um site exchange (tipo poloniex, HITBTC),
# talvez precise informar um PAYMENT_ID para esta carteira.
WALLET = '49dL5bCSYRH6YxitPseZzc6cKnawcC4Fjjoaf22k8P4TYNoZBWKF3t6jXqrT3anyZ22j7DEE74GkbVcQFyH2nNiC3emV3we'
# Somente se você usa site de exchange que necessite de PAYMENT_ID.
PAYMENT_ID = ''

# abaixo se a pool permitir estatística individual para cada mineiro assuma True, senão False em ENABLE_WORKER_ID
# em seus mineiros deverá usar números como nome de usuário (usename), sem a informação de wallet/carteira.
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# Em algumas Pools existe a opção de monitorar seus mineiros por email.
# se WORKER_ID estiver como "True", voc pode monitorar seus mineiros/rig separadamente.
MONITORING = True
MONITORING_EMAIL = 'mail@exemplo.com'

# Pool Principal
POOL_HOST = 'xmr-eu.dwarfpool.com'
POOL_PORT = 8050

# Pool Secundária em caso de falha da Principal
POOL_FAILOVER_ENABLE = False
POOL_HOST_FAILOVER = 'xmr-usa.dwarfpool.com'
POOL_PORT_FAILOVER = 8050

# ERROS, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"

# Caso queira ajudar com alguma doação seguem abaixo minha carteira:
# Monero/XMR: 49dL5bCSYRH6YxitPseZzc6cKnawcC4Fjjoaf22k8P4TYNoZBWKF3t6jXqrT3anyZ22j7DEE74GkbVcQFyH2nNiC3emV3w
# AEON:       Wmsu2ov3b21gaajQNH1wXfhjCtJpPb8stde3ikYopxFo1fpWJy434PjhFaaEttMUt9c61Em6dP1WeHkyDtyRgWf11Q6PMJjjA
# TRX:        0xbf63ae5d3060a4e73df18b513c3984194908e8c9
