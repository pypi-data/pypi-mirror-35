from django.core.files.storage import FileSystemStorage
import os, time, random
from django.conf import settings
from bs4 import BeautifulSoup
from django.utils import html
from urllib import request, parse
from textrank4zh import TextRank4Sentence, TextRank4Keyword
import shortuuid
import re
import datetime


class ImageStorage(FileSystemStorage):
    # 初始化
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # 文件扩展名
        ext = os.path.splitext(name)[1]
        # 文件目录
        d = os.path.dirname(name)
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 100)
        # 重写合成文件名
        name = os.path.join(d, fn + ext)
        # 调用父类方法
        return super(ImageStorage, self)._save(name, content)


class HtmlStorage:
    """
    Html解析存储工具
    """

    @staticmethod
    def save_content(content, save_img=True, remove_a=True):
        """
        保存html中图片 并提取最一张图片
        :param content:
        :param remove_a:
        :param save_img:
        :return: html_content, first_img, key_list
        """
        soup = BeautifulSoup(content, 'lxml')
        all_imgs = soup.find_all('img')
        dir_name = '/article/' + datetime.datetime.now().strftime('%Y%m%d') + '/'
        if not os.path.exists(settings.MEDIA_ROOT + dir_name):
            os.makedirs(settings.MEDIA_ROOT + dir_name)
        first_img = ''
        for img in all_imgs:
            try:
                img_obj = parse.urlparse(img['src'])
                img_path = img_obj.path
                query_obj = parse.parse_qs(img_obj.query)
                # 已经是本站文件不保存
                if not str(img_path).startswith(settings.MEDIA_URL) and save_img:
                    # 判断是不是微信图片
                    if img_obj.netloc.__contains__('mmbiz.qpic.cn'):
                        new_query_str = str(img_obj.query).replace('tp=webp&', '')
                        new_query_obj = (
                        img_obj.scheme, img_obj.netloc, img_obj.path, img_obj.params, new_query_str, img_obj.fragment)
                        query_url = parse.urlunparse(new_query_obj)
                        img_type = img['data-type']
                        del img['data-src']
                    else:
                        img_type = img_path.split('.')[-1]
                        query_url = img['src']
                    file_path = dir_name + shortuuid.uuid() + '.' + img_type
                    request.urlretrieve(query_url, settings.MEDIA_ROOT + file_path)
                    img['src'] = settings.MEDIA_URL + file_path[1:]
                else:
                    file_path = img_path
                if first_img == '':
                    first_img = file_path
            except Exception as e:
                print('%s! img utl:%s' % (str(e), img['src']))
        html_content = ''
        for x in soup.body.contents:
            html_content += str(x)
        if remove_a:
            html_content = re.sub('</?a[^>]*>', '', html_content)
        # 关键词提取
        pure_text = html.strip_tags(html_content)
        tr_keyword = TextRank4Keyword()
        tr_keyword.analyze(pure_text)
        tr_sentence = TextRank4Sentence()
        tr_sentence.analyze(pure_text)
        return html_content, first_img, tr_keyword.get_keyphrases(), tr_sentence.get_key_sentences(1)[0].sentence
