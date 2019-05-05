import sys
import yaml
import requests
print("Python version")
print (sys.version)
stack_name = "API_SHIPYARDMASTER" #"ONLINE_ELASTICDATA"
with open("/home/narendra/Narendra/Client/Test.yml", 'r') as stream:
    try:

        a=yaml.safe_load(stream)
        
        for stackname in a:
          print(stackname)
          for cft_name in a[stackname]:
              if stack_name in cft_name:
                  git_conf_link = cft_name[stack_name]                  
                  for conf_key,conf_value in git_conf_link.items():
                       if ("null" != conf_value):
                           print(conf_key , conf_value)

    except yaml.YAMLError as exc:
        print(exc)
