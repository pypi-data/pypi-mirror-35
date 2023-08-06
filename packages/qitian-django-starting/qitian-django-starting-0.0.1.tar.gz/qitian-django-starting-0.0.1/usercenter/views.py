from django.views.generic import TemplateView, RedirectView, DetailView, FormView, ListView
from rest_framework.views import APIView
from system.utils.sms import YunpianSms
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Wallet, WalletLog, Orders, VipLogs
from django.http.response import HttpResponseRedirect
from .models import QtUser
from django.conf import settings
from django.shortcuts import redirect, reverse
from system.utils.Cipher import QTCipher
from system.utils.tools import pagination_tool
from system.utils.views import QtTemplateView, QtListView, QtDetailView
import time, random, logging


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return '/'


class LoginView(RedirectView):
    back_url = ''

    def post(self, request):
        phone = request.POST.get('phone')
        login_name = QtUser.real_login_name(phone, request.site)
        password = request.POST.get('login_password')
        self.back_url = request.POST.get('back_url')
        user = authenticate(username=login_name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        return super().post(request)

    def get_redirect_url(self, *args, **kwargs):
        return self.back_url


class RegisterView(APIView):
    back_url = '/'

    def post(self, request):
        phone = request.POST.get('phone')
        # 检测手机号是否已注册
        if QtUser.user_available(phone, request.site):
            return Response({'code': 300, 'msg': '手机号已注册，请直接登陆。'})
        verify_code = request.POST.get('verify_code')
        password = request.POST.get('password')
        self.back_url = request.POST.get('back_url')
        if YunpianSms.verify_code(phone, verify_code):
            # 写入用户数据
            user = User.objects.create_user(username=QtUser.real_login_name(phone, request.site), password=password)
            user.qtuser.site = request.site
            user.qtuser.phone = phone
            user.qtuser.nickname = request.POST.get('nickname')
            user.qtuser.save()
            login(request, user)
            return Response({'code': 200, 'msg': '注册成功，并自动为您登陆系统。'})
        else:
            return Response({'code': 301, 'msg': '手机验证码不正确，请重新输入。'})


class MemberView(QtTemplateView):
    template_name = 'member.html'

    def get_context_data(self, **kwargs):
        context = super(MemberView, self).get_context_data(**kwargs)
        context['member'] = Group.objects.all()
        return context


class UserHomeView(LoginRequiredMixin, QtTemplateView):
    login_url = '/'
    template_name = 'usercenter/home.html'

    def get(self, request, *args, **kwargs):
        return super(UserHomeView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserHomeView, self).get_context_data(**kwargs)
        context['wallet'] = Wallet.objects.filter(user=self.request.user).get()
        # 订单列表
        # context['orders'] = Orders.objects.filter(user=self.request.user).all()[:5]
        return context


class SendCodeView(APIView):
    """
    发送验证码
    """
    back_url = '/'

    def post(self, request):
        try:
            phone = request.POST.get('mobile')
            result = YunpianSms.register_code(phone, request)
            if not result:
                ret_data = {
                    'code': 401,
                    'msg': '请勿频繁发送验证码',
                }
                return Response(ret_data)
            if result.is_succ():
                ret_data = {
                    'code': 200,
                    'msg': result.msg(),
                }
            else:
                ret_data = {
                    'code': 400,
                    'msg': result.msg(),
                }
        except IndexError:
            ret_data = {
                'code': 300,
                'msg': '手机号错误',
            }
        return Response(ret_data)


class ChangeProfileView(TemplateView):
    """
    用户属性修改
    """
    template_name = 'usercenter/change_profile.html'

    def post(self, request, *args, **kwargs):
        qt_user = QtUser.objects.filter(user=request.user).get()
        qt_user.qq = request.POST.get('qq')
        qt_user.email = request.POST.get('email')
        qt_user.real_name = request.POST.get('real_name')
        qt_user.idcard = request.POST.get('idcard')
        qt_user.alipay = request.POST.get('alipay')
        qt_user.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qt_user'] = self.request.user.qtuser
        return context


class AccountView(TemplateView):
    """
    用户帐户
    """
    template_name = 'usercenter/account.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['wallet'] = Wallet.objects.get(user_id=self.request.user.id)
        return context


class WalletLogView(ListView):
    template_name = 'usercenter/wallet_log.html'
    model = WalletLog
    context_object_name = 'wallet_log'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WalletLogView, self).get_context_data()

        # 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据，见下方。
        pagination_data = pagination_tool(context, self.request)

        # 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
        context.update(pagination_data)

        return context


class GoPayView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # 创建订单
        order = Orders.create()
        order.goods = kwargs.get('goods')
        order.type = kwargs.get('type')
        if kwargs.get('type') == 1:
            item = Group.objects.get(pk=kwargs.get('goods'))
            amount = item.groupproperty.price
            goods_name = item.name
        pay_amount = 0.01 if settings.PAY_PROJECT_ID == 2 else amount
        order.user = self.request.user
        order.amount = pay_amount
        order.site = self.request.site
        order.save()
        pay_obj = {
            'project_id': settings.PAY_PROJECT_ID,
            'amount': pay_amount,
            'order_id': order.order_sn,
            'goods_name': goods_name,
            'order_type': 1,
        }
        crypt = QTCipher(settings.AES_KEY)
        return settings.PAY_URL + crypt.encrypt(pay_obj)


class PayNoticeView(RedirectView):
    """
    支付成功后跳转
    TODO 目前跳转到用户中心  要到文章列表
    {'code': 200, 'msg': '', 'data': {'pay_type': '支付宝', 'order_no': '20180612165544279', 'total_amount': '0.01', 'trade_no': '2018061221001004650564193052', 'order_type': 1}}
    """
    crypt = QTCipher(settings.AES_KEY)
    ret_data = {}
    logger = logging.getLogger('django')

    def get(self, request, *args, **kwargs):
        try:
            self.ret_data = eval(self.crypt.decrypt(kwargs.get('key')))
        except Exception:
            self.logger.error('回调串错误：%s' % kwargs.get('key'))
            return redirect(reverse('orders:pub_article'))
        return super(PayNoticeView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        order_sn = self.ret_data['data']['order_no']
        total_amount = self.ret_data['data']['total_amount']
        order_type = self.ret_data['data']['order_type']
        pay_type = self.ret_data['data']['pay_type']

        # 开始写入钱包记录 用户为订单的用户
        WalletLog.create(self.request.user, total_amount, order_sn, 1, pay_type, '用户充值')

        if order_type == 2:
            return reverse('uc:wallet_log')

        VipLogs.add_log(order_sn, 1)
        return reverse('uc:my_vip')


class ChargeView(TemplateView):
    template_name = 'usercenter/charge.html'

    def post(self, request):
        # 创建订单
        tmp_id = time.strftime('%Y%m%d%H%M%S') + str(random.randint(100, 999))
        pay_obj = {
            'project_id': settings.PAY_PROJECT_ID,
            'amount': request.POST.get('amount'),
            'order_id': tmp_id,
            'goods_name': '用户充值',
            'order_type': 2,
        }
        crypt = QTCipher(settings.AES_KEY)
        return HttpResponseRedirect(settings.PAY_URL + crypt.encrypt(pay_obj))

    def get_context_data(self, **kwargs):
        context = super(ChargeView, self).get_context_data(**kwargs)
        context['wallet'] = self.request.user.wallet.get()
        return context


class ResetPasswordView(TemplateView):
    template_name = 'usercenter/reset_pwd.html'


class MyVipView(QtTemplateView):
    template_name = 'usercenter/member.html'

    def get_context_data(self, **kwargs):
        context = super(MyVipView, self).get_context_data(**kwargs)
        return context


class DoRestView(APIView):
    def post(self, request, *args, **kwargs):
        ret_data = dict()
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        oldpwd = request.POST.get('oldpwd')
        user = request.user
        if password != repassword:
            ret_data['code'] = 300
            ret_data['msg'] = 'notsame'
            return Response(ret_data)
        if not user.check_password(oldpwd):
            ret_data['code'] = 301
            ret_data['msg'] = 'error'
            return Response(ret_data)
        user.set_password(password)
        user.save()
        ret_data['code'] = 200
        ret_data['msg'] = '密码修改成功'
        return Response(ret_data)
