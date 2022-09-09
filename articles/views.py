from django.shortcuts import render


data_list = [
    {
        'titel': 'چگونه UIUX کار شویم؟',
        'image': 'how-to-become-ui-ux-designer.jpg',
    }, {
        'teacher': 'تجربه کاربری (UX) چیست؟',
        'titel': 'what-is-ux.jpg',
    }, {
        'teacher': 'طراحی UI و طراحی UX چیست؟',
        'titel': 'picture5.png',
    }, {
        'teacher': 'اصول گشتالت در طراحی UI(رابط کاربری)',
        'titel': 'gestalt-principles.jpg',
    },{
        'teacher': 'طراحی رابط کاربری به سبک حرفه ای ها در Adobe XD',
        'titel': 'xd-design.jpg',
    },
]


def articles_page(request):
    return render(request, 'articles/articles.html')


def uiux_page(request):
    return render(request, 'articles/uiux.html')


