import win32gui
from airtest.core.api import *
from config_path import config_path

auto_setup(__file__)
path = os.path.dirname(os.path.dirname(__file__))
cp_image = 'adb push ./image/IMG_20200705_104501.jpg /sdcard/DCIM/Screenshots/'
delete_image = "adb shell su -c 'rm /sdcard/DCIM/Screenshots/*'"
airtest_path = config_path(os.path.join("lib", "airtest.exe"))


def login():
    for i in range(30):
        try:
            connect_device('Windows:///?title_re=QQ')
        except Exception as e:
            print(e)
            sleep(1)
        else:
            print('结束？')
            break
    sleep(4)
    touch(Template(r"{}tpl1601034777327.png".format(path + "/airtest_script/"), record_pos=(2.593, 0.516),
                   resolution=(495, 470)))
    sleep(1)
    snapshot(filename=path + "/airtest_script/image/IMG_20200705_104501.jpg")
    return


def adb_shell(cmd2):
    result = os.popen(cmd2)
    res = result.read()
    for line in res.splitlines():
        print(line)


def start_qq_by_mobile():
    try:
        # 脚本名称
        script_name = "main.air"
        # 启动之前删除上一次的日志文件
        my_file = './logs.txt'
        if os.path.exists(my_file):
            os.remove(my_file)
            print('删除日志文件')
        start_test = os.system(
            airtest_path + " run {script_name} --device Android://127.0.0.1:5037/?cap_method=JAVACAP".format(
                script_name=path+'/airtest_script/'+script_name
            )
        )
    except Exception as e:
        print(e)
    return


def backups():
    hld = win32gui.FindWindow(None, 'QQ')
    connect_device('Windows:///%d' % hld)
    wait(Template(r"{}tpl1601366059946.png".format(path + '/airtest_script/'), record_pos=(3.936, 1.446),
                  resolution=(312, 698)), timeout=10)
    touch(Template(r"{}tpl1601366059946.png".format(path + '/airtest_script/'), record_pos=(3.936, 1.446),
                   resolution=(312, 698)))
    touch(Template(r"{}tpl1601038539801.png".format(path + '/airtest_script/'), record_pos=(3.894, 0.948),
                   resolution=(308, 718)))
    sleep(1)
    hld = win32gui.FindWindow(None, '聊天记录备份与恢复')
    connect_device('Windows:///%d' % hld)
    touch(Template(r"{}tpl1601171543989.png".format(path + '/airtest_script/'), record_pos=(0.915, 0.337),
                   resolution=(650, 530)))
    return


def confirm_backups_for_pc():
    hld = win32gui.FindWindow(None, '聊天记录备份')
    connect_device('Windows:///%d' % hld)
    touch(Template(r"{}tpl1601367010576.png".format(path + '/airtest_script/'), record_pos=(1.682, 0.399),
                   resolution=(650, 530)))
    return


def confirm_backups():
    try:
        # 脚本名称
        script_name = "confirm_backups.air"
        # 启动之前删除上一次的日志文件
        my_file = './logs.txt'
        if os.path.exists(my_file):
            os.remove(my_file)
            print('删除日志文件')
        start_test = os.system(
           airtest_path + " run {script_name} --device Android://127.0.0.1:5037/?cap_method=JAVACAP".format(
                script_name=path + '/airtest_script/' + script_name
            )
        )
        return 'qq备份成功'
    except Exception as e:
        raise e


if __name__ == '__main__':
    # login()
    # adb_shell(delete_image)
    # adb_shell(cp_image)
    # start_qq_by_mobile()
    # backups()
    confirm_backups()
    # confirm_backups_for_pc()
