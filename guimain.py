# -*- coding: utf-8 -*-
import os
import time

from remi.gui import *
from remi import start, App
from bkret import *
from fnmatch import fnmatch


class Myapp(App):
    def __init__(self, *args):
        super(Myapp, self).__init__(*args)
        self.history = []
        self.nowpage = 0
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR

    def main(self):
        a = os.getcwd()
        self.dict1 = {}
        if (not os.path.exists(a + "\\config\\namenum.txt")):
            getallbook()
        with open(a + "\\config\\namenum.txt", "r", encoding="utf-8") as f:
            li1 = f.read().splitlines()
        for i in li1:
            tmp = i.split("=")
            if len(tmp) == 2:
                self.dict1[tmp[0]] = tmp[1]
        print("写入完成")
        self.construct_ui()
        return self.tabbox0

    def construct_ui(self):
        self.tabbox0 = TabBox()
        self.tabbox0.attr_class = "TabBox"
        self.tabbox0.attr_editor_newclass = False
        self.tabbox0.css_height = "1000px"
        self.tabbox0.css_left = "20px"
        self.tabbox0.css_overflow = "scroll"
        self.tabbox0.css_position = "absolute"
        self.tabbox0.css_top = "20px"
        self.tabbox0.css_width = "1920px"
        self.tabbox0.variable_name = "tabbox0"
        self.container0 = Container()
        self.container0.attr_class = "Container"
        self.container0.attr_editor_newclass = False
        self.container0.css_display = "none"
        self.container0.css_height = "960px"
        self.container0.css_left = "20px"
        self.container0.css_position = "absolute"
        self.container0.css_top = "80px"
        self.container0.css_visibility = "visible"
        self.container0.css_width = "1800px"
        self.container0.variable_name = "container0"
        self.label1 = Label()
        self.label1.attr_class = "Label"
        self.label1.attr_editor_newclass = False
        self.label1.css_background_color = "rgb(255,0,255)"
        self.label1.css_font_size = "30px"
        self.label1.css_font_weight = "900"
        self.label1.css_height = "50px"
        self.label1.css_left = "20%"
        self.label1.css_line_height = "45px"
        self.label1.css_position = "absolute"
        self.label1.css_text_align = "center"
        self.label1.css_top = "20px"
        self.label1.css_white_space = "pre-wrap"
        self.label1.css_width = "60%"
        self.label1.text = "小说查询系统"
        self.label1.variable_name = "label1"
        self.container0.append(self.label1, 'label1')
        self.vbox0 = VBox()
        self.vbox0.attr_class = "VBox"
        self.vbox0.css_align_items = "center"
        self.vbox0.css_background_color = "rgb(255,0,0)"
        self.vbox0.css_display = "flex"
        self.vbox0.css_flex_direction = "column"
        self.vbox0.css_height = "195.0px"
        self.vbox0.css_justify_content = "space-around"
        self.vbox0.css_left = "25%"
        self.vbox0.css_position = "absolute"
        self.vbox0.css_top = "100px"
        self.vbox0.css_width = "50%"
        self.vbox0.variable_name = "vbox0"
        self.label0 = Label()
        self.label0.attr_class = "Label"
        self.label0.attr_editor_newclass = False
        self.label0.css_align_self = "center"
        self.label0.css_background_color = "rgb(0,255,255)"
        self.label0.css_border_color = "rgb(255,255,255)"
        self.label0.css_color = "rgb(105,154,94)"
        self.label0.css_font_style = "italic"
        self.label0.css_font_weight = "bolder"
        self.label0.css_height = "20px"
        self.label0.css_order = "-1"
        self.label0.css_position = "static"
        self.label0.css_text_align = "center"
        self.label0.css_top = "100%"
        self.label0.css_width = "100px"
        self.label0.text = "输入"
        self.label0.variable_name = "label0"
        self.vbox0.append(self.label0, 'label0')
        self.textinput0 = TextInput()
        self.textinput0.attr_class = "TextInput"
        self.textinput0.css_font_weight = "bolder"
        self.textinput0.css_height = "30px"
        self.textinput0.css_order = "-1"
        self.textinput0.css_position = "static"
        self.textinput0.css_top = "20px"
        self.textinput0.css_width = "60%"
        self.textinput0.text = "请输入查找内容"
        self.textinput0.variable_name = "textinput0"
        self.vbox0.append(self.textinput0, 'textinput0')
        self.button0 = Button()
        self.button0.attr_class = "Button"
        self.button0.attr_editor_newclass = False
        self.button0.css_border_color = "rgb(0,255,255)"
        self.button0.css_height = "30px"
        self.button0.css_order = "-1"
        self.button0.css_position = "static"
        self.button0.css_top = "20px"
        self.button0.css_width = "100px"
        self.button0.text = "查找"
        self.button0.variable_name = "button0"
        self.button0.onclick.connect(self.commit1)
        self.vbox0.append(self.button0, 'button0')
        self.container0.append(self.vbox0, 'vbox0')
        self.vbox1 = VBox()
        self.vbox1.attr_class = "VBox"
        self.vbox1.attr_editor_newclass = False
        self.vbox1.css_align_items = "center"
        self.vbox1.css_background_color = "rgb(0,181,130)"
        self.vbox1.css_display = "flex"
        self.vbox1.css_flex_direction = "column"
        self.vbox1.css_height = "640px"
        self.vbox1.css_justify_content = "space-around"
        self.vbox1.css_left = "10%"
        self.vbox1.css_position = "absolute"
        self.vbox1.css_top = "320px"
        self.vbox1.css_width = "80%"
        self.vbox1.variable_name = "vbox1"
        self.label2 = Label()
        self.label2.attr_class = "Label"
        self.label2.attr_editor_newclass = False
        self.label2.css_background_color = "rgb(241,140,108)"
        self.label2.css_font_weight = "bolder"
        self.label2.css_height = "20px"
        self.label2.css_order = "-1"
        self.label2.css_position = "static"
        self.label2.css_text_align = "center"
        self.label2.css_top = "10px"
        self.label2.css_width = "100px"
        self.label2.text = "查询结果"
        self.label2.variable_name = "label2"
        self.vbox1.append(self.label2, 'label2')
        self.label3 = Label()
        self.label3.attr_class = "Label"
        self.label3.attr_editor_newclass = False
        self.label3.css_font_style = "italic"
        self.label3.css_font_weight = "bold"
        self.label3.css_height = "20px"
        self.label3.css_order = "-1"
        self.label3.css_position = "static"
        self.label3.css_text_align = "center"
        self.label3.css_top = "410px"
        self.label3.css_width = "40%"
        self.label3.text = "按照pagerank及相关度排序"
        self.label3.variable_name = "label3"
        self.vbox1.append(self.label3, 'label3')
        self.label4 = Label()
        self.label4.attr_class = "Label"
        self.label4.attr_editor_newclass = False
        self.label4.css_background_color = "rgb(255,255,255)"
        self.label4.css_font_weight = "bold"
        self.label4.css_height = "500px"
        self.label4.css_order = "-1"
        self.label4.css_overflow = "scroll"
        self.label4.css_position = "static"
        self.label4.css_top = "231.8499984741211px"
        self.label4.css_width = "1400px"
        self.label4.css_white_space = "pre-line"
        self.label4.text = "若完全匹配则输出章节内容，否则请选择所需书名重新查询"
        self.label4.variable_name = "label4"
        self.vbox1.append(self.label4, 'label4')
        self.textinput1 = TextInput()
        self.textinput1.attr_class = "TextInput"
        self.textinput1.attr_editor_newclass = False
        self.textinput1.css_height = "30px"
        self.textinput1.css_order = "-1"
        self.textinput1.css_position = "static"
        self.textinput1.css_top = "339.8499984741211px"
        self.textinput1.css_width = "300px"
        self.textinput1.text = "请输入跳转章节（默认下一页）"
        self.textinput1.variable_name = "textinput1"
        self.vbox1.append(self.textinput1, 'textinput1')
        self.button1 = Button()
        self.button1.attr_class = "跳转"
        self.button1.attr_editor_newclass = False
        self.button1.css_height = "30px"
        self.button1.css_order = "-1"
        self.button1.css_position = "static"
        self.button1.css_top = "414.8499984741211px"
        self.button1.css_width = "100px"
        self.button1.text = "跳转"
        self.button1.variable_name = "button1"
        self.button1.onclick.connect(self.jump)
        self.vbox1.append(self.button1, 'button1')
        self.container0.append(self.vbox1, 'vbox1')
        self.label5 = Label()
        self.label5.attr_class = "Label"
        self.label5.attr_editor_newclass = False
        self.label5.css_background_color = "rgb(0,255,255)"
        self.label5.css_color = "rgb(255,0,0)"
        self.label5.css_font_size = "20px"
        self.label5.css_font_weight = "bolder"
        self.label5.css_height = "120.0px"
        self.label5.css_left = "20px"
        self.label5.css_position = "absolute"
        self.label5.css_text_align = "center"
        self.label5.css_top = "20px"
        self.label5.css_width = "150.0px"
        self.label5.text = "适度网文放松，沉迷网文伤身。 合理安排时间，享受健康生活。"
        self.label5.variable_name = "label5"
        self.container0.append(self.label5, 'label5')
        self.tabbox0.append(self.container0, '普通搜索')
        self.container1 = Container()
        self.container1.attr_class = "Container"
        self.container1.attr_editor_newclass = False
        self.container1.css_background_color = "rgb(255,255,255)"
        self.container1.css_display = "block"
        self.container1.css_height = "960px"
        self.container1.css_left = "60px"
        self.container1.css_position = "absolute"
        self.container1.css_top = "80px"
        self.container1.css_width = "1800px"
        self.container1.variable_name = "container1"
        self.vbox2 = VBox()
        self.vbox2.attr_class = "VBox"
        self.vbox2.attr_editor_newclass = False
        self.vbox2.css_align_items = "center"
        self.vbox2.css_background_color = "rgb(0,131,0)"
        self.vbox2.css_display = "flex"
        self.vbox2.css_flex_direction = "column"
        self.vbox2.css_height = "300px"
        self.vbox2.css_justify_content = "space-around"
        self.vbox2.css_left = "300px"
        self.vbox2.css_position = "absolute"
        self.vbox2.css_top = "20px"
        self.vbox2.css_width = "1200px"
        self.vbox2.variable_name = "vbox2"
        self.hbox0 = HBox()
        self.hbox0.attr_class = "HBox"
        self.hbox0.attr_editor_newclass = False
        self.hbox0.css_align_items = "center"
        self.hbox0.css_background_color = "rgb(255,255,171)"
        self.hbox0.css_display = "flex"
        self.hbox0.css_flex_direction = "row"
        self.hbox0.css_height = "50px"
        self.hbox0.css_justify_content = "space-around"
        self.hbox0.css_order = "-1"
        self.hbox0.css_position = "static"
        self.hbox0.css_top = "10%"
        self.hbox0.css_width = "250px"
        self.hbox0.variable_name = "hbox0"
        self.label6 = Label()
        self.label6.attr_class = "Label"
        self.label6.attr_editor_newclass = False
        self.label6.css_font_weight = "bold"
        self.label6.css_height = "30px"
        self.label6.css_order = "-1"
        self.label6.css_position = "static"
        self.label6.css_text_align = "center"
        self.label6.css_top = "20px"
        self.label6.css_width = "100px"
        self.label6.text = "包含所有关键词"
        self.label6.variable_name = "label6"
        self.hbox0.append(self.label6, 'label6')
        self.textinput2 = TextInput()
        self.textinput2.attr_class = "TextInput"
        self.textinput2.attr_editor_newclass = False
        self.textinput2.css_height = "30px"
        self.textinput2.css_order = "-1"
        self.textinput2.css_position = "static"
        self.textinput2.css_top = "114.8499984741211px"
        self.textinput2.css_width = "100px"
        self.textinput2.text = "请用半角逗号隔开字符串"
        self.textinput2.variable_name = "textinput2"
        self.hbox0.append(self.textinput2, 'textinput2')
        self.vbox2.append(self.hbox0, 'hbox0')
        self.hbox1 = HBox()
        self.hbox1.attr_class = "HBox"
        self.hbox1.attr_editor_newclass = False
        self.hbox1.css_align_items = "center"
        self.hbox1.css_background_color = "rgb(0,127,176)"
        self.hbox1.css_display = "flex"
        self.hbox1.css_flex_direction = "row"
        self.hbox1.css_height = "50px"
        self.hbox1.css_justify_content = "space-around"
        self.hbox1.css_order = "-1"
        self.hbox1.css_position = "static"
        self.hbox1.css_top = "268.8499984741211px"
        self.hbox1.css_width = "250px"
        self.hbox1.variable_name = "hbox1"
        self.label7 = Label()
        self.label7.attr_class = "Label"
        self.label7.attr_editor_newclass = False
        self.label7.css_font_weight = "bolder"
        self.label7.css_height = "30px"
        self.label7.css_order = "-1"
        self.label7.css_position = "static"
        self.label7.css_top = "415.8499984741211px"
        self.label7.css_width = "100px"
        self.label7.text = "不包含关键词"
        self.label7.variable_name = "label7"
        self.hbox1.append(self.label7, 'label7')
        self.textinput3 = TextInput()
        self.textinput3.attr_class = "TextInput"
        self.textinput3.attr_editor_newclass = False
        self.textinput3.css_height = "30px"
        self.textinput3.css_order = "-1"
        self.textinput3.css_position = "static"
        self.textinput3.css_top = "428.8499984741211px"
        self.textinput3.css_width = "100px"
        self.textinput3.text = "请用半角逗号隔开字符串"
        self.textinput3.variable_name = "textinput3"
        self.hbox1.append(self.textinput3, 'textinput3')
        self.vbox2.append(self.hbox1, 'hbox1')
        self.hbox2 = HBox()
        self.hbox2.attr_class = "HBox"
        self.hbox2.attr_editor_newclass = False
        self.hbox2.css_align_items = "center"
        self.hbox2.css_background_color = "rgb(255,0,0)"
        self.hbox2.css_display = "flex"
        self.hbox2.css_flex_direction = "row"
        self.hbox2.css_height = "50px"
        self.hbox2.css_justify_content = "space-around"
        self.hbox2.css_order = "-1"
        self.hbox2.css_position = "static"
        self.hbox2.css_top = "240.8499984741211px"
        self.hbox2.css_width = "250px"
        self.hbox2.variable_name = "hbox2"
        self.label8 = Label()
        self.label8.attr_class = "Label"
        self.label8.attr_editor_newclass = False
        self.label8.css_font_weight = "bolder"
        self.label8.css_height = "30px"
        self.label8.css_order = "-1"
        self.label8.css_position = "static"
        self.label8.css_top = "222.8499984741211px"
        self.label8.css_width = "100px"
        self.label8.text = "包含任意关键词"
        self.label8.variable_name = "label8"
        self.hbox2.append(self.label8, 'label8')
        self.textinput4 = TextInput()
        self.textinput4.attr_class = "TextInput"
        self.textinput4.attr_editor_newclass = False
        self.textinput4.css_height = "30px"
        self.textinput4.css_order = "-1"
        self.textinput4.css_position = "static"
        self.textinput4.css_top = "220.8499984741211px"
        self.textinput4.css_width = "100px"
        self.textinput4.text = "请用半角逗号隔开字符串"
        self.textinput4.variable_name = "textinput4"
        self.hbox2.append(self.textinput4, 'textinput4')
        self.vbox2.append(self.hbox2, 'hbox2')
        self.button2 = Button()
        self.button2.attr_class = "Button"
        self.button2.attr_editor_newclass = False
        self.button2.css_height = "30px"
        self.button2.css_order = "-1"
        self.button2.css_position = "static"
        self.button2.css_top = "20px"
        self.button2.css_width = "100px"
        self.button2.text = "关键词搜索"
        self.button2.variable_name = "button2"
        self.button2.onclick.connect(self.keyword)
        self.vbox2.append(self.button2, 'button2')
        self.container1.append(self.vbox2, 'vbox2')
        self.vbox3 = VBox()
        self.vbox3.attr_class = "VBox"
        self.vbox3.attr_editor_newclass = False
        self.vbox3.css_align_items = "center"
        self.vbox3.css_background_color = "rgb(91,136,126)"
        self.vbox3.css_display = "flex"
        self.vbox3.css_flex_direction = "column"
        self.vbox3.css_height = "200px"
        self.vbox3.css_justify_content = "space-around"
        self.vbox3.css_left = "394.1999816894531px"
        self.vbox3.css_position = "absolute"
        self.vbox3.css_top = "360px"
        self.vbox3.css_width = "1000px"
        self.vbox3.variable_name = "vbox3"
        self.hbox3 = HBox()
        self.hbox3.attr_class = "HBox"
        self.hbox3.attr_editor_newclass = False
        self.hbox3.css_align_items = "center"
        self.hbox3.css_background_color = "rgb(159,136,121)"
        self.hbox3.css_display = "flex"
        self.hbox3.css_flex_direction = "row"
        self.hbox3.css_height = "100px"
        self.hbox3.css_justify_content = "space-around"
        self.hbox3.css_order = "-1"
        self.hbox3.css_position = "static"
        self.hbox3.css_top = "180.8499984741211px"
        self.hbox3.css_width = "250px"
        self.hbox3.variable_name = "hbox3"
        self.label9 = Label()
        self.label9.attr_class = "Label"
        self.label9.attr_editor_newclass = False
        self.label9.css_font_weight = "bolder"
        self.label9.css_height = "30px"
        self.label9.css_order = "-1"
        self.label9.css_position = "static"
        self.label9.css_text_align = "center"
        self.label9.css_top = "20px"
        self.label9.css_width = "100px"
        self.label9.text = "通配符"
        self.label9.variable_name = "label9"
        self.hbox3.append(self.label9, 'label9')
        self.textinput5 = TextInput()
        self.textinput5.attr_class = "TextInput"
        self.textinput5.attr_editor_newclass = False
        self.textinput5.css_height = "30px"
        self.textinput5.css_order = "-1"
        self.textinput5.css_position = "static"
        self.textinput5.css_top = "20px"
        self.textinput5.css_width = "100px"
        self.textinput5.text = ""
        self.textinput5.variable_name = "textinput5"
        self.hbox3.append(self.textinput5, 'textinput5')
        self.vbox3.append(self.hbox3, 'hbox3')
        self.button3 = Button()
        self.button3.attr_class = "Button"
        self.button3.attr_editor_newclass = False
        self.button3.css_height = "30px"
        self.button3.css_order = "-1"
        self.button3.css_position = "static"
        self.button3.css_top = "20px"
        self.button3.css_width = "100px"
        self.button3.text = "通配查询"
        self.button3.variable_name = "button3"
        self.button3.onclick.connect(self.fuzzy)
        self.vbox3.append(self.button3, 'button3')
        self.container1.append(self.vbox3, 'vbox3')
        self.label10 = Label()
        self.label10.attr_class = "Label"
        self.label10.attr_editor_newclass = False
        self.label10.css_border_color = "rgb(255,136,0)"
        self.label10.css_border_radius = "4px"
        self.label10.css_border_style = "solid"
        self.label10.css_border_width = "2px"
        self.label10.css_height = "550px"
        self.label10.css_left = "400px"
        self.label10.css_position = "absolute"
        self.label10.css_top = "600px"
        self.label10.css_width = "1000px"
        self.label10.css_overflow = "scroll"
        self.label10.css_white_space = "pre-line"
        self.label10.text = "仅按相关度输出书名，若需获取章节内容请返回普通搜索"
        self.label10.variable_name = "label10"
        self.container1.append(self.label10, 'label10')
        self.button4 = Button()
        self.button4.attr_class = "Button"
        self.button4.attr_editor_newclass = False
        self.button4.css_height = "30px"
        self.button4.css_left = "850px"
        self.button4.css_position = "absolute"
        self.button4.css_top = "1200px"
        self.button4.css_width = "100px"
        self.button4.text = "显示查询历史"
        self.button4.variable_name = "button4"
        self.button4.onclick.connect(self.getlog)
        self.container1.append(self.button4, 'button4')
        self.tabbox0.append(self.container1, '高级搜索')
        return self.tabbox0

    def commit1(self, emitter):
        self.label4.set_text("搜寻中，请稍候...")
        str1 = self.textinput0.get_text().replace("\n", "")
        if str1 in self.dict1.keys():
            self.thebook = book(self.dict1[str1], str1)
            allcon = []
            tag = True
            allcon = self.thebook.get_page("1", tag)
            self.nowpage = 1
            self.history.append((time.asctime(), str1, "1"))
            str2 = ""
            for i in allcon:
                str2 += i
            self.label4.set_text(str2)
        else:
            self.label4.set_text("搜不到，这边建议重新输入呢")

    def jump(self, emitter):
        self.label4.set_text("跳转中，请稍候...")
        if self.textinput1.get_text().isdigit():
            num1 = self.textinput1.get_text()
            tag = True
            allcon = self.thebook.get_page(num1, tag)
            self.nowpage = num1
            if len(allcon) != 0:
                self.history.append((time.asctime(), self.textinput0.get_text(), num1))
            str1 = ""
            if tag:
                for i in allcon:
                    str1 += i
                self.label4.set_text(str1)
            else:
                str1 = "页数输入超出范围！总页数：{}".format(self.thebook.tpg)
                self.label4.set_text(str1)
        else:
            self.nowpage = self.nowpage + 1
            tag = True
            allcon = self.thebook.get_page(self.nowpage, tag)
            if len(allcon) != 0:
                self.history.append((time.asctime(), self.textinput0.get_text(), self.nowpage))
            str1 = ""
            if tag:
                for i in allcon:
                    str1 += i
                self.label4.set_text(str1)
            else:
                str1 = "页数已经超出范围！总页数：{}".format(self.thebook.tpg)
                self.label4.set_text(str1)

    def fuzzy(self, emitter):
        self.label10.set_text("通配查询中，请稍候...")
        strfu = self.textinput5.get_text()
        answ = []
        for i in self.dict1.keys():
            if (fnmatch(i, strfu)):
                answ.append(i)
        self.label10.set_text("（请自行copy所需结果到普通查询处搜索）符合关键词要求的书名有：\n" + "\n".join(answ))
        self.history.append((time.asctime(), "通配查询", strfu))

    def keyword(self, emitter):
        self.label10.set_text("关键词查询中，请稍候...")
        strand = self.textinput2.get_text()
        strno = self.textinput3.get_text()
        stror = self.textinput4.get_text()
        answ = self.dict1.keys()
        if strand != "" and strand != "请用半角逗号隔开字符串":
            tmp = []
            li1 = strand.split(",")
            for i in answ:
                if all(h in i for h in li1):
                    tmp.append(i)
            answ = tmp
        else:
            strand = ""
        if stror != "" and stror != "请用半角逗号隔开字符串":
            tmp = []
            li1 = stror.split(",")
            for i in answ:
                if any(h in i for h in li1):
                    tmp.append(i)
            answ = tmp
        else:
            stror=""
        if strno != "" and strno != "请用半角逗号隔开字符串":
            tmp = []
            li1 = strno.split(",")
            for i in answ:
                if all(h not in i for h in li1):
                    tmp.append(i)
            answ = tmp
        else:
            strno=""
        str1 = "（请自行copy所需结果到普通查询处搜索）符合关键词要求的书名有：\n"
        for i in answ:
            str1 += i
            str1 += "\n"
        self.label10.set_text(str1)
        self.history.append((time.asctime(), "关键字查询", strand,strno,stror))

    def getlog(self, emitter):
        self.label10.set_text("日志查询中，请稍候...")
        str1 = "查询日志如下：\n"
        for i in self.history:
            if len(i)==3 and i[1]!="通配查询":
                str1 += "{},{}——{}".format(i[0], i[1], i[2]) + "  来源：https://www.1qxs.com/xs/{}/{}/1.html\n".format(
                self.dict1[i[1]], i[2])
            else:
                if i[1]=="通配查询":
                    str1 += "{},{}——{}".format(i[0], i[1], i[2])+"\n"
                else:
                    str1 += "{},{}——必须有的：{} 不能有的：{} 存在其中一个的：{}".format(i[0],i[1],i[2],i[3],i[4])+"\n"
        self.label10.set_text(str1)


# Configuration
"""configuration = {'config_project_name': 'Myapp', 'config_address': '127.0.0.1', 'config_port': 8000,
                 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True,
                 'config_resourcepath': './res/'}"""

if __name__ == "__main__":
    start(Myapp, address='127.0.0.1', port=8000, multiple_instance=False, enable_file_cache=True, update_interval=0.1,
          start_browser=True)
    """start(Myapp, address=configuration['config_address'], port=configuration['config_port'],
          multiple_instance=configuration['config_multiple_instance'],
          enable_file_cache=configuration['config_enable_file_cache'],
          start_browser=configuration['config_start_browser'])"""
