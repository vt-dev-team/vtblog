# vtblog

A simple blog system with FaseApi

## Installation

### 1. Install `FastApi`

```
pip install fastapi
pip install uvicorn
```

### 2. Clone this project

```
git clone https://github.com/vt-dev-team/vtblog
```

### 3. Start Backend

```
cd vtblog
uvicorn backend.main:app --reload
```

## Interface

| Url | Description | Request Method | Data Type | Example |
| ---- | ---- | ---- | ---- | ---- |
| `/new/post` | Create a post | post | application/json | `curl -X POST "http://127.0.0.1:8000/new/post" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"title\":\"测试\",\"content\":\"测试\",\"tags\":\"测hi\",\"toplevel\":1,\"date\":1593950888,\"defunct\":true}"` |