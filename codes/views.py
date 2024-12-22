from django.shortcuts import render, redirect
from django.contrib.auth import login
from codes.form import CodeForm
from codes.models import Code
from users.models import User


def verify_view(request):
    """Проверка логина пользователя по высылаемому коду в смс"""
    form = CodeForm(request.POST or None)
    pk = request.session.get("pk")

    if pk:
        # получаем пользователя
        user = User.objects.get(pk=pk)
        # проверяем есть в БД для этого пользователя код, если нет, то создаю экземпляр класса Code
        if Code.objects.filter(user=user).exists():
            code = Code.objects.get(user=user)
        else:
            code = Code.objects.create(user=user)
        # строковое представление данных
        code_user = f"{user.phone}: {code.number}"
        # запуск формы верификации с выводом в консоль кода (либо отправки смс)
        if not request.POST:
            print(code_user)
        # проверка введенного кода
        if form.is_valid():
            num = form.cleaned_data.get("number")

            if code.number == num:
                # в БД обновляю код верификации
                code.save()
                # авторизирую пользователя
                login(request, user)
                return redirect("publications:publication_list")
            else:
                return redirect("users:login")
    return render(request, "codes/verify.html", {"form": form})
