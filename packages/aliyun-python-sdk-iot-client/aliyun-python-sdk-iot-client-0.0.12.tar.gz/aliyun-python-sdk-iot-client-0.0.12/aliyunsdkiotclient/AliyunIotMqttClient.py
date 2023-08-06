# -*- coding: utf-8 -*-

import sys

import paho.mqtt.client as mqtt
import hashlib
import hmac
import time
import ssl
import os

from .exceptions import SSLError

if sys.version > '3':
    PY3 = True
else:
    PY3 = False

here = os.path.abspath(os.path.dirname(__file__))
default_cert_path = (os.path.join(here, 'data', 'root.cert'))


def get_sort_keys(product_key, device_name, client_id):
    """
    key排序
    :param product_key: 产品key
    :param device_name: 设备名称
    :param client_id: 客户id
    :return:
    """
    ts = str(int(time.time()))
    d = {'productKey': product_key, 'deviceName': device_name,
         'timestamp': ts, 'clientId': client_id}
    sort_d = [(k, d[k]) for k in sorted(d.keys())]

    content = ''
    for i in sort_d:
        content += str(i[0])
        content += str(i[1])

    return content


def get_client_id(client_id, secure_mode=2, sign_method='hmacsha1'):
    """
    获取加密后id
    :param client_id:
    :param secure_mode:
    :param sign_method:
    :return:
    """
    ts = str(int(time.time()))
    return client_id + '|securemode=' + str(secure_mode) + ',signmethod=' + sign_method + ',timestamp=' + ts + '|'


def create_signature(secret_key, text, sign_method='hmacsha1'):
    """
    生成签名
    :param secret_key:
    :param text:
    :param sign_method:
    :return:
    """
    string_to_sign = text.encode('utf-8')
    if PY3:
        string_to_sign = bytes(text, 'utf-8')
    if sign_method == 'hmacsha1':
        hashed = hmac.new(secret_key, string_to_sign, hashlib.sha1)
    elif sign_method == 'hmacmd5':
        hashed = hmac.new(secret_key, string_to_sign, hashlib.md5)
    return hashed.hexdigest().upper()


def getAliyunIotMqttClient(product_key, device_name, device_secret, client_id='iot_client', secure_mode=2,
                           sign_method='hmacsha1', cert_path='root.cer'):
    """
    初始化client
    :param product_key:
    :param device_name:
    :param device_secret:
    :param client_id:
    :param secure_mode:
    :param sign_method:
    :param cert_path:
    :return:
    """
    mqtt_client_id = get_client_id(client_id, secure_mode, sign_method)
    client = AliyunIotMqttClient(mqtt_client_id)
    user_name = device_name + '&' + product_key
    ordered_keys = get_sort_keys(product_key, device_name, client_id)
    password = create_signature(device_secret, ordered_keys)

    if secure_mode == 2:
        if cert_path is None:
            raise SSLError('empty ssl perm path')
        client.tls_set(ca_certs=cert_path, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                       tls_version=ssl.PROTOCOL_TLSv1_1, ciphers=None)
        client.tls_insecure_set(False)

    client.username_pw_set(user_name, password=password)

    return client


class AliyunIotMqttClient(mqtt.Client):
    def __init__(self, *args, **kwargs):
        super(AliyunIotMqttClient, self).__init__(*args, **kwargs)
