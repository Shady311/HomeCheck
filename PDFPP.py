from PyPDF2 import PdfWriter, PdfReader, PageObject, Transformation
from datetime import datetime

import io
from PySide6.QtCore import Qt
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon


import HomeCheck_ui
from HomeCheck_ui import Ui_MainWindow



class ExampleApp(QtWidgets.QMainWindow, HomeCheck_ui.Ui_MainWindow):

    p = [0, 0, 0, 0, 0, 0, 0, 0]
    pk = ["Квартплата", "Телефон", "Электричество", "Охрана пульт", "Охрана тех", "Квартплата", "Телефон", "Электричество"]

    today = datetime.today()
    year = str(today.year)  ### 2024
    month = str(today.month)  ### 1
    folder = 'E:/Документы/Дом/House_check/'
    ###house = "House_check/"
    month = "4"
    ### габариты бланка
    list_x = 2480
    list_y = 3508

    def __init__(self):
        super(ExampleApp,self).__init__()
        self.setFixedSize(600, 310)   #fis size window
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        ###self.init_UI()


    ### определение даты
    if len(month) == 1:
        month = "0" + month   ### 01
    date = year + "_" + month   ###2024_01

    report_folder = folder + year + "/"  ###  E:/Документы/Дом/House_main_check/2024/  путь до отчета
    main_folder = report_folder + "Month/" + month + "/"  ###  E:/Документы/Дом/House_main_check/2024/Month/01/  путь до чеков

    ### Список наименований чеков
    ### "CP" - квартплата 
    ### "TL"- телефон 
    ### "El_1"- электричество 1 
    ### "El_2"- электричество 2

    check = ["O_CP", "O_TL", "O_El", "O_OXR_1", "O_OXR_2", "T_CP", "T_TL", "T_El"]

    ms = 0.75 ### коэфициент масштабирования листа

    ###print(today)
    ###print(month)
    ###print(year)
    ###print(date)
    ###print(ms)

    ### Считываем PDF бланки и формируем список наличия чеков
    def input_file(self, main_folder_d, check_d, i):
        pdf_d = main_folder_d + check_d + ".pdf" ###путь до запрашиваемых пдф файлов
        print(pdf_d)
        try:
            input_d = PdfReader(open(pdf_d, 'rb'))
            page_d = input_d.pages[0]
            self.p[i] = 1
        except FileNotFoundError:
            self.p[i] = 0
        ### Если чек есть значение в контрольном списке меняем на 1, если нет- остается 0
        ### Если чек есть - возращаем чек, если нет - ни чего
        if self.p[i] == 1:
            return page_d
        if self.p[i] == 0:
            return 

    ### Создаем пустой бланк-подложку
    page_0 = PageObject.create_blank_page(None, list_x, list_y)

    ###print("page_0 - ", page_0.mediabox.upper_right[0], page_0.mediabox.upper_right[1])

    ### Функция перемещения листа
    def trXY_def(page_trXY, tx, ty):
        tr = Transformation().translate(tx, ty)
        page_trXY.add_transformation(tr)
        ###print("def tr1_def complete - ", tx, ty)
        return page_trXY

    ### Функция масштабирования листа
    def trScC_def(page_trSc, scx, scy):
        trSc = Transformation().scale(sx=scx, sy=scy)
        page_trSc.add_transformation(trSc)
        ###print("def tr2_def complete - ", scx, scy)
        return page_trSc

    ###  Вводим 4 чека

    page_1 = input_file(main_folder, check[0], 0)
    page_2 = input_file(main_folder, check[1], 1)
    page_3 = input_file(main_folder, check[2], 2)
    page_4 = input_file(main_folder, check[3], 3)
    page_5 = input_file(main_folder, check[4], 4)
    page_6 = input_file(main_folder, check[5], 5)
    page_7 = input_file(main_folder, check[6], 6)
    page_8 = input_file(main_folder, check[7], 7)

    print(p)

    ### обработка чеков 1-4
    ### если чека нет - на подложку ни чего не приходит, выдается чистая подложка

    smesh_y = 35  ### 35 - запас под заголовки
    smesh_x = 0   ### =const

    if p[0] == 1:
        check_size_y = round(page_1.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        zero_page.merge_page(page_1)
        page_01 = zero_page
        page_01 = trXY_def(page_01, smesh_x, list_y-check_size_y-smesh_y)
        smesh_x += 310

    else:
        page_01 = PageObject.create_blank_page(None, list_x, list_y)

    if p[1] == 1:
        check_size_y = round(page_2.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        zero_page.merge_page(page_2)
        page_02 = zero_page
        page_02 = trXY_def(page_02, smesh_x, list_y-check_size_y-smesh_y)
        smesh_x += 310
    else:
        page_02 = PageObject.create_blank_page(None, list_x, list_y)

    if p[2] == 1:
        check_size_y = round(page_3.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        zero_page.merge_page(page_3)
        page_03 = zero_page
        page_03 = trXY_def(page_03, smesh_x, list_y-check_size_y-smesh_y)
        smesh_x += 620
    else:
        page_03 = PageObject.create_blank_page(None, list_x, list_y)

    if p[3] == 1:
        check_size_y = round(page_4.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        zero_page.merge_page(page_4)
        page_04 = zero_page
        page_04 = trXY_def(page_04, smesh_x, list_y-check_size_y-smesh_y)
        smesh_x += 310
    else:
        page_04 = PageObject.create_blank_page(None, list_x, list_y)

    if p[4] == 1:
        check_size_y = round(page_5.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        zero_page.merge_page(page_5)
        page_05 = zero_page
        page_05 = trXY_def(page_05, smesh_x, list_y-check_size_y-smesh_y)
    else:
        page_05 = PageObject.create_blank_page(None, list_x, list_y)

    ###окончена сборка 1 документа

    smesh_x = 0

    if p[5] == 1:
        check_size_y = round(page_6.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        ###zero_page.merge_page(page_0_T)
        zero_page.merge_page(page_6)
        page_06 = zero_page
        page_06 = trXY_def(page_06, smesh_x, list_y-check_size_y-smesh_y)
        smesh_x += 310
    else:
        page_06 = PageObject.create_blank_page(None, list_x, list_y)

    if p[6] == 1:
        check_size_y = round(page_7.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        zero_page.merge_page(page_7)
        page_07 = zero_page
        page_07 = trXY_def(page_07, smesh_x, list_y-check_size_y-smesh_y)
        smesh_x += 310
    else:
        page_07 = PageObject.create_blank_page(None, list_x, list_y)

    if p[7] == 1:
        check_size_y = round(page_8.mediabox.upper_right[1])
        zero_page = PageObject.create_blank_page(None, list_x, list_y)
        zero_page.merge_page(page_8)
        page_08 = zero_page
        page_08 = trXY_def(page_08, smesh_x, list_y-check_size_y-smesh_y)
    else:
        page_08 = PageObject.create_blank_page(None, list_x, list_y)

    ###окончена сборка 2 документа

    ### генерация надписей

    buffer_O = io.BytesIO()

    list_x_c = float(list_x)
    list_y_c = float(list_y)
    canvas_otstup_x = 20.0
    canvas_otstup_y = list_y - 40.0

    shag_canvas = 310
    H_max = 1700

    ### генерация надписей 1 документ
    smesh_x = 0

    list_canvas_O = canvas.Canvas(buffer_O, pagesize=(list_x_c, list_y_c))
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    list_canvas_O.setFont('FreeSans', 16)  # Устанавливаем шрифт и размер

    list_canvas_O.drawString(canvas_otstup_x, list_y - 15.0, "Отрадное " + year + " " + month)  # Добавляем заголовок на страницу

    count = 0

    for z in range(5):
        if p[z] == 1:
            if z == 2:
                smesh_x += 33
            list_canvas_O.drawString(canvas_otstup_x + float(smesh_x), canvas_otstup_y, pk[z])  # Добавляем текст на страницу
            count += 1
            if z == 2:
                smesh_x += shag_canvas - 33
                count += 1
            smesh_x += shag_canvas

    list_canvas_O.setLineWidth(5)
    list_canvas_O.line(0,list_y - H_max, 0 + shag_canvas * count, list_y - H_max)
    list_canvas_O.line(0 + shag_canvas * count, list_y - H_max, 0 + shag_canvas * count, list_y)


    list_canvas_O.showPage()
    list_canvas_O.save()
    buffer_O.seek(0)

    pdf_list_canvas_O = PdfReader(buffer_O)
    zero_page_canvas_O = PageObject.create_blank_page(None, list_x, list_y)
    zero_page_canvas_O.merge_page(pdf_list_canvas_O.pages[0])
    page_0_O = zero_page_canvas_O

    ### генерация надписей 2 документ
    smesh_x = 0
    canvas_otstup_x = 20.0

    buffer_T = io.BytesIO()

    list_x_t = float(list_x)
    list_y_t = float(list_y)
    canvas_otstup_x = 20.0
    canvas_otstup_y = list_y - 40.0

    list_canvas_T = canvas.Canvas(buffer_T, pagesize=(list_x_t, list_y_t))
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    list_canvas_T.setFont('FreeSans', 16)  # Устанавливаем шрифт и размер

    list_canvas_T.drawString(canvas_otstup_x, list_y - 15.0, "Тушино " + year + " " + month)  # Добавляем заголовок на страницу

    count = 0

    for zt in range(3, 6):    
        if p[zt+2] == 1:
            list_canvas_T.drawString(canvas_otstup_x + float(smesh_x), canvas_otstup_y, pk[zt+2])  # Добавляем текст на страницу
            smesh_x += shag_canvas
            count += 1

    list_canvas_T.setLineWidth(5)
    list_canvas_T.line(0, list_y - H_max, 0 + shag_canvas * count, list_y - H_max)
    list_canvas_T.line(0 + shag_canvas * count, list_y - H_max, 0 + shag_canvas * count , list_y)

    list_canvas_T.showPage()
    list_canvas_T.save()
    buffer_T.seek(0)

    pdf_list_canvas_T = PdfReader(buffer_T)
    zero_page_canvas_T = PageObject.create_blank_page(None, list_x, list_y)
    zero_page_canvas_T.merge_page(pdf_list_canvas_T.pages[0])
    page_0_T = zero_page_canvas_T

    ### объединение бланков
    ### page_01
    page_01.merge_page(page_02)
    page_01.merge_page(page_03)
    page_01.merge_page(page_04)
    page_01.merge_page(page_05)
    page_01.merge_page(page_0_O)
    ### page_06
    page_06.merge_page(page_07)
    page_06.merge_page(page_08)
    page_06.merge_page(page_0_T)

    ###print("page_1 - ", page_01.mediabox.upper_right[0], page_01.mediabox.upper_right[1])
    ###print("page_2 - ", page_02.mediabox.upper_right[0], page_02.mediabox.upper_right[1])
    ###print("page_3 - ", page_03.mediabox.upper_right[0], page_03.mediabox.upper_right[1])
    ###print("page_4 - ", page_04.mediabox.upper_right[0], page_04.mediabox.upper_right[1])

    ### Вывод итогового бланка

    ### Вывод квартиры 1
    output1 = PdfWriter()
    output1.add_page(page_01)
    output1.write(open(report_folder + date + "_O.pdf", "wb")) ###путь сохраняемого отчета E:/Документы/Дом/House_main_check/2024/2024_01.pdf  путь до отчета
    print("Report  File:" + report_folder + date + "_O.pdf - created!")

    ### Вывод квартиры 2
    output2 = PdfWriter()
    output2.add_page(page_06)
    output2.write(open(report_folder + date + "_T.pdf", "wb")) ###путь сохраняемого отчета E:/Документы/Дом/House_main_check/2024/2024_01.pdf  путь до отчета
    print("Report  File:" + report_folder + date + "_T.pdf - created!")

def main(): 
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = ExampleApp()
    mainwindow.show()
    sys.exit(app.exec())
main()



