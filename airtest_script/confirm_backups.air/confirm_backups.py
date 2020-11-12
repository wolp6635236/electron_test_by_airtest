# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

path = os.path.dirname(os.path.dirname(__file__))
path += '/'
ST.SNAPSHOT_QUALITY = 75


def run():
    # 启动app
    print('#@@@@@@@@', path)
    # start_app("com.tencent.mobileqq")
    touch(Template(r"{}tpl1601366468449.png".format(path), record_pos=(0.016, 0.042), resolution=(1080, 2400)))
    sleep(2)
    touch(Template(r"{}tpl1601372848829.png".format(path), record_pos=(-0.418, 1.036), resolution=(1080.0, 2400.0)))
    touch(Template(r"{}tpl1601366787658.png".format(path), record_pos=(0.36, 1.015), resolution=(1080, 2400)))


run()
