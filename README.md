# speee-problem

# 環境内容
```
python = "^3.11"
fastapi = "0.111.0"
uvicorn = "0.29.0"
```

# ファイル構造
```
.
├── fibo.py // フィボナッチ数列プログラム
├── main.py // FastAPIのエントリポイント
└── test/test-fibo.py // フィボナッチ数列プログラムのユニットテスト
```

# エンドポイント
```
https://speee-problem.onrender.com/fib
```
## リクエストパラメータ
| パラメータ | 型 | 説明 |
| ---- | ---- | ---- |
| n | int | フィボナッチ数列の第n項(0 < n < 100) |

## レスポンスフィールド
| フィールド | 説明 |
| ---- | ---- |
| result | フィボナッチ数列第n項の値 |

## エラーレスポンス
| コード | 説明 |
| ---- | ---- |
| 400 | 無効な入力値 |

## 例
```
https://speee-problem.onrender.com/fib/?n=99
{"result":218922995834555169026}
```
