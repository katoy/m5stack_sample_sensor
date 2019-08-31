
- https://docs.m5stack.com/#/en/unit/finger
  M5Stack Docs / Unit FINGER

- https://www.youtube.com/watch?v=PN6thkTXB9c
  Fingerprint lock with M5Stack and UIFlow

- https://github.com/m5stack/m5-docs/blob/master/docs/ja/unit/finger.md
  m5-docs/docs/ja/unit/finger.md

- https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/Fingerprint


環境：
- m5stack go
- fingerprint ユニットを C ポートに接続。
- M5Burner で UOFlow-v1.4.0-beta を書き込み。
- Mac で UIFlow-Desktop-IDE で Flow 1.3.2 に設定して作業。

使い方
- ボタンC: 登録した指紋を削除する。
- ボタンA, B: user1, user2 として指紋を登録する。(登録がおわるまで、指をセンサーから指を話さない)
- 登録後、センサーをタッチする。
登録した指紋なら、高いラの音が鳴る。user id も表示される。
登録していない指紋なら、低いラの音が鳴る。
