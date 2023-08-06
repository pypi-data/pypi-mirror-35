from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.sites.models import Site
from system.utils.storage import ImageStorage
from uuslug import slugify


class Menu(MPTTModel):
    title = models.CharField('名称', max_length=128)
    alias = models.CharField('标签', max_length=32, blank=True)
    url = models.CharField('地址', max_length=256)
    description = models.TextField('描述', blank=True, null=True)
    parent = TreeForeignKey('self', verbose_name='上级菜单', related_name='children', null=True, blank=True,
                            on_delete=models.SET_NULL)
    status = models.IntegerField('状态', choices={(1, '显示'), (2, '隐藏')}, default=1)
    sort = models.IntegerField('排序', default=1)
    type = models.IntegerField('类别', choices={(1, '店铺'), (2, '文章'), (3, '论坛')}, default=1)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'menu'
        verbose_name = '菜单'
        verbose_name_plural = verbose_name + '管理'

    def __str__(self):
        return self.title


class Province(models.Model):
    name = models.CharField('省份', max_length=32)
    code = models.CharField('代码', max_length=32, blank=True)

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name
        db_table = 'province'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField('城市', max_length=32)
    province = models.ForeignKey('Province', verbose_name='所属省份', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name
        db_table = 'city'

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField('区域', max_length=32)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name
        db_table = 'area'

    def __str__(self):
        return self.name


# 用户访问记录
class VisitLogs(models.Model):
    url = models.CharField('访问页面', max_length=128)
    ip = models.CharField('IP', max_length=32, blank=True)
    user_agent = models.CharField('User-Agent', max_length=255)
    plant_form = models.CharField('用户终端', max_length=255, blank=True)
    referrer = models.CharField('来源网站', max_length=255, blank=True)
    passport = models.CharField('用户身份', max_length=32, blank=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'visit_log'
        verbose_name = '访问记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.url


class SmsCode(models.Model):
    mobile = models.CharField('手机', max_length=32)
    code = models.IntegerField('验证码')
    used = models.BooleanField('是否验证', default=False)
    ip = models.CharField('IP', max_length=32, blank=True)
    user_agent = models.CharField('User-Agent', max_length=255, blank=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'sms_code'
        verbose_name = '手机验证码'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.mobile


class SiteProperty(models.Model):
    site = models.OneToOneField(Site, verbose_name='站点', on_delete=models.CASCADE)
    title = models.CharField('站点标题', max_length=128, blank=True)
    sub_title = models.CharField('副标题', max_length=128, blank=True)
    template = models.CharField('模板名称', max_length=64, blank=True)
    slug = models.SlugField('简称别名', help_text='图片、文件存储路径,为域名中间名称', max_length=64)
    meta_desc = models.TextField('描述', blank=True, null=True)
    meta_keywords = models.TextField('关键词', blank=True, null=True)
    type = models.IntegerField('站点类别', choices={(1, '女性'), (2, '新闻'), (3, '企业')}, default=1)
    logo = models.ImageField('LOGO', upload_to='upload/sites', storage=ImageStorage(), blank=True, null=True)
    icon = models.ImageField('ICON', upload_to='upload/sites', storage=ImageStorage(), blank=True, null=True)
    blocks = models.CharField('模块设定', max_length=255, help_text='使用英文,号分隔类别,:号后面为显示条数|分隔区块', blank=True, null=True)
    phone = models.CharField('联系电话', max_length=32, blank=True)
    email = models.CharField('Email', max_length=64, blank=True)
    qq = models.CharField('QQ', max_length=64, blank=True)
    beian = models.CharField('备案号', max_length=64, blank=True)
    baidu_verify: '百度站点验证码' = models.CharField('百度验证', max_length=64, blank=True)
    tongji = models.TextField('百度统计', blank=True)

    class Meta:
        db_table = 'site_property'
        verbose_name = '站点信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.site.name

    @staticmethod
    def check_site_property(site):
        if not hasattr(site, 'siteproperty'):
            site_property = SiteProperty()
            site_property.site = site
            site_property.slug = slugify(site.name)
            site_property.title = site.name
            site_property.save()


# 友情链接
class Links(models.Model):
    site = models.ManyToManyField(Site, verbose_name='所属站点', blank=True)
    title = models.CharField('站点名称', max_length=64)
    domain = models.CharField('域名', max_length=128)
    desc = models.TextField('备注', blank=True, null=True)
    status = models.BooleanField('状态', choices=((1, '启用'), (0, '禁用')), default=1)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'links'
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.title
