# Copyright 2016 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# Copyright 2017 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2017 Lilia Salihova
# Copyright 2016-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).

{
    "name": "Mail Relocation",
    "version": "12.0.1.0.6",
    "author": "IT-Projects LLC, Ivan Yelizariev, Pavel Romanchenko",
    "license": "Other OSI approved licence",  # MIT
    "category": "Discuss",
    "images": ["images/m1.png"],
    "support": "apps@itpp.dev",
    "website": "https://twitter.com/yelizariev",
    "price": 100.00,
    "currency": "EUR",
    "depends": ["mail_all"],
    "data": ["mail_move_message_views.xml", "data/mail_move_message_data.xml"],
    "qweb": ["static/src/xml/mail_move_message_main.xml"],
    "installable": False,
}
