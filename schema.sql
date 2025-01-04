-- 创建笔记表
CREATE TABLE IF NOT EXISTS notes (
   id TEXT PRIMARY KEY,        -- 使用UUID作为主键
   title TEXT NOT NULL,        -- 笔记标题不能为空
   content TEXT,              -- 笔记内容可以为空
   created_at TIMESTAMP NOT NULL,  -- 创建时间
   updated_at TIMESTAMP NOT NULL   -- 更新时间
);

-- 创建索引以优化按更新时间排序的查询
CREATE INDEX IF NOT EXISTS idx_notes_updated
ON notes(updated_at DESC);
