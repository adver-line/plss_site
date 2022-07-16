from email import message
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.urls import reverse_lazy


# class EmailLoginOnlyView(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.login_method == "email"

#     def handle_no_permission(self):
#         messages.error(self.request, "해당 페이지로 이동 할 수 없습니다.")
#         return redirect("core:home")


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "페이지를 찾을 수 없습니다."

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "해당 페이지로 이동 할 수 없습니다.")
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")
