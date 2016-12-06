#!/bin/env python3
#coding=u8

import sys
import yaml
import os
import time
import urllib
import urllib.parse
import urllib.request

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)

def send_sms(conf, invalid_files):
    invalid_files = list(map(os.path.basename, invalid_files))
    content = \
'''
{} files:
{}
error occurred
'''.format(conf['project_name'], '\n'.join(invalid_files))
    print(content)

    #拼请求
    headers = {
            "Accept" : "application/json",
            "Content-Type" : "application/json; charset=UTF-8" }
    url = "http://club.api.autohome.com.cn/api/sms/send"
    post_data = {
            "_appid" : "test",
            "mobile" : ','.join(map(str, conf['admins'])),
            "message" : content
            }
    post_data = urllib.parse.urlencode(post_data)
    req = urllib.request.Request(url + '?' + post_data, headers = headers)
    print(urllib.request.urlopen(req).read().decode('utf8'))
    

if __name__ == '__main__':
    yaml_conf_name = realdir + '/conf.yaml'
    if len(sys.argv) >= 2:
        yaml_conf_name = sys.argv[1]

    conf = None

    if not os.path.isfile(yaml_conf_name):
        print("{} conf file not exist".format(yaml_conf_name))
        exit(-1)
    #加载配置
    with open(yaml_conf_name) as f:
        conf = yaml.load(f)

    invalid_files = []
    now = time.time()
    time_diff = conf['refresh_time']['days'] * 60 * 60 * 24 + \
                conf['refresh_time']['hour'] * 60 * 60 + \
                conf['refresh_time']['min'] * 60
    #检测文件
    for file in conf['files_path']:
        if not os.path.isfile(file):
            invalid_files += [file]
            continue
        time = os.path.getmtime(file)
        if (now - time) > time_diff:
            invalid_files += [file]
            continue

    #发报警
    if len(invalid_files) > 0:
        send_sms(conf, invalid_files)
    else:
        print('check {} ok'.format(conf['project_name']))
