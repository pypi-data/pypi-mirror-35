# coding=utf-8
import os

def play(filename=''):
    """
    功能：播放filename指定的音频、视频文件。

    参数 filename 是当前目录下期望播放的音频、视频文件的名字，
    返回：无。
    """

    if not filename:
        return -1

    filepath = os.path.abspath(filename)
    os.system(filepath)

def main():
    play('test.wav')

if __name__ == '__main__':
    main()
