#!/bin/bash

# usage:
#  ctl.html の内容を char 配列文にして page,h に出力する。
#  (変換結果と ctl.html を念のための比較する)

# gcc gen_page.c -o gen_page
gzip -c ctl.html | ./gen_page > page.h

gcc decode_page.c -o decode_page
./decode_page > /tmp/ctl.html.gz
gunzip /tmp/ctl.html.gz
diff ctl.html /tmp/ctl.html
