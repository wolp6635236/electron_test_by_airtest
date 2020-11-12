import os
import threading
import tkinter as tk

from action.run_action import RunAction
from base_package import driver_factory
from faker import Factory, Faker


class Root:
    def __init__(self):
        self.entry_usr_name = None
        self.entry_pass_word = None
        self.ck_1 = None
        self.ck_2 = None
        self.app_lists = None
        self.window = tk.Tk()
        self.window.title('快采伴侣')
        self.window.geometry('580x350')
        self.var_monitor_name = None
        self.entry_monitory_name = None
        self.text = None
        self.var_case_name = None
        self.close = None
        self.entry_case_name = None
        fake = Faker("zh_CN")
        self.name = fake.name()

    def quit_driver(self):
        self.close = os.popen('taskkill /im "电信*" /f')

    def upload_data(self):
        fake = Faker("zh_CN")
        self.name = fake.name()
        self.var_case_name.set(str(self.name)+'抢劫案件')
        self.var_monitor_name.set(self.name)

    def foo(self):
        # 用户名密码文本
        tk.Label(self.window, text='UserName:', font=('Arial', 11)).place(x=10, y=10)
        tk.Label(self.window, text='PassWord:', font=('Arial', 11)).place(x=300, y=10)

        # 案件名， 姓名
        tk.Label(self.window, text='CaseName:', font=('Arial', 11)).place(x=10, y=40)
        tk.Label(self.window, text='MonitorName:', font=('Arial', 11)).place(x=300, y=40)
        # 案件， 姓名文本框
        self.var_case_name = tk.StringVar()
        self.var_case_name.set(str(self.name)+'抢劫案件')
        self.entry_case_name = tk.Entry(self.window, textvariable=self.var_case_name, font=('Arial', 11))
        self.entry_case_name.place(x=110, y=40)

        self.var_monitor_name = tk.StringVar()
        self.var_monitor_name.set(self.name)
        self.entry_monitory_name = tk.Entry(self.window, textvariable=self.var_monitor_name, font=('Arial', 11))
        self.entry_monitory_name.place(x=400, y=40)
        # 用户文本框
        var_usr_name = tk.StringVar()
        var_usr_name.set('demo-data04')
        self.entry_usr_name = tk.Entry(self.window, textvariable=var_usr_name, font=('Arial', 11))
        self.entry_usr_name.place(x=110, y=10)
        # 密码框
        var_pass_word = tk.StringVar()
        var_pass_word.set('a1234567')
        self.entry_pass_word = tk.Entry(self.window, textvariable=var_pass_word, font=('Arial', 11), show='*')
        self.entry_pass_word.place(x=400, y=10)
        # App 类型
        tk.Label(self.window, text='AppType:', font=('Arial', 11), justify=tk.RIGHT).place(x=10, y=80)
        # App复选框
        self.ck_1 = tk.IntVar()
        ck1 = tk.Checkbutton(self.window, text='qq', variable=self.ck_1, command=self.check_check).place(x=100, y=80)

        self.ck_2 = tk.IntVar()
        ck2 = tk.Checkbutton(self.window, text='支付宝', variable=self.ck_2, command=self.check_check).place(x=140, y=80)
        # 启动按钮
        bt = tk.Button(self.window, text='启动', command=lambda: FnThread(self.start), width=5, height=1).place(x=10, y=120)
        # 清空按钮
        bt_delete = tk.Button(self.window, text='清空日志', command=lambda: FnThread(self.delete), width=8, height=1).place(x=80, y=120)
        # 关闭按钮
        bt_close = tk.Button(self.window, text='关闭浏览器', command=lambda: FnThread(self.quit_driver), width=11, height=1).place(x=160,
                                                                                                              y=120)
        # 重置数据
        bt_close = tk.Button(self.window, text='重置', command=lambda: FnThread(self.upload_data), width=11, height=1).place(x=260,
                                                                                                                              y=120)
        # 日志展示区域
        self.text = tk.Text(self.window, width=79, height=12)
        self.text.place(x=10, y=170)
        self.window.mainloop()

    def delete(self):
        self.text.delete(0.0, tk.END)

    def check_check(self):
        self.app_lists = []
        if self.ck_1.get() == 1:
            self.app_lists.append('QQ')
        if self.ck_2.get() == 1:
            self.app_lists.append('支付宝')

    def start(self):
        try:
            driver = driver_factory.ElectronFactory()
            self.text.delete(0.0, tk.END)
            self.insert_log('开始执行任务')
            username = self.entry_usr_name.get()
            password = self.entry_pass_word.get()
            case_name = self.entry_case_name.get()
            monitor_name = self.entry_monitory_name.get()

            print(username, password, self.app_lists)
            self.insert_log(username)
            self.insert_log(password)

            self.insert_log('执行的app是:')
            self.insert_log(str(self.app_lists))

            action = RunAction(driver=driver)
            case_text = action.test_case(
                username_text=username,
                password_text=password,
                case_name=case_name,
                monitor_name=monitor_name,
                app_type=self.app_lists
            )
            self.insert_log(case_text)
            login_qq = action.login_qq()
            self.insert_log(login_qq)
        except Exception as e:
            print(e)
            if 'NoneType' in str(e):
                self.insert_log('####你没有勾选AppType####')
            self.insert_log('#' * 30)
            self.insert_log(str(e))
            self.insert_log('#' * 30)

    def insert_log(self, text):
        self.text.insert('insert', text + '\n')


class FnThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)


if __name__ == '__main__':
    f = Root()
    f.foo()
