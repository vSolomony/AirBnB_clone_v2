#!/usr/bin/python3
"""Package initializer"""
from models.engine.file_storage import FileStorage

"""A variable storage, an instance of FileStorage"""
storage = FileStorage()
storage.reload()
