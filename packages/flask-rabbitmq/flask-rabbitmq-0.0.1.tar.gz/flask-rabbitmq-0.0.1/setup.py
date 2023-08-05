from setuptools import setup, find_packages

# setup(
#     name = "flask-rabbitmq",
#     version = "0.1.0",
#     keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
#     description = "Let rabbitmq use flask development more easy! ! !",
#     long_description = "Let rabbitmq use flask development more easy! ! !",
#     license = "MIT Licence",
#
#     url = "https://github.com/PushyZqin/flask-rabbitmq",
#     author = "Pushy",
#     author_email = "1437876073@qq.com",
#
#     packages = find_packages(),
#     include_package_data = True,
#     platforms = "any",
#     install_requires = ['pika']
# )

from setuptools import setup

setup(
    name='flask-rabbitmq',
    version='0.0.1',
    author='Pushy',
    author_email='1437876073@qq.com',
    url='https://github.com/PushyZqin/flask-rabbitmq',
    description=u'Let rabbitmq use flask development more easy! ! !',
    packages=['flask_rabbitmq'],
    install_requires=['pika']
)