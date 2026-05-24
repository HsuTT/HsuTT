# HsuTT Starter (Python)

一個給新手練習的最小 Python 專案骨架，重點是：
- 有清楚的目錄結構
- 有可執行程式入口
- 有第一個自動化測試

## 專案結構

```text
.
├── README.md
├── pyproject.toml
├── src/
│   └── hsutt_starter/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

## 環境需求

- Python 3.10+

## 安裝與執行

1. （可選）建立虛擬環境：

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. 安裝測試工具：

   ```bash
   pip install -e .[dev]
   ```

3. 執行程式：

   ```bash
   python -m hsutt_starter.main
   ```

你會看到：

```text
Hello, HsuTT starter!
```

## 執行測試

```bash
pytest
```

## 新手下一步建議

1. 在 `main.py` 新增一個函式（例如加法）
2. 在 `tests/test_main.py` 先寫測試，再補實作
3. 熟悉 `git add` / `git commit` 的小步提交習慣
