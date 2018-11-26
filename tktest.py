#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk

def pushed(self):
 self["text"] = "押されたよ"

def btn_callback():
    print("ボタン0が押されました")

#rootウィンドウを作成
root = tk.Tk()
#rootウィンドウのタイトルを変える
root.title("Tkinterテスト")
#rootウィンドウの大きさを320x240に
root.geometry("320x240")

#Label部品を作る
label = tk.Label(root, text="Tkinterのテストです")
#表示する
label.pack()

#ボタンを作る
button1 = tk.Button(root, text="ボタン", command=btn_callback)
#表示
button1.pack(fill="x")

#メインループ
root.mainloop()
