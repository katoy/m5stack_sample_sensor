
これは beetelC を M5Stick + joystick でコントロールするようにしたものです。

M5stickC (beetlcC に搭載するマシン) のプログラムも、M5Stack(コントローラ) のプログラムもすべてUIFLOW 1.4.1 beta で書いています。

M5stock 側では、 HAT の beetelcC を追加しています。

M5stack 側では、UNITS の joystick を追加しています。

2 つのマシンの間は ESPNOW で通信しています (ブロードキャストで)

# リモコンの操作方法

joystic のボタンを押すと、モーターをすべて Stop します。同時に LED(一番目) を赤く点灯させます。
ボタンを話せば、LEC は消えます。また、現時点の joystick で指示されたエンジンの回転をします。

JOYSTIC のケーブルを手首側にして持ちます。

stick を 90 度側に倒せば 左右のエンジンが同じ速度で回転します。深く倒すほどに回転速度があがります。
逆に 090 度側に倒せば、左右にエンジンが逆回転します。

stick を 0 度側に倒すと、車が右側に曲がるようになります。(左側モーターが stock を倒す量に応じて増えていきます)

stick を 180 度側に倒すと、車が左側に曲がるようになります。(右側モーターが stock を倒す量に応じて増えていきます)

回転の量は、M5stack, M5stock にスクリーンに 数字で示されます。
