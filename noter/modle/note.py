from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Note:
   id: str
   title: str
   content: str
   created_at: datetime
   updated_at: datetime

   @staticmethod
   def create(title: str = "", content: str = "") -> "Note":
       now = datetime.now()
       return Note(
           id=str(uuid.uuid4()),
           title=title,
           content=content,
           created_at=now,
           updated_at=now
       )

   def update(self, title: str = None, content: str = None) -> None:
       if title is not None:
           self.title = title
       if content is not None:
           self.content = content
       self.updated_at = datetime.now()

   @property
   def preview(self) -> str:
       return self.content[:100] + "..." if len(self.content) > 100 else self.content
