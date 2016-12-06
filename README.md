# 基础工具集

## 输出文件检测工具check_file.py

基于python3
检测指定文件是否存在&及时更新，失败发送报警
配合crontab使用效果更佳

### 调用方式

python3 check_file.py [conf_file = conf.yaml]

### 输出

如果检测通过,输出OK
否则输出短信内容及短信接口返回值

### 配置

可通过脚本的第一个参数指定配置文件路径,默认为同级目录下的conf.yaml

可配置项: 
- project_name:项目名称，出现在短信内容里，辨别各个项目
- files_path:待检测文件的绝对路径，可配置多个文件
- refresh_time:文件更新阈值，文件时间戳与当前时间差值大于此阈值发送报警
- admins:报警接收人，写手机号。线上项目默认加井哲天、罗景

配置可参照conf.yaml.defualt填写
