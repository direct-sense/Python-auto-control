import pygetwindow as gw

windows = gw.getAllTitles()
for title in windows:
    if title.strip():  # 忽略空白視窗名稱
        print(f"視窗標題：{title}")
