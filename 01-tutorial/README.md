## admin の画面が表示されない

### 内容

[はじめての Django アプリ作成、その 2 | Django ドキュメント](https://docs.djangoproject.com/ja/5.0/intro/tutorial02/#start-the-development-server)

admin ユーザーを作成して [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) にアクセスをしたところ以下のようなエラーが発生

```text
TypeError at /admin/
'set' object is not reversible
Request Method:	GET
Request URL:	http://127.0.0.1:8000/admin/
Django Version:	5.0.6
Exception Type:	TypeError
Exception Value:	
'set' object is not reversible
Exception Location:	\01-tutorial\.venv\Lib\site-packages\django\urls\resolvers.py, line 568, in _populate
Raised during:	django.contrib.admin.sites.index
Python Executable:	\01-tutorial\.venv\Scripts\python.EXE
Python Version:	3.12.4
Python Path:	
[]
Server time:	Sun, 30 Jun 2024 05:32:00 +0000
```

### 解決

`polls.urls` で記述した以下の記述は間違いで、配列にする必要があった。

間違い
```python
urlpatterns = {path("", views.index, name="index")}
```

正解
```python
urlpatterns = [path("", views.index, name="index")]
```