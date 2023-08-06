import flask
from flask import Flask,render_template
from threading import Thread
from Host import test


class Connect:
  def __init__(self):
    print("[ GOTji ]: Connected!")

class Host:
  def __init__(self):
    test()
