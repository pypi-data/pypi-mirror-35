Kurdish

Welcome to Kurdish Language Library - a Python Library for converting characters and numbers in Persian, English and also Arabic to Kurdish and vice versa.

Installation:

install the library as follows:

pip install Kurdish


Converting English Characters to Kurdish Based on KRG Unicode System (http://unicode.ekrg.org/ku_unicodes.html):
print('Kurdish.convert_En_Char_to_Ku', Kurdish.convert_En_Char_to_Ku('bexSyn le gwnah w heLe CawpoSyne! \n to Con heReSet be uagry pRtyne? \n bmbexSy be nwYjanewe, kesman le kese \n be gwnahewe bmbexSe, delYm bexSyne'))


Converting Arabic Characters to Kurdish:
print('Kurdish.convert_Ar_Char_to_Ku', Kurdish.convert_Ar_Char_to_Ku('الأبجدية العربية هي أبجدية تستخدم أحرف الهجاء العربية للكتابة، وتعد الأبجدية العربية من أكثر الأبجديات استخدامًا بعد الأبجدية اللاتيينة.[2] وتستخدم الأبجدية العربية في العديد من اللغات الآسيوية والأفريقية، مثل اللغة العربي ة، وال لغة الأردية، واللغة العثمانية، واللغة الفارسية. '))


Converting Kurdish Characters to English:
print('Kurdish.convert_Ku_Char_to_En', Kurdish.convert_Ku_Char_to_En('بەخشین لە گوناه و هەڵە چاوپۆشینە! \n  \nتۆ چۆن هەڕەشەت بە ئاگری پڕتینە?\n بمبەخشی بە نوێژانەوە, کەسمان لە کەسە\n بە گوناهەوە بمبەخشە, دەلێم بەخشینە'))


Converting Persian (Farsi) Numbers to Kurdish:
print('Kurdish.convert_Fa_Num_to_Ku', Kurdish.convert_Fa_Num_to_Ku('٠١٢٣۴۵۶٧٨٩'))


Converting Kurdish Numbers to Persian (Farsi):
print('Kurdish.convert_Ku_Num_to_Fa', Kurdish.convert_Ku_Num_to_Fa('٠١٢٣٤٥٦٧٨٩'))


Converting English Numbers to Kurdish:
print('Kurdish.convert_En_Num_to_Ku', Kurdish.convert_En_Num_to_Ku('0123456789'))


Converting Kurdish Numbers to English:
print('Kurdish.convert_Ku_Num_to_En', Kurdish.convert_Ku_Num_to_En('٠١٢٣٤٥٦٧٨٩'))

Contact me:
I hope you like this library. Feel free to reach out if you have questions or if you want to contribute in any way:

E-mail: dolanskurd@mail.com
Twitter: @dolanskurd

License:
Kurdish is available under the MIT license. See LICENSE file for more info.

