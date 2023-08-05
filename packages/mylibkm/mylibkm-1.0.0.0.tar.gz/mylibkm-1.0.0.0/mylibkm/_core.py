import ctypes
import win32api
import win32con
import time
from PyQt5.QtCore import QThread, QWaitCondition, QMutex
from constants import const


class ScriptInter(QThread):
    # 构造函数
    def __init__(self):
        super().__init__()
        self.isBlock = False
        self.isCancel = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    # 阻塞
    def block(self):
        self.isBlock = True
        const.status['paused'] = True
        const.UI.ui_signal.emit('status_pause', '暂停执行')

    # 恢复
    def resume(self):
        self.isBlock = False
        self.cond.wakeAll()
        const.status['paused'] = False
        const.UI.ui_signal.emit('status_pause', '继续执行')

    # 取消
    def cancel(self):
        self.isCancel = True
        const.status['paused'] = False
        const.status['running'] = False
        const.UI.ui_signal.emit('status_run', '完成执行')

    # 恢复
    def begin(self):
        const.status['running'] = True
        const.UI.ui_signal.emit('status_run', '开始执行')

    # 恢复
    def end(self):
        const.status['running'] = False
        const.UI.ui_signal.emit('status_run', '完成执行')

    #
    def mouse(self, action, x=-1, y=-1):
        # 线程锁on
        self.mutex.lock()
        if self.isBlock:
            self.cond.wait(self.mutex)
        # TODO=>待优化，应该一次结束后面的动作不再判断，而不是每个动作里都判断
        if self.isCancel:
            # TODO=>
            # self.valueChange.emit(0)
            return

        time.sleep(0.1)

        if action == 'move_to' and x != -1 and y != -1:
            # 挪动鼠标 普通做法
            ctypes.windll.user32.SetCursorPos(x, y)

        # 约定 [-1, -1] 表示鼠标保持原位置不动, 非move_to的动作就不需要传入坐标值，默认-1 -1
        elif action == 'left_single_click':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        elif action == 'left_double_click':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        elif action == 'left_long_press':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        elif action == 'left_long_up':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        elif action == 'right_single_click':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        elif action == 'right_double_click':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        elif action == 'right_long_press':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        elif action == 'right_long_up':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

        elif action == 'middle_single_click':
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
        elif action == 'middle_double_click':
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
        elif action == 'middle_long_press':
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
        elif action == 'middle_long_up':
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)

        elif action == 'wheel_up':
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA, 0)
        elif action == 'wheel_down':
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -win32con.WHEEL_DELTA, 0)

        # 线程锁off
        self.mutex.unlock()

    #
    def keyboard(self, action, key_name):
        # 线程锁on
        self.mutex.lock()
        if self.isBlock:
            self.cond.wait(self.mutex)
        # TODO=>待优化，应该一次结束后面的动作不再判断，而不是每个动作里都判断
        if self.isCancel:
            # TODO=>
            # self.valueChange.emit(0)
            return

        time.sleep(0.1)

        key_code = const.key_dict[key_name]
        # keybd_event函数的第3个参数为0表示按下，为win32con.KEYEVENTF_KEYUP表示弹起；第2个参数和第4个参数都默认0就行
        if action == 'key down':
            win32api.keybd_event(key_code, 0, 0, 0)
        elif action == 'key up':
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

        # 线程锁off
        self.mutex.unlock()

    # 特别注意，线程的开始不是直接调用run方法，而是调用start；否则仍然是阻塞状态，就像没使用线程一样的普通调用
    # 要发挥线程的效果就必须使用start()来开始运行线程任务
    # 运行(入口)
    def run(self):
        pass
