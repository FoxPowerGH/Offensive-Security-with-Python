import dns
import dns.resolver

# Dominio a evaluar
DOMINIO_A_EVALUAR = 'google.com'

# Registro A
ansA=(dns.resolver.query(DOMINIO_A_EVALUAR,'A'))
print('   ++++++++++  Registo A ++++++++++    ')
print (ansA.response.to_text(), '\n')

# Registro MX
ansMX=(dns.resolver.query(DOMINIO_A_EVALUAR,'MX'))
print('   ++++++++++  Registo MX ++++++++++    ')
print (ansMX.response.to_text(), '\n')

# Registro NS
ansNS=(dns.resolver.query(DOMINIO_A_EVALUAR,'NS'))
print('   ++++++++++  Registo NS ++++++++++    ')
print (ansNS.response.to_text(), '\n')
