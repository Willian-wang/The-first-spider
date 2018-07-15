import xlwt

def txt_to_excel():
    file=open('日志.txt','r',encoding='utf-8')
    workbook=xlwt.Workbook(encoding='ascii')
    worksheet=workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    print("TXT转换EXCEL中")
    colmun=0
    rows=0
    content=""
    
    while 1:
        line=file.readline()
        if (line=='﻿【厚朴足迹】\n'or line=='【厚朴足迹】\n'):
           worksheet.write(rows,colmun,content)
           content=""
           colmun=0
           rows=rows+1
           worksheet.write(rows,colmun,line)
        elif (colmun!=4):
            colmun=colmun+1
            worksheet.write(rows,colmun,line)
        else:
            content=content+line
        if not line:
            worksheet.write(rows,colmun,content)
            break
    print("TXT转换EXCEL完成")
    workbook.save('日志.xls')
    