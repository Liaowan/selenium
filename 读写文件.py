def fc():
        import re
        file=open(r'C:\Users\nglih\Desktop\实验室安全教育题库.txt', mode='r', encoding='UTF-8')
        tex=file.read()
        # b='''abca231sdasd1231231adasd
        # adwdq
        # 标准答案：A
        # xbaaxbah
        # 标准答案：正确
        # 23123'''
        # list=re.findall(r'[在火灾初发阶段，应采取哪种方法撤+]',text)
        # result=''.join(list)
        # print(result)
        # # print(list)
        # a=re.search(r'adasd',b)
        a=re.search('的处境有清醒的判',tex).span()
        c=re.search('标准答案： ',tex[a[1]:]).span()
        m=c[1]+a[1]
        for i in tex[m:]:
            if i=='\n':
                break
            else:
                print(i,end='')
