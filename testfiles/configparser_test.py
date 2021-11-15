import configparser
cfg = configparser.ConfigParser()

cfg.read('/home/pi/interoperabilitaet/config_dateien/benutzer.ini')

benutzer = cfg.get('benutzer1', 'zugang')

cfgfile = open("/home/pi/interoperabilitaet/config_dateien/benutzer.ini", 'w')
cfg.add_section(id)
cfg.set('benutzer1', 'id', 'test')
cfg.set('benutzer1', 'zugang', 'darf rein')
cfg.write(cfgfile)
cfgfile.close()
