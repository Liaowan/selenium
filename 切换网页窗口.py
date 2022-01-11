for handle in wd.window_handles:
    #先切换到该窗口
    wd.switch_to.window(handle)
    if 'bing' in wd.title:
        #如果网址标题有关键词bing，跳出循环
        break