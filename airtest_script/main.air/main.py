# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

path = os.path.dirname(os.path.dirname(__file__))
path += '/'

image_btn = Template(
    r"tpl1594296363096.png", record_pos=(0.377, 0.787), resolution=(1080, 2400)
)

ST.SNAPSHOT_QUALITY = 75


def run():
    # 启动app
    print('#@@@@@@@@', path)
    start_app("com.tencent.mobileqq")
    touch(Template(r"{}tpl1601035384920.png".format(path), record_pos=(0.427, -0.956), resolution=(1080, 2400)))
    touch(Template(r"{}tpl1601038115421.png".format(path), record_pos=(0.119, -0.384), resolution=(1080, 2400)))
    touch(Template(r"{}tpl1601035517797.png".format(path), record_pos=(0.424, -0.869), resolution=(1080, 2400)))
    touch(Template(r"{}tpl1601036327291.png".format(path), record_pos=(-0.006, -0.961), resolution=(1080.0, 2400.0)))
    touch(Template(r"{}tpl1601036010189.png".format(path), record_pos=(-0.18, -0.335), resolution=(1080, 2400)))
    touch(Template(r"{}tpl1601036068037.png".format(path), record_pos=(-0.328, -0.772), resolution=(1080, 2400)))
    touch(Template(r"{}tpl1601038179056.png".format(path), record_pos=(0.389, 1.059), resolution=(1080.0, 2400.0)))
    touch(Template(r"{}tpl1601037761291.png".format(path), record_pos=(0.011, 0.539), resolution=(1080, 2400)))
    touch(Template(r"{}tpl1601362218482.png".format(path), record_pos=(0.008, 0.448), resolution=(1080, 2400)))

    # image_btn_ele = is_display(image_btn, time_out=7)
    # if image_btn_ele:
    #     print('出现相册')
    #     touch(image_btn)


def is_display(img, time_out=10):
    try:
        wait(img, timeout=time_out)
        return True
    except Exception as e:
        print(e)
        return False


run()
