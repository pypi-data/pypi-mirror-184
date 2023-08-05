import socket
import json
import struct
from ga_utils.helper import helper


HOST = "127.0.0.1"  # The server's hostname or IP address
CMD_DUMP_TREE = 300
CMD_GET_POSITION = 103

cmd_tree = json.dumps({
    'cmd': CMD_DUMP_TREE,
    'value': ''
})
def dump_tree(client):
    body_buffer, head_buffer = helper.get_buffer(cmd_tree)
    client.send(head_buffer)
    client.send(body_buffer)

def init_client(port: int, cmd: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, port))

    dump_tree(client)
    data = client.recv(4)
    body_len = struct.unpack('<I', data)[0] 
    msg = client.recv(body_len)
    helper.log(msg)
    print(msg)

    # 通过@id或者@name获取元素的位置信息
    if (cmd == CMD_GET_POSITION):
        tree_data = json.loads(msg.decode('UTF-8'))
        xml = json.loads(helper.xmltojson(tree_data['data']['xml']))
        root = xml['AbstractRoot']
        child = 'GameObject'
        attr = '@id'
        isNumber = True
        if 'UWidget' in root:
            child = 'UWidget'
            attr = '@name'
            isNumber = False

        ids = helper.getIds(root, child, attr)
        cmd_position = json.dumps({
            'cmd': CMD_GET_POSITION,
            'value': helper.handleIds(ids, isNumber)
        })
        body_buffer, head_buffer = helper.get_buffer(cmd_position)
        client.send(head_buffer)
        client.send(body_buffer)
        data = client.recv(4)
        body_len = struct.unpack('<I', data)[0] 
        msg = client.recv(body_len)
        helper.log(msg)
        print(msg)
    






