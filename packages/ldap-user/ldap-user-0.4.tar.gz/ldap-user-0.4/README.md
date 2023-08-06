# ldap_user

## required
yum install openldap-devel
pip install python-ldap

## 0.4
jy-ldap-config 支持 -e 将生成的配置文件，设置环境变量

## 0.3
add_user 传入的参数支持为unicode自动进行encode

## 0.2
初步功能实现。可读取配置，可命令行生存配置。可建用户，删用户，密码校验，锁定解锁用户

## 0.1
init