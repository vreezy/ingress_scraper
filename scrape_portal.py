from ingressAPI import IntelMap, MapTiles
import argparse
import json
from pymysql import connect
import math
import sys
import datetime
from discord_webhook import DiscordWebhook



# Python2 and Python3 compatibility
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser

DEFAULT_CONFIG = "default.ini"

def create_config(config_path):
    """ Parse config. """
    config = dict()
    config_raw = ConfigParser()
    config_raw.read(DEFAULT_CONFIG)
    config_raw.read(config_path)
    config['db_r_host'] = config_raw.get(
        'DB',
        'HOST')
    config['db_r_name'] = config_raw.get(
        'DB',
        'NAME')
    config['db_r_user'] = config_raw.get(
        'DB',
        'USER')
    config['db_r_pass'] = config_raw.get(
        'DB',
        'PASSWORD')
    config['db_r_port'] = config_raw.getint(
        'DB',
        'PORT')
    config['db_r_charset'] = config_raw.get(
        'DB',
        'CHARSET')
    config['db_gym'] = config_raw.get(
        'DB',
        'TABLE_GYM')
    config['db_gym_id'] = config_raw.get(
        'DB',
        'TABLE_GYM_ID')
    config['db_gym_name'] = config_raw.get(
        'DB',
        'TABLE_GYM_NAME')
    config['db_gym_image'] = config_raw.get(
        'DB',
        'TABLE_GYM_IMAGE')
    config['db_ingress'] = config_raw.get(
        'DB',
        'DB_INGRESS')
    config['db_pokestop'] = config_raw.get(
        'DB',
        'TABLE_POKESTOP')
    config['db_pokestop_id'] = config_raw.get(
        'DB',
        'TABLE_POKESTOP_ID')
    config['db_pokestop_name'] = config_raw.get(
        'DB',
        'TABLE_POKESTOP_NAME')
    config['db_pokestop_image'] = config_raw.get(
        'DB',
        'TABLE_POKESTOP_IMAGE')
    config['cookies'] = config_raw.get(
        'Ingress',
        'COOKIES')
    config['encoding'] = config_raw.get(
        'Other',
        'ENCODING')
    config['bbox'] = config_raw.get(
        'Area',
        'BBOX')
    config['whurl'] = config_raw.get(
        'Discord',
        'WEBHOOK')
    config['whenable'] = config_raw.getboolean(
        'Discord',
        'ENABLED_WH')
    return config


def print_configs(config):
    """Print the used config."""
    print("\nFollowing Configs will be used:")
    print("-"*15)    
    print("")
    print("DB:")
    print("Host: {}".format(config['db_r_host']))
    print("Name: {}".format(config['db_r_name']))
    print("User: {}".format(config['db_r_user']))
    print("Password: {}".format(config['db_r_pass']))
    print("Port: {}".format(config['db_r_port']))
    print("Charset: {}".format(config['db_r_charset']))
    print("")
    print("~"*15)

# def get_all_portals(login, tiles):
#     timed_out_items = []
#     portals = []
#     portal_id = []
#     tiles_data = []
#     for idx, tile in enumerate(tiles):
#         iitc_xtile = int( tile[0] )
#         iitc_ytile = int( tile[1] )
        
#         iitc_tile_name  = ('{0}_{1}_{2}_0_8_100').format(zoom, iitc_xtile, iitc_ytile)
#         current_tile = idx+1
#         print(str("{0}/{1} Getting portals from tile : {2}").format(current_tile, total_tiles, iitc_tile_name))
#         try:
#             tiles_data.append(login.get_entities([iitc_tile_name]))
#         except:
#             print(str("Something went wrong while getting portal from tile {0}").format(current_tile) )
#     for tile_data in tiles_data:
#         try:
#             if 'result' in tile_data:
#                 for data in tile_data['result']['map']:
#                     if 'error' in tile_data['result']['map'][data]:
#                         timed_out_items.append(data)
#                     else:
#                         for entry in tile_data['result']['map'][data]['gameEntities']:
#                             #print(entry)
#                             if entry[2][0] == 'p':
#                                 portal_id.append(entry[0])
#                                 portals.append(entry[2])
#                                 #print(entry[0])
#         except:
#             print("could not parse all prtals")
#  return portals, portal_id

if __name__ == "__main__":
    portal_name = 8
    portal_url = 7
    zoom = 15
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--pokestop", action='store_true', help="updates pokestop only")
    parser.add_argument(
        "-g", "--gym", action='store_true', help="updates gyms only")
    parser.add_argument(
        "-all", "--all_poi", action='store_true', help="updates gyms, pokestops and ingress portals")
    parser.add_argument(
        "-i", "--ingress", action='store_true', help="updates ingress portal table")
    parser.add_argument(
        "-c", "--config", default="default.ini", help="Config file to use")
    parser.add_argument(
        "-s", "--cellscore", action='store_true', help="get cellscores")
    args = parser.parse_args()
    config_path = args.config
    config = create_config(config_path)
    print_configs(config)

    print("Initialize/Start DB Session")
   #  mydb_r = connect(
   #      host=config['db_r_host'],
   #      user=config['db_r_user'],
   #      passwd=config['db_r_pass'],
   #      database=config['db_r_name'],
   #      port=config['db_r_port'],
   #      charset=config['db_r_charset'],
   #      autocommit=True)

   # mycursor_r = mydb_r.cursor()
    print("Connection clear")
    updated_gyms = 0
    updated_pokestops = 0

    IngressLogin = IntelMap(config['cookies'])

    if IngressLogin.getCookieStatus() is False:
        if config['whenable']:
            webhook = DiscordWebhook(url=config['whurl'], content='Cookie has expired or not working')
            response = webhook.execute()
        sys.exit()


    if args.cellscore:

        # NR02-GOLF-15 50380447 6940699
        cellscore = IngressLogin.get_region_score_details(50380447,6940699)
        # NR02-GOLF-14 50267618 8696043
        cellscore2 = IngressLogin.get_region_score_details(50267618,8696043)
        # NR02-GOLF-12 2577708 4061932 
        cellscore3 = IngressLogin.get_region_score_details(2577708,4061932)

        # f = open("response1.json", "w")
        # print(cellscore)
        # print(cellscore2)

        with open('response1.json', 'w') as fp:
           json.dump(cellscore, fp)

        with open('response2.json', 'w') as fp:
           json.dump(cellscore2, fp)

        with open('response3.json', 'w') as fp:
           json.dump(cellscore3, fp)

 