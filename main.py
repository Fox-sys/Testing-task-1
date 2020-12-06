import os
import json
import re
from jsonschema import validate, ValidationError


schemas = {} # Подготовка словоря для схем
for i in os.listdir('schema'):
    schemas[f"{i[:-7]}"] = json.load(open(f"schema\\{i}", "r"))
events = [json.load(open(f"event\\{i}", "r")) for i in os.listdir("event")] # создание списка с евентами

open("logs.txt", "w")
logs = open("logs.txt", "a")
for i in events: # Валидация ошибок с их классификацией и логгированием
    try:
        validate(i, schemas[i["event"]])
    except ValidationError as e:
        string = str(re.findall(r'\'[\w]+\'\s', str(e), flags=re.M|re.X)[0]) + "is required \n"
        logs.write(string)
    except TypeError as e:
        logs.write("Empty Pocket \n")
    except KeyError as e:
        logs.write(f"schema with name {e} not found \n")
    except Exception as e :
        logs.write("Unnown Error \n")
logs.close()