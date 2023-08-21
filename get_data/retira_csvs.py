import json

# Carregar a lista de links
lista_de_links = ['https://www.mercadolivre.com.br/mixer-oster-delight-2615-fpsthb2615-vermelho-127v-60-hz-250w/p'
                  '/MLB10399772?pdp_filters=official_store:3049#searchVariation=MLB10399772&position=3&search_layout'
                  '=grid&type=product&tracking_id=d12ec83f-ef66-49cf-b1c9-b30636123d9c',
                  'https://www.mercadolivre.com.br/chaleira-eletrica-britnia-bch02pi-aco-inoxidavel-220v-18l/p'
                  '/MLB13303524?pdp_filters=official_store:3049#searchVariation=MLB13303524&position=16&search_layout'
                  '=grid&type=product&tracking_id=2594e82b-24bb-4057-9f3a-400fdac2fe70',
                  'https://www.mercadolivre.com.br/mixer-britnia-bmx630pi-aco-escovado-e-preto-127v-600w/p'
                  '/MLB17083215?pdp_filters=official_store:1553#searchVariation=MLB17083215&position=25&search_layout'
                  '=grid&type=product&tracking_id=76bd77a3-f71e-4dfe-b46d-7f4a50b90b62',
                  'https://www.mercadolivre.com.br/smart-tv-philco-ptv50rcg70bl-led-4k-50-110v220v/p/MLB18561002'
                  '?pdp_filters=official_store:3049#searchVariation=MLB18561002&position=2&search_layout=grid&type'
                  '=product&tracking_id=1f020ca4-6b94-45b5-9d73-c1c0746fef57',
                  'https://www.mercadolivre.com.br/fone-de-ouvido-in-ear-sony-ex-series-mdr-ex15lp-preto/p/MLB6072242'
                  '?pdp_filters=official_store:3049#searchVariation=MLB6072242&position=48&search_layout=grid&type'
                  '=product&tracking_id=87d718eb-c8f0-4961-a674-01c76af16030',
                  'https://www.mercadolivre.com.br/aquecedor-eletrico-cadence-aqc500-branco-220v/p/MLB15558421'
                  '?pdp_filters=official_store:3049#searchVariation=MLB15558421&position=6&search_layout=grid&type'
                  '=product&tracking_id=d12ec83f-ef66-49cf-b1c9-b30636123d9c',
                  'https://www.mercadolivre.com.br/smart-tv-samsung-bet-m-full-hd-43-110v220v/p/MLB15911487'
                  '?pdp_filters=official_store:1553#searchVariation=MLB15911487&position=6&search_layout=grid&type'
                  '=product&tracking_id=3b58b515-10c2-47b3-a981-46fc12f7bd5b',
                  'https://www.mercadolivre.com.br/liquidificador-britnia-fortis-turbo-blq1300-3-l-chumbo-com-jarra'
                  '-de-acrilico-220v/p/MLB18493163?pdp_filters=official_store:3049#searchVariation=MLB18493163'
                  '&position=21&search_layout=grid&type=product&tracking_id=44addbf3-bb20-45bf-b5ea-b8b51fdb34fb',
                  'https://www.mercadolivre.com.br/no-break-estabilizador-de-tenso-sms-station-ii-1200-27392-1200va'
                  '-entrada-de-115v-127v-e-saida-de-115v-preto/p/MLB14729806?pdp_filters=official_store:3049'
                  '#searchVariation=MLB14729806&position=1&search_layout=grid&type=product&tracking_id=87d718eb-c8f0'
                  '-4961-a674-01c76af16030',
                  'https://www.mercadolivre.com.br/samsung-galaxy-a04s-dual-sim-64-gb-black-4-gb-ram/p/MLB21078575'
                  '?pdp_filters=official_store:1553#searchVariation=MLB21078575&position=35&search_layout=grid&type'
                  '=product&tracking_id=3b58b515-10c2-47b3-a981-46fc12f7bd5b',
                  'https://www.mercadolivre.com.br/cmera-de-seguranca-tp-link-tapo-c200-v1-tapo-smart-com-resoluco-de'
                  '-2mp-viso-nocturna-incluida-branca/p/MLB18593981?pdp_filters=official_store:1553#searchVariation'
                  '=MLB18593981&position=41&search_layout=grid&type=product&tracking_id=3b58b515-10c2-47b3-a981'
                  '-46fc12f7bd5b', 'https://www.mercadolivre.com.br/secador-de-cabelo-philco-ph3700-pink-rosa-127v/p'
                                   '/MLB18705660?pdp_filters=official_store:3049#searchVariation=MLB18705660&position'
                                   '=12&search_layout=grid&type=product&tracking_id=0dc4f28f-8ec6-48c1-b0e4'
                                   '-18ee60cc3c94',
                  'https://www.mercadolivre.com.br/xiaomi-redmi-note-10s-dual-sim-128-gb-onyx-gray-6-gb-ram/p'
                  '/MLB18027052?pdp_filters=official_store:1553#searchVariation=MLB18027052&position=3&search_layout'
                  '=grid&type=product&tracking_id=7d9998eb-3719-4d9b-9398-8689008b19fc',
                  'https://www.mercadolivre.com.br/arrozeira-eletrica-a-vapor-philco-ph10-visor-glass-inox'
                  '-vermelhoprata-220v/p/MLB15571051?pdp_filters=official_store:3049#searchVariation=MLB15571051'
                  '&position=32&search_layout=grid&type=product&tracking_id=0dc4f28f-8ec6-48c1-b0e4-18ee60cc3c94',
                  'https://www.mercadolivre.com.br/lixeira-automatica-com-sensor-de-aproximacao-branca-9l-ei078-cor'
                  '-branco/p/MLB19544463?pdp_filters=official_store:3049#searchVariation=MLB19544463&position=35'
                  '&search_layout=grid&type=product&tracking_id=72b1b923-2e80-4d73-b20e-6fe1aa5664ad',
                  'https://www.mercadolivre.com.br/apple-watch-series-8-gps-caixa-meia-noite-de-aluminio-41-mm'
                  '-pulseira-esportiva-meia-noite-padro/p/MLB19679793?pdp_filters=official_store:1553#searchVariation'
                  '=MLB19679793&position=32&search_layout=grid&type=product&tracking_id=76bd77a3-f71e-4dfe-b46d'
                  '-7f4a50b90b62', 'https://www.mercadolivre.com.br/mixer-britnia-bmx350p-preto-220v-350w/p'
                                   '/MLB18427665?pdp_filters=official_store:3049#searchVariation=MLB18427665&position'
                                   '=19&search_layout=grid&type=product&tracking_id=87d718eb-c8f0-4961-a674'
                                   '-01c76af16030',
                  'https://www.mercadolivre.com.br/monitor-gamer-lg-20mk400h-led-195-preto-100v240v/p/MLB15121865'
                  '?pdp_filters=official_store:1553#searchVariation=MLB15121865&position=43&search_layout=grid&type'
                  '=product&tracking_id=3b58b515-10c2-47b3-a981-46fc12f7bd5b',
                  'https://www.mercadolivre.com.br/fogo-cooktop-gas-philco-cook-chef-5-preto-110v220v/p/MLB12117776'
                  '?pdp_filters=official_store:3049#searchVariation=MLB12117776&position=34&search_layout=grid&type'
                  '=product&tracking_id=0dc4f28f-8ec6-48c1-b0e4-18ee60cc3c94',
                  'https://www.mercadolivre.com.br/smart-tv-lg-ai-thinq-43uq751c0sf-led-4k43-100v240v/p/MLB19625084'
                  '?pdp_filters=official_store:1553#searchVariation=MLB19625084&position=37&search_layout=grid&type'
                  '=product&tracking_id=3b58b515-10c2-47b3-a981-46fc12f7bd5b',
                  'https://www.mercadolivre.com.br/liquidificador-philco-ph1200-3-l-preto-com-jarra-de-acrilico-220v'
                  '/p/MLB12358569?pdp_filters=official_store:3049#searchVariation=MLB12358569&position=33'
                  '&search_layout=grid&type=product&tracking_id=87d718eb-c8f0-4961-a674-01c76af16030',
                  'https://www.mercadolivre.com.br/samsung-galaxy-watch5-bt-40mm-cinza-escuro-cor-da-caixa-cinza'
                  '-escuro-cor-da-pulseira-cinza-escuro-cor-do-bisel-cinza-escuro/p/MLB19930564?pdp_filters'
                  '=official_store:1553#searchVariation=MLB19930564&position=4&search_layout=grid&type=product'
                  '&tracking_id=7d9998eb-3719-4d9b-9398-8689008b19fc',
                  'https://www.mercadolivre.com.br/cooktop-de-induco-philco-smart-chef-pct01-preto-127v/p/MLB15818170'
                  '?pdp_filters=official_store:3049#searchVariation=MLB15818170&position=14&search_layout=grid&type'
                  '=product&tracking_id=93dec6af-0b01-46fa-bb4f-2a75ef5815f7',
                  'https://www.mercadolivre.com.br/smartphone-motorola-moto-e13-cmera-13-mpx-tela-de-65-32gb-ram-4g'
                  '-verde/p/MLB23062116?pdp_filters=official_store:1553#searchVariation=MLB23062116&position=9'
                  '&search_layout=grid&type=product&tracking_id=76bd77a3-f71e-4dfe-b46d-7f4a50b90b62',
                  'https://www.mercadolivre.com.br/aspirador-tambor-electrolux-acqua-power-aqp20-10l-preto-y-laranja'
                  '-127v-60hz/p/MLB6215149?pdp_filters=official_store:1553#searchVariation=MLB6215149&position=21'
                  '&search_layout=grid&type=product&tracking_id=76bd77a3-f71e-4dfe-b46d-7f4a50b90b62',
                  'https://www.mercadolivre.com.br/roteador-repetidor-access-point-intelbras-action-rg-1200-preto'
                  '-100v240v/p/MLB15344291?pdp_filters=official_store:3049#searchVariation=MLB15344291&position=46'
                  '&search_layout=grid&type=product&tracking_id=0dc4f28f-8ec6-48c1-b0e4-18ee60cc3c94',
                  'https://www.mercadolivre.com.br/cafeteira-tres-coracoes-passione-automatica-vermelho-brilhante'
                  '-para-capsulas-monodose-220v/p/MLB18025161?pdp_filters=official_store:1553#searchVariation'
                  '=MLB18025161&position=23&search_layout=grid&type=product&tracking_id=3b58b515-10c2-47b3-a981'
                  '-46fc12f7bd5b', 'https://www.mercadolivre.com.br/barbeador-e-cortador-de-cabelo-philco-body-groom'
                                   '-aqua-preto-azul-e-prateado-110v220v/p/MLB18325196?pdp_filters=official_store'
                                   ':3049#searchVariation=MLB18325196&position=10&search_layout=grid&type=product'
                                   '&tracking_id=1f020ca4-6b94-45b5-9d73-c1c0746fef57',
                  'https://www.mercadolivre.com.br/fone-de-ouvido-over-ear-sem-fio-philco-wave-pfo01b-preto/p'
                  '/MLB15570789?pdp_filters=official_store:3049#searchVariation=MLB15570789&position=25&search_layout'
                  '=grid&type=product&tracking_id=1f020ca4-6b94-45b5-9d73-c1c0746fef57',
                  'https://www.mercadolivre.com.br/kit-de-teclado-e-mouse-microsoft-wired-desktop-600-portugus-brasil'
                  '-de-cor-preto/p/MLB18611638?pdp_filters=official_store:3049#searchVariation=MLB18611638&position'
                  '=17&search_layout=grid&type=product&tracking_id=72b1b923-2e80-4d73-b20e-6fe1aa5664ad',
                  'https://www.mercadolivre.com.br/mixer-electrolux-eib10-preto-127v-60-hz-400w/p/MLB18425326'
                  '?pdp_filters=official_store:1553#searchVariation=MLB18425326&position=25&search_layout=grid&type'
                  '=product&tracking_id=3b58b515-10c2-47b3-a981-46fc12f7bd5b',
                  'https://www.mercadolivre.com.br/motorola-edge-30-neo-dual-sim-256-gb-black-onyx-8-gb-ram/p'
                  '/MLB19781019?pdp_filters=official_store:1553#searchVariation=MLB19781019&position=8&search_layout'
                  '=grid&type=product&tracking_id=499fcb14-f9aa-49c3-bb14-7c23660302e3',
                  'https://www.mercadolivre.com.br/controle-joystick-sem-fio-sony-playstation-dualsense-cfi-zct1-gray'
                  '-camouflage/p/MLB19692998?pdp_filters=official_store:1553#searchVariation=MLB19692998&position=10'
                  '&search_layout=grid&type=product&tracking_id=76bd77a3-f71e-4dfe-b46d-7f4a50b90b62']

# Carregar os produtos do arquivo links.json
with open('links.json', 'r') as json_file:
    produtos = json.load(json_file)

# Filtrar os produtos mantendo apenas aqueles cujos links não estão na lista
produtos_filtrados = [produto for produto in produtos if produto['link'] not in lista_de_links]

# Escrever os produtos filtrados em um novo arquivo JSON
with open('links_filtrados.json', 'w') as json_file:
    json.dump(produtos_filtrados, json_file, indent=4)

print("Arquivo 'links_filtrados.json' gerado com sucesso!")
