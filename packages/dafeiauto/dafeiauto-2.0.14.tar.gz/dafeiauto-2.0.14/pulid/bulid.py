#!/usr/bin/env python
# coding=utf-8
import os, tarfile
def make_targz(output_filename, source_dir):
    """
    逐个添加文件打包，未打包空子目录。可过滤文件。
    如果只打包不压缩，将"w:gz"参数改为"w:"或"w"即可。
    :param output_filename:  文件名
    :param source_dir: 需要打包的路径
    :return:
    """
    if os.path.exists(os.path.join(source_dir + '\\pulid', 'dafeiauto.tar.gz')):
        os.remove(os.path.join(source_dir + '\\pulid', 'dafeiauto.tar.gz'))
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        tar.close()
        print("Successfully bulid package of dafeiauto.tar.gz...")

def bulid():
    path = os.path.dirname(os.path.realpath('.'))
    make_targz("dafeiauto.tar.gz", path)

if __name__ == "__main__":
    bulid()