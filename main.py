# Uitleg pip en venv
# Uitleg self-made modules
# Uitleg externe apachelogs module (installatie pip)
# Uitleg pymysql
# Nieuwe user toevoegen mysql met permissies
# Connectie maken met db

from modules import apacheparser as a

con = a.connect('web', '230mod', 'apachelog')
a.write_to_db(con, 'small_apache.log')

    
  