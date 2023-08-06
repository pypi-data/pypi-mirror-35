# 项目：Pytohon工具包
# 模块：安装模块
# 作者：黄涛
# License:GPL
# Email:huangtao.sh@icloud.com
# 创建：2015-09-03 16:02
# 修改：2016-03-08 16:47
# 修改：2016-04-13 21:07
# 修改：2016-9-7 将通过shell调用pip命令调整为直接引入pip模块
# 修改：2018-7-12 调整参数处理方法

import os
import sys
import re
from orange import R, Path, info, read_shell, command, arg
from orange.deploy import Ver, run_pip, run_setup, pyclean


RootPath = '~/OneDrive/pylib'
Pattern = R / r'\d+(\.\d+)*([ab]\d+)?'


def find_ver(path):
    v = Pattern.search(path.name)
    if v:
        return Ver(v.group())


@command(allow_empty=True)
@arg('packages', help='python package', nargs='*', metavar='package')
@arg('-p', '--path', default=RootPath, help='指定的目录')
@arg('-d', '--download', help='默认的包目录', action='store_true')
@arg('-u', '--upgrade', help='升级系统中已安装的软件包', action='store_true')
def py_setup(packages=None, path=None, download=None, upgrade=False):
    root = Path(path)
    if download:
        run_pip('download', '-d', str(root), *packages)
        # exec_cmd('pip','download -d %s %s'%(Path(path),
        #                      " ".join(packages)))
    elif upgrade:
        pip = 'pip' if os.name == 'nt' else 'pip3'
        pkglist = read_shell('%s list -o' % (pip))
        for line in pkglist:
            pkg = line.split()
            if pkg:
                run_pip('install', '-U', pkg[0])
    else:
        if packages:
            pkgs = []
            for pkg in packages:
                pkg_path, pkg_ver = None, Ver('0.0')
                for file in root.glob('%s-*' % (pkg)):
                    info('Process file %s' % (file.name))
                    ver = find_ver(file)
                    info('Get ver %s' % (ver))
                    if ver > pkg_ver:
                        pkg_path = file
                        pkg_ver = ver
                if pkg_path:
                    if Path(pkg_path).lsuffix in ('.zip', '.whl', '.gz', '.tar'):
                        pkgs.append(str(pkg_path))
                        info('Add file %s' % (pkg_path.name))
                    else:
                        print('%s 不是正常的包文件' % (pkg_path.name))
                else:
                    pkgs.append(pkg)
                    info('Add pkg %s' % (pkg))
            os.chdir('%s' % (root))
            run_pip('install', *pkgs)
            # exec_cmd('pip','install %s'%(" ".join(pkgs)))
        else:
            if Path('setup.py').exists():
                run_setup('install')
                pyclean()
            else:
                print('Can''t find the file setup.py!')


if __name__ == "__main__":
    py_setup()
