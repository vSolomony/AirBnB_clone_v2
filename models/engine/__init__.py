#!/usr/bin/python3
"""Engine Package initializer"""
from models.engine.file_storage import FileStorage

"""A variable storage, an instance of FileStorage"""
storage = FileStorage()
storage.reload()
