#! /usr/bin/env python3
# coding=utf-8

from os import *
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class MailBuilder:
    """ 提供邮件构造功能 """
    def __init__(self):
        self._is_set_header = False # 用于判断是否已经设置头部信息
        self._mail = MIMEMultipart('mixed') # MIME邮件对象

    def set_header(self, h_from:str, h_to:str, subject:str):
        """ 设置头部信息及邮件主题 """
        # 省略了对参数的校验
        self._mail['From'] = h_from
        self._mail['To'] = h_to
        self._mail['subject'] = subject

    def add_text(self, text_content):
        """ 添加邮件正文部分的纯文本内容 """
        # 省略了对参数的校验
        text = MIMEText(text_content, 'plain', 'utf-8')
        self._mail.attach(text)

    def add_html(self, file_path:str, file_name:str):
        """ 添加正文部分的html文本内容，失败返回False """
        # 省略了对参数的校验
        file_complete_path = file_path / file_name
        if not os.path.isfile(file_complete_path):
            print("file don't exist...\n")
            return False
        tmp_list = file_name.split('.') # 对文件名切片
        if tmp_list[len(tmp_list)-1] != "jpg" or tmp_list[len(tmp_list)-1] != "png":
            print("file is not a jpg or png...\n")
            return False
        with open(file_complete_path, 'r') as f: # 省略对文件大小判断排除bug
            html_content = f.read()
            html_sub = MIMEText(html_content, 'html', 'utf-8')
            html_sub.add_header("Content-Disposition", "attachment", filename=file_name)
            self._mail.attach(html_sub)

    def add_image(self, file_path:str, file_name:str):
        """ 添加图片附件, 失败返回False """
        # 省略了对参数的校验
        file_complete_path = file_path / file_name
        if not os.paht.isfile(file_complete_path):
            print("file don't exitst...\n")
            return False

    def add_file(self, file_path:str, file_name:str):
        """ 添加文件附件 """
        pass

    def get_mail(self):
        """ 获取当前构建的MIME邮件对象，失败返回None """
        if not self._is_set_header:
            print("mail header format error...\n")
            return None
        



