import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():

    # Brief Notes: (because Chinese could save more space so I use it as note here)
    # 先创建字典，列出想要添加的网页，然后嵌套字典，设置分类，虽然不好理解但是容易迭代，方便为模型增加数据。

    # There were 5 line comment here before. but I didn't write them.
    # Assume this is comment line 2
    # line 3
    # line 4
    # line 5
    python_pages = [

        # I guess there is no other person also use the 'pi', 3.1415926535
        # If there is another person, it is pure coincidence...
        # actually I also made a short Vlog/video for my whole process of lab exercise...
        # because I finished all of them within nearly two days at home not lab,
        # (because I have a large monitor, good at code)
        # this video is just as a record for small part of
        # my daily life, Maybe it can also be used as evidence ahhhh

        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/', 'views': 3},

        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/', 'views': 14},

        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/', 'views': 15}]

    django_pages = [

        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 92},

        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/', 'views': 65},

        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/', 'views': 35}]

    other_pages = [

        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/', 'views': 89},

        {'title': 'Flask',
         'url': 'http://flask.pocoo.org', 'views': 79}]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}}

    # if you want to add more categories or pages,
    # add them to the dictionaries above.

    # the code below goes through the cats dictionaries, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])

    # print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    # c.views = views
    # c.likes = likes
    c.save()
    return c


# Start execution here!

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
