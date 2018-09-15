#需要在用例结束的时候去清理一些测试数据，或清除测试过程中创建的对象
import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp():
    smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)       #module中的用例执行完成后smtp.close()方法会执行，无论用例的运行状态是怎么样的,都会执行
    yield smtp  # provide the fixture value          #yield 关键字返回了fixture中实例化的对象smtp
    print("teardown smtp")
    smtp.close()