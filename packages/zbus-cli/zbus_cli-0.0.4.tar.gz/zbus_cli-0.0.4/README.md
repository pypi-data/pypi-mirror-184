# zbus命令行调试工具

## 下载或更新
+ 下载: sudo pip install zbus_cli
+ 更新: sudo pip install --upgrade zbus_cli

## 上传python包
1. python3 -m build
2. python3 -m twine upload  dist/*'
3. 上传 
+ username: token(首尾需加双下划线)
+ password: pypi-AgEIcHlwaS5vcmcCJDM4ZjYxODhhLWExZDktNGM4Yi1hYTY1LTc3OTc5ODM0ZDNiMwACKlszLCI2MzEwNTE3NS00OGZkLTRhZTctOTkwOS0wYzkxNzcxODY4ODYiXQAABiDSZYHFo8sACiQKY8puYVcQGdfV-TG5FPPmvLwUIQQRhg

## 版本记录
+ 0.0.4: service call显示响应时间 
+ 0.0.3: 去除topic delay无关打印
+ 0.0.2: 新增topic delay功能
+ 0.0.1: 具备topic echo, hz, pub和service call功能