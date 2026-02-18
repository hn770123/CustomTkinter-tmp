"""
メインモジュール
CustomTkinter を使用して "Hello World" を表示するシンプルなアプリケーションです。
"""

import customtkinter

def main():
    """
    アプリケーションのメインエントリーポイントです。
    ウィンドウを作成し、"Hello World" ラベルを表示します。
    """
    # テーマの設定
    customtkinter.set_appearance_mode("System")  # モード: "System" (標準), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # テーマ: "blue" (標準), "green", "dark-blue"

    # アプリケーションウィンドウの作成
    app = customtkinter.CTk()
    app.geometry("400x240")
    app.title("Hello World App")

    # ラベルの作成と配置
    label = customtkinter.CTkLabel(app, text="Hello World", font=("Arial", 24))
    label.pack(pady=20, padx=20, expand=True)

    # アプリケーションの実行
    app.mainloop()

if __name__ == "__main__":
    main()
