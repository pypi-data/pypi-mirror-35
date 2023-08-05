#!/usr/bin/python
import sys
import json
import argparse
from subprocess import Popen, PIPE
import pandas as pd
import re
import os
import shlex
import sys
from collections import OrderedDict
import csv
import time

if sys.version_info[0] < 3: 
  from StringIO import StringIO
else:
  from io import StringIO


_HASH_PATTERN = re.compile("^\/\w+\/(\w*)")
_TMP_PATH = os.environ.get("HOME")
_MAX_ATTEMPTS = 10
_DELAY = .1


#---------------------------------------------------------------------
def _shell_exec_once(command, cwd=None):
  if cwd:
    proc = Popen(shlex.split(command), stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=cwd)
    stdoutdata, err = proc.communicate()
    return stdoutdata, err
  else:
    proc = Popen(shlex.split(command), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdoutdata, err = proc.communicate()
    return stdoutdata.decode(), err

def _shell_exec(command):
  stdoutdata, err = _shell_exec_once(command)
  for _ in range(_MAX_ATTEMPTS - 1):
    if "error" not in stdoutdata[:15]:
      break
    time.sleep(_DELAY)
    stdoutdata, err = _shell_exec_once(command)
  return stdoutdata

#---------------------------------------------------------------------
def clean_up_files(paths):
  for path in paths:
    cmd = "rm -rf {}".format(path)
    _shell_exec(cmd)

def strip_color(s):
  ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
  return ansi_escape.sub('', s)    
#---------------------------------------------------------------------

def shift_root_down(d):
  keys = list(d.keys())
  if len(keys) > 1:
    print("error: dict must have single root")
  else:
    root = keys[0]
    new_d = d[root]
    new_d['root'] = root
    return new_d

def shift_root_up(d):
  if 'root' not in d:
    print("error: no root key found")
  else:
    root_val = d['root']
    del d['root']
    new_d = {root_val: d}
    return new_d

class QriDataset(object):
  def __init__(self, body, head, name):
    self.body = body
    self.head = head
    self.ds_name = name
  
  def _update_head_from_body(self):
    pass
  
  def save(self, commit_msg, publish=True):
    tmp_body_save_path = os.path.join(_TMP_PATH, "body.json")
    tmp_head_save_path = os.path.join(_TMP_PATH, "head.json") 
    if is_csv(self.head):
      tmp_body_save_path = tmp_body_save_path.replace(".json", ".csv")
    body = self.body
    head = self.head
    head['bodyPath'] = tmp_body_save_path
    name = self.ds_name
    head['name'] = name
    # save body to temp file
    if is_csv(self.head):
      d = body.where((pd.notnull(body)), None).to_csv(tmp_body_save_path, index=False)
    else:
      with open(tmp_body_save_path, "w") as fp:
        d = body.where((pd.notnull(body)), None).to_dict(orient="records")
        json.dump(d, fp, indent=2)
    # save head to temp file
    with open(tmp_head_save_path, "w") as fp:
      json.dump(head, fp, indent=2)
    flags = { "head_path": tmp_head_save_path,
              "commit_msg": commit_msg,
              "name": name,
              "publish": "-p " if publish else "", 
            }

    cmd = "qri save {publish}--file '{head_path}' -t '{commit_msg}' {name}".format(**flags)
    result = _shell_exec(cmd)
    print(result)
    # remove tmp files
    # clean_up_files([tmp_body_save_path, tmp_head_save_path])
    print("dataset saved")

def is_csv(head):
  if 'structure' in head and 'format' in head['structure'] and head['structure']['format'].lower() == "csv":
    return True
  else:
    return False

def convert_csv(body):
  field_names = body[0]
  data = body[1:]
  # print("fieldnames: type: {}, len:{}".format(type(field_names)), len(field_names))
  # print("data: type: {}, len:{}".format(type(data)), len(data))

  new_data = list()
  for row in data:
    d = dict()
    for key, value in zip(field_names, row):
      d[key] = value
    new_data.append(d)
  return new_data

#---------------------------------------------------------------------
def _load_ds_body(name, fix_csv=False):
  flags = {"name": name}
  cmd = "qri body -a {name}".format(**flags)
  result = _shell_exec(cmd)
  data = json.loads(result)
  if fix_csv:
    data = convert_csv(data)
  return pd.DataFrame.from_records(data)

def _load_ds_head(name):
  flags = {"name": name}
  cmd = "qri get -f json {name}".format(**flags)
  result = _shell_exec(cmd)
  d = json.loads(result)
  return shift_root_down(d)

def load_ds(ds_name):
  if len(ds_name.split("/")) != 2:
    ds_name = u"me/{}".format(ds_name)
  head = _load_ds_head(ds_name)
  if is_csv(head):
    body = _load_ds_body(ds_name, fix_csv=True)
  else:
    body = _load_ds_body(ds_name, fix_csv=False)

  return QriDataset(body, head, ds_name)

#---------------------------------------------------------------------
def _list_ds(limit, offset):
  flags = {"limit": limit, "offset": offset, "format": "json"}
  cmd = "qri -l {limit} -o {offset} -f {format} list".format(**flags)
  result = _shell_exec(cmd)
  return json.loads(result)

def list_ds(limit=25, offset=0, name_only=True):
  datasets = _list_ds(limit, offset)
  if name_only:
    return ["{}/{}".format(x["peername"], x["name"]) for x in datasets]
  else:
    return datasets
