import configparser
cfg = configparser.ConfigParser()

cfg.read('/home/pi/interoperabilitaet/config_dateien/benutzer.ini')

benutzer = cfg.get('benutzer1', 'zugang')
print(benutzer)
'''cfgfile = open("/home/pi/interoperabilitaet/config_dateien/benutzer.ini", 'w')
cfg.add_section('benutzer1')
cfg.set('benutzer1', 'id', 'test')
cfg.set('benutzer1', 'zugang', 'darf rein')
cfg.write(cfgfile)
cfgfile.close()'''
