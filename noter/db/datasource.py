import sqlite3
from datetime import datetime
from typing import List, Optional
from noter.modle.note import Note
import os

class Database:
   def __init__(self, db_path: str):
       """
       初始化数据库管理类
       Args:
           db_path: 数据库文件路径
       """
       self.db_path = db_path
       self.init_db()

   def init_db(self):
       """
       初始化数据库：
       1. 创建数据库目录（如果不存在）
       2. 创建数据库表和索引
       3. 处理可能的数据库错误
       """
       try:
           # 确保数据库目录存在
           os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
           
           # 创建数据库连接并执行初始化脚本
           with sqlite3.connect(self.db_path) as conn:
               with open('schema.sql', 'r', encoding='utf-8') as f:
                   conn.executescript(f.read())
       except sqlite3.Error as e:
           print(f"数据库初始化错误: {e}")
           raise

   def get_connection(self):
       """
       获取数据库连接
       Returns:
           sqlite3.Connection: 数据库连接对象
       """
       try:
           return sqlite3.connect(self.db_path)
       except sqlite3.Error as e:
           print(f"数据库连接错误: {e}")
           raise
