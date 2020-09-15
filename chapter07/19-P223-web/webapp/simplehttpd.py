# http.server, simplehttp.py

# 导入HTTP服务器和CGI模块
from http.server import HTTPServer,CGIHTTPRequestHandler

# 配置一个简单的httpserver

# 指定一个端口
port = 8083

# 创建一个HTTP服务器
httpd = HTTPServer(('',port),CGIHTTPRequestHandler)

# 显示一个友好的消息
print('Starting simple_httpd on port:' + str(httpd.server_port))

# 并启动服务器
httpd.serve_forever()