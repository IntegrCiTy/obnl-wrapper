import json

from google.protobuf import json_format

from obnl.message.coside.coside_pb2 import SimulationInit, Schedule


def convert_protobuf_to_data(message):
    if type(message) is SimulationInit:
        data = json.loads(json_format.MessageToJson(message, preserving_proto_field_name=True))
        res = dict()
        res['links'] = data['links']
        res['nodes'] = {}
        for node in data['nodes']:
            res['nodes'][node['name']] = {}
            if 'inputs' in node:
                res['nodes'][node['name']]['inputs'] = node['inputs']
            if 'outputs' in node:
                res['nodes'][node['name']]['outputs'] = node['outputs']

        return res
    elif type(message) is Schedule:
        data = json.loads(json_format.MessageToJson(message, preserving_proto_field_name=True))

        res = dict()
        res['simulation_name'] = data["simulation_name"]
        res['steps'] = data["steps"]
        res['schedule'] = list()
        for nodes in data['schedule']:
            res['schedule'].append(nodes['node_names'])

        return res
    else:
        return json.loads(json_format.MessageToJson(message, preserving_proto_field_name=True))
