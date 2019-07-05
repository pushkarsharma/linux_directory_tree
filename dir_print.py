#!/usr/bin/python3

import os


def file_listing(path, level):
  file_list = os.listdir(path)
  for entry in file_list:
    if os.path.isdir(path+entry):
      print("\t"*level + entry)
      file_listing(path+entry+"/", level+1)
    else:
      print("\t"*level + entry)
      
      
if __name__ == '__main__':
  file_listing("./", 0)
