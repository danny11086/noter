from noter.modle.note import Note
import sqlite3
from typing import List
from noter.db.datasource import Database
from noter.config import DB_PATH,DB_NAME
from datetime import datetime

@staticmethod
def _row_to_note(row) -> Note:
    """
    将数据库行转换为Note对象
    Args:
        row: 数据库查询结果行
    Returns:
        Note: 转换后的笔记对象
    """
    try:
        return Note(
            id=row[0],
            title=row[1],
            content=row[2],
            created_at=datetime.fromisoformat(row[3]),
            updated_at=datetime.fromisoformat(row[4])
        )
    except (IndexError, ValueError) as e:
        print(f"数据转换错误: {e}")
        raise
class DbCrud:
    
    def __init__(self):
        self.db=Database(f'{DB_PATH}/{DB_NAME}')
    def get_connection(self):
        return self.db.get_connection()
    def save_note(self, note: Note) -> None:
       """
       保存或更新笔记
       Args:
           note: 要保存的笔记对象
       """
       sql = '''
       INSERT OR REPLACE INTO notes (id, title, content, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?)
       '''
       try:
           with self.get_connection() as conn:
               conn.execute(sql, (
                   note.id,
                   note.title,
                   note.content,
                   note.created_at.isoformat(),  # 转换为ISO格式字符串
                   note.updated_at.isoformat()
               ))
       except sqlite3.Error as e:
           print(f"保存笔记错误: {e}")
           raise

    def delete_note(self, note_id: str) -> None:
        """
        删除笔记
        Args:
            note_id: 要删除的笔记ID
        """
        sql = 'DELETE FROM notes WHERE id = ?'
        try:
            with self.get_connection() as conn:
                conn.execute(sql, (note_id,))
        except sqlite3.Error as e:
            print(f"删除笔记错误: {e}")
            raise

    def get_all_notes(self) -> List[Note]:
        """
        获取所有笔记，按更新时间降序排序
        Returns:
            List[Note]: 笔记对象列表
        """
        sql = 'SELECT * FROM notes ORDER BY updated_at DESC'
        try:
            with self.get_connection() as conn:
                cursor = conn.execute(sql)
                return [_row_to_note(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"获取笔记列表错误: {e}")
            raise

    def search_notes(self, query: str) -> List[Note]:
        """
        搜索笔记
        Args:
            query: 搜索关键词
        Returns:
            List[Note]: 匹配的笔记列表
        """
        sql = '''
        SELECT * FROM notes
        WHERE title LIKE ? OR content LIKE ?
        ORDER BY updated_at DESC
        '''
        try:
            with self.get_connection() as conn:
                cursor = conn.execute(sql, (f'%{query}%', f'%{query}%'))
                return [_row_to_note(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"搜索笔记错误: {e}")
            raise
