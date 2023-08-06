import copy
import datetime
import time
from typing import Iterable, Tuple

import cv2
from airtest.core.helper import G

from AutoWSGR.constants.custom_exceptions import ImageNotFoundErr
from AutoWSGR.constants.other_constants import INFO1
from AutoWSGR.utils.api_image import (MyTemplate, convert_position,
                                      locateCenterOnImage)
# from AutoWSGR.utils.logger import get_time_as_string, logit
from AutoWSGR.utils.math_functions import CalcDis
from AutoWSGR.utils.new_logger import Logger

from .android_controller import AndroidController
from .windows_controller import WindowsController


class Emulator():
    """模拟器管理单位,可以用于其它游戏
    """

    def __init__(self, config, logger:Logger):
        # 获取设置，初始化windows控制器
        self.config = config
        self.logger = logger
        self.Windows = WindowsController(config, logger)

        # 初始化android控制器
        self.Windows.ConnectAndroid()
        self.update_screen()
        self.config.resolution = self.screen.shape[:2]
        self.config.resolution = self.config.resolution[::-1]  # 转换为 （宽x高）
        self.logger.info(f"resolution:{str(self.config.resolution)}")
        self.Android = AndroidController(config, logger)

    # @logit()
    def update_screen(self):
        """记录现在的屏幕信息,以 numpy.array 格式覆盖保存到 RD.screen
        """
        self.screen = G.DEVICE.snapshot(filename=None, quality=99)

    def get_screen(self, resolution=(1280, 720), need_screen_shot=True):
        if (need_screen_shot):
            self.update_screen()
        return cv2.resize(self.screen, resolution)

    def get_pixel(self, x, y, screen_shot=False) -> list:
        """获取当前屏幕相对坐标 (x,y) 处的像素值

        Args:
            x (int): [0, 960)
            y (int): [0, 549)

        Returns:
            list[]: RGB 格式的像素值
        """
        if (screen_shot):
            self.update_screen()
        if (len(self.screen) != 540):
            self.screen = cv2.resize(self.screen, (960, 540))
        return [self.screen[y][x][2], self.screen[y][x][1], self.screen[y][x][0]]

    def check_pixel(self, position, bgr_color, distance=30, screen_shot=False) -> bool:
        color = self.get_pixel(*position, screen_shot)
        color.reverse()
        return CalcDis(color, bgr_color) < distance ** 2

    def locateCenterOnScreen(self, query: MyTemplate, confidence=0.85, this_methods=None):
        """从屏幕中找出和模板图像匹配度最高的矩阵区域的中心坐标
            参考 locateCenterOnImage
        Returns:
            如果找到返回一个二元组表示绝对坐标

            否则返回 None
        """
        if this_methods is None:
            this_methods = ["tpl"]
        return locateCenterOnImage(self.screen, query, confidence, this_methods)

    # @logit()
    def get_image_position(self, image, need_screen_shot=1, confidence=0.85, this_methods=None):
        """从屏幕中找出和多张模板图像匹配度超过阈值的矩阵区域的中心坐标,如果有多个,返回第一个
            参考 locateCenterOnScreen
        Args:
            need_screen_shot (int, optional): 是否重新截取屏幕. Defaults to 1.
        Returns:
            如果找到:返回一个二元组表示相对坐标 (相对 960x540 屏幕)

            否则返回 None
        """
        if this_methods is None:
            this_methods = ["tpl"]
        images = image
        if (not isinstance(images, Iterable)):
            images = [images]
        if (need_screen_shot == 1):
            self.update_screen()
        for image in images:
            res = self.locateCenterOnScreen(image, confidence, this_methods)
            if (res is not None):
                return convert_position(res[0], res[1], self.config.resolution, mode='this_to_960')
        return None

    def get_images_position(self, images, need_screen_shot=1, confidence=0.85, this_methods=None):
        """同 get_image_position
        """
        if this_methods is None:
            this_methods = ["tpl"]
        return self.get_image_position(images, need_screen_shot, confidence, this_methods)

    # @logit()
    def image_exist(self, images, need_screen_shot=1, confidence=0.85, this_methods=None):
        """判断图像是否存在于屏幕中
        Returns:
            bool:如果存在为 True 否则为 False 
        """
        if this_methods is None:
            this_methods = ["tpl"]
        if not isinstance(images, list):
            images = [images]
        if need_screen_shot:
            self.update_screen()
        return any(self.get_image_position(image, 0, confidence, this_methods) is not None for image in images)

    def images_exist(self, images, need_screen_shot=1, confidence=0.85, this_methods=None):
        """判断图像是否存在于屏幕中
        Returns:
            bool:如果存在为 True 否则为 False 
        """
        if this_methods is None:
            this_methods = ["tpl"]
        return self.image_exist(images, need_screen_shot, confidence, this_methods)

    # @logit()
    def wait_image(self, image: MyTemplate, confidence=0.85, timeout=10, gap=.15, after_get_delay=0, this_methods=None):
        """等待一张图片出现在屏幕中,置信度超过一定阈值(支持多图片)

        Args:
            timeout (int, optional): 最大等待时间. Defaults to 10.
        Returns:
            如果在 timeout 秒内发现,返回一个二元组表示其相对(960x540 屏幕)位置

            否则返回 False
        """
        if this_methods is None:
            this_methods = ["tpl"]
        if (timeout < 0):
            raise ValueError("arg 'timeout' should at least be 0 but is ", str(timeout))
        StartTime = time.time()
        while (True):
            x = self.get_image_position(image, 1, confidence, this_methods)
            if (x != None):
                time.sleep(after_get_delay)
                return x
            if (time.time()-StartTime > timeout):
                time.sleep(gap)
                return False
            time.sleep(gap)

    # @logit()
    def wait_images(self, images=None, confidence=0.85, gap=.15, after_get_delay=0, timeout=10):
        """等待一系列图片中的一个在屏幕中出现

        Args:
            images (list, optional): 很多图片,可以是列表或字典. Defaults to [].
            confidence (_type_, optional): 置信度. Defaults to 0.85.
            timeout (int, optional): 最长等待时间. Defaults to 10.

        Raises:
            TypeError: image_list 中有不合法参数

        Returns:
            None: 未找到任何图片
            a number of int: 第一个出现的图片的下标(0-based) if images is a list
            the key of the value: if images is a dict
        """
        if images is None:
            images = []
        images = copy.copy(images)
        if (isinstance(images, MyTemplate)):
            images = [images]
        if isinstance(images, (list, Tuple)):
            for i in range(len(images)):
                images[i] = (i, images[i])
        if (isinstance(images, dict)):
            images = images.items()

        if (timeout < 0):
            raise ValueError("arg 'timeout' should at least be 0 but is ", str(timeout))

        StartTime = time.time()
        while (True):
            self.update_screen()
            for res, image in images:
                if self.image_exist(image, 0, confidence):
                    time.sleep(after_get_delay)
                    return res
            time.sleep(gap)
            if (time.time() - StartTime > timeout):
                return None

    def wait_images_position(self, images=None, confidence=0.85, gap=.15, after_get_delay=0, timeout=10):
        """等待一些图片,并返回第一个匹配结果的位置

        参考 wait_images     
        """
        if images is None:
            images = []
        if (not isinstance(images, Iterable)):
            images = [images]
        rank = self.wait_images(images, confidence, gap, after_get_delay, timeout)
        if rank is None:
            return None
        return self.get_image_position(images[rank], 0, confidence)

    # @logit(level=INFO1)
    def click_image(self, image, must_click=False, timeout=0, delay=0.5):
        """点击一张图片的中心位置
        Args:
            image (MyTemplate): 目标图片
            must_click (bool, optional): 如果为 True,点击失败则抛出异常. Defaults to False.
            timeout (int, optional): 等待延时. Defaults to 0.
            delay (float, optional): 点击后延时. Defaults to 0.5.

        Raises:
            NotFoundErr: 如果在 timeout 时间内未找到则抛出该异常
        """
        pos = self.wait_images_position(image, gap=.03, timeout=timeout)
        if (pos == False):
            if (must_click == False):
                return False
            else:
                raise ImageNotFoundErr(f"Target image not found:{str(image.filepath)}")

        self.Android.click(*pos, delay=delay)
        return True

    def click_image(self, image: MyTemplate, must_click=False, timeout=0, delay=0.5):
        """点击一张图片的中心位置
        Args:
            image (MyTemplate): 目标图片
            must_click (bool, optional): 如果为 True,点击失败则抛出异常. Defaults to False.
            timeout (int, optional): 等待延时. Defaults to 0.
            delay (float, optional): 点击后延时. Defaults to 0.5.

        Raises:
            NotFoundErr: 如果在 timeout 时间内未找到则抛出该异常
        """
        if (timeout < 0):
            raise ValueError("arg 'timeout' should at least be 0 but is ", str(timeout))
        if (delay < 0):
            raise ValueError("arg 'delay' should at least be 0 but is ", str(delay))
        pos = self.wait_image(image, timeout=timeout)
        if pos is None:
            if (must_click == False):
                return False
            else:
                raise ImageNotFoundErr(f"Target image not found:{str(image.filepath)}")

        self.Android.click(*pos, delay=delay)
        return True

    def click_images(self, images, must_click=False, timeout=0, delay=0.5):
        """点击一些图片中第一张出现的,如果有多个,点击第一个
        """
        self.click_image(images, must_click, timeout)

    def log_screen(self, need_screen_shot=False):
        """向默认数据记录路径记录当前屏幕数据,带时间戳保存,960x540大小
        Args:
            need_screen_shot (bool, optional): 是否新截取一张图片. Defaults to False.
        """
        if (need_screen_shot):
            self.update_screen()
        screen = copy.deepcopy(self.screen)
        screen = cv2.resize(screen, (960, 540))
        self.logger.log_image(image=screen, name=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
