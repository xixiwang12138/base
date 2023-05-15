
import sys

from prettytable import PrettyTable
# reload(sys)
# sys.setdefaultencoding('utf8')

table = PrettyTable(['配置' ,'白名单' ,'黑名单'])
table.add_row(['禁止空Referer' ,'.baidu.com' ,'-,-.baidu.com'])
table.add_row(['允许空Referer' ,',.baidu.com' ,'-.baidu.com'])

print(table)