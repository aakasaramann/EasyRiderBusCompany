import json
from datetime import datetime

test_var1 = '''[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "O",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]'''

test_var2 = '''[
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]'''

user_input = json.loads(input())

bus_id_c, stop_id_c, stop_name_c, next_stop_c, stop_type_c, a_time_c = 0, 0, 0, 0, 0, 0

# for bus in user_json:
#     if not re.match(r"\d{3}", str(bus['bus_id'])):
#         bus_id_c += 1
#
#     if not isinstance(bus['stop_id'], int):
#         stop_id_c += 1
#
#     if not re.match(r"[A-Z].*( Road| Avenue| Boulevard| Street)$", bus['stop_name']):
#         stop_name_c += 1
#
#     if not isinstance(bus['next_stop'], int):
#         next_stop_c += 1
#
#     if not re.match(r"[SOF]?$", bus['stop_type']):
#         stop_type_c += 1
#
#     if not re.match(r"(0[1-9]|1[0-9]|2[0-4]):(0[0-9]|[1-5][0-9]|60)$", bus['a_time']):
#         a_time_c += 1
#
#
# # total_error_c = bus_id_c + stop_id_c + stop_name_c + next_stop_c + stop_type_c + a_time_c
# #
# # # print(f'Format validation: {total_error_c} errors')
# # # print(f'stop_name: {stop_name_c}')
# # # print(f'stop_type: {stop_type_c}')
# # # print(f'a_time: {a_time_c}')

# bus_data = {}
# start_stops, transfer_stops, finish_stops, ondemand_stops = [], [], [], []

# for element in user_input:
#     bus_id = element["bus_id"]
#     if bus_id not in [key for key in bus_data]:
#         bus_data[bus_id] = {}
#         bus_data[bus_id]["number of stops"] = 1
#         bus_data[bus_id]["bus_stop_set"] = []
#         bus_data[bus_id]["bus_stop_set"].append(element["stop_name"])
#         bus_data[bus_id]["bus_type_list"] = []
#         bus_data[bus_id]["bus_type_list"].append(element["stop_type"])
#     else:
#         bus_data[bus_id]["number of stops"] = bus_data[bus_id]["number of stops"] + 1
#         bus_data[bus_id]["bus_type_list"].append(element["stop_type"])
#         bus_data[bus_id]["bus_stop_set"].append(element["stop_name"])
#
#     if element["stop_type"] == 'S':
#         start_stops.append(element["stop_name"])
#     elif element["stop_type"] == 'F':
#         finish_stops.append(element["stop_name"])
#     elif element["stop_type"] == 'O':
#         ondemand_stops.append(element["stop_name"])
#
# k = True
# for bus_line in bus_data:
#     # print(bus_data[bus_line]["bus_stop_set"])
#     if 'S' not in bus_data[bus_line]["bus_type_list"] or 'F' not in bus_data[bus_line]["bus_type_list"]:
#         k = False
#         print(f"There is no start or end stop for the line: {bus_line}.")
#         break
#
# if k:
#     bus_128_stops = set(bus_data[128]["bus_stop_set"])
#     bus_256_stops = set(bus_data[256]["bus_stop_set"])
#     bus_512_stops = set(bus_data[512]["bus_stop_set"])
#
#     print(bus_128_stops, bus_256_stops, bus_512_stops)
#
#     transfer_stops.extend(list(bus_128_stops.intersection(bus_256_stops)))
#     transfer_stops.extend(list(bus_256_stops.intersection(bus_512_stops)))
#     transfer_stops.extend(list(bus_512_stops.intersection(bus_128_stops)))
#     print(f'''Start stops: {len(list(set(start_stops)))} {sorted(list(set(start_stops)))}
# Transfer stops: {len(list(set(transfer_stops)))} {sorted(list(set(transfer_stops)))}
# Finish stops: {len(list(set(finish_stops)))} {sorted(list(set(finish_stops)))}''')

# arrival_test = True
# print("Arrival time test:")
# for element in user_input:
#     bus_id = element["bus_id"]
#     stop_name = element["stop_name"]
#     if bus_id not in [key for key in bus_data]:
#         bus_data[bus_id] = {}
#         bus_data[bus_id]["a_time"] = {}
#         bus_data[bus_id]["a_time"][stop_name] = element["a_time"]
#     else:
#         bus_data[bus_id]["a_time"][stop_name] = element["a_time"]
#
# # print(bus_data)
#
# def check_time(bus_id):
#     temp = list(bus_data[bus_id]['a_time'])
#     try:
#         for element in temp:
#             first = bus_data[bus_id]['a_time'][element]
#             next_element = temp[temp.index(element) + 1]
#             next = bus_data[bus_id]['a_time'][next_element]
#             if datetime.strptime(first, '%H:%M') < datetime.strptime(next, '%H:%M'):
#                 pass
#             else:
#                 print(f"bus_id line {bus_id}: wrong time on station {next_element}")
#                 return False
#     except IndexError:
#         return arrival_test
#
# for key in bus_data:
#     arrival_test = check_time(key)
#
# if arrival_test:
#     print("OK")


bus_stop_data = {}

print("On demand stops test:")
for element in user_input:
    bus_id = element["bus_id"]
    stop_name = element["stop_name"]
    stop_type = element["stop_type"]
    if stop_name not in list(bus_stop_data):
        bus_stop_data[stop_name] = [stop_type]
    else:
        bus_stop_data[stop_name].append(stop_type)

# print(bus_stop_data)
wrong_stop_type = []
for key in bus_stop_data:
    if 'O' in bus_stop_data[key]:
        if len(bus_stop_data[key]) != 1:
            wrong_stop_type.append(key)

if len(wrong_stop_type) == 0:
    print("OK")
else:
    print(f"Wrong stop type: {sorted(wrong_stop_type)}")
