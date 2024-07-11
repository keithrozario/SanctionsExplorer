import sdn_parser

SDN_URL         = 'https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml'
NONSDN_URL      = 'https://www.treasury.gov/ofac/downloads/sanctions/1.0/cons_advanced.xml'

sdn_parser.parse_to_file('./lists/xmls/sdn_advanced.xml', './lists/jsons/sdn_advanced.json')
sdn_parser.parse_to_file('./lists/xmls/cons_advanced.xml', './lists/jsons/cons_advanced.json')

