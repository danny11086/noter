
# Noter
Noter 是一个现代化的笔记应用，使用 Flet 和 SQLite 构建。它提供了创建、编辑、删除和搜索笔记的功能。

## 项目结构

```
    assets/ # 静态资源文件
    db/ 
        noter.db  # 数据库文件
    noter/
        db/
            crud.py # 数据库操作
            datasource.py  # 数据源管理
        modle/
            note.py # 笔记数据模型
        ui/
            container.py # 用户界面容器
        main.py  # 应用入口
        config.py # 配置文件
    README.md # 项目说明文件
    requirements.txt  # 项目依赖
    run.py  # 应用启动脚本
    schema.sql  # 数据库初始化脚本
```
## 安装依赖

首先，确保你已经安装了 Python 3.7 及以上版本。然后在项目根目录下运行以下命令来安装依赖：

```sh
pip install -r requirements.txt
```

## 初始化数据库

在首次运行项目之前，需要初始化数据库。你可以通过运行以下命令来完成：

```sh
python noter/db/datasource.py
```

## 运行项目

在项目根目录下运行以下命令启动应用：

```sh
python run.py
```

## 项目功能

- **创建笔记**：点击侧边栏的“新建笔记”按钮可以创建一条新的笔记。
- **编辑笔记**：在右侧编辑区编辑笔记的标题和内容，系统会自动保存。
- **删除笔记**：点击笔记列表中的删除按钮可以删除对应的笔记。
- **搜索笔记**：在搜索框中输入关键词可以搜索笔记的标题和内容。

## 目录说明

- db
    包含数据库相关的操作，包括 CRUD 和数据源管理。
- modle
    包含笔记的数据模型。
- ui
    包含用户界面相关的代码。
- assets
    存放静态资源文件。
-  storage
    存放临时数据和其他存储文件。
-  config.py
    包含应用的配置参数，如数据库路径、API 设置等。
-  schema.sql
    数据库初始化脚本，用于创建数据库表和索引。
## 贡献

欢迎提交问题和贡献代码！请确保在提交 PR 之前运行所有测试并通过。

## 许可证

本项目采用 MIT 许可证，详情请参阅 LICENSE 文件。
```
希望这个README说明能帮助你更好地理解和使用这个项目。
 