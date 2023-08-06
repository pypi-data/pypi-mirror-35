import os

config = {
    # Web应用端口
    "port": 3055,
    "middleware": {
        # 框架内置中间件
        "list": [
            "config_middleware",
            "http_middleware",
            "static_middleware",
            "cookie_middleware",
            "session_middleware",
            "router_middleware",
            "mvc_middleware",
            "template_middleware",
            "response_middleware"],
        # 中间件目录
        "path": "{path}/../middleware".format(path=os.path.dirname(os.path.realpath(__file__))), # NOQA
    },
    "controller": {
        # 控制器目录
        "path": "{path}/controller".format(path=os.getcwd())
    },
    "router": {
        # 路由模式
        "model": 1,
        # 默认控制器
        "controller": "home",
        # 默认action
        "action": "index"
    },
    "view": {
        # 视图目录
        "path": "{path}/view".format(path=os.getcwd()),
        # 视图后缀名
        "suffix": "html"
    },
    "static": {
        # 静态文件后缀名
        "suffix": ["html", "jpg", "ico", "png", "css", "json", "js", "gif", "txt"], # NOQA
        # 静态文件路径
        "path": "{path}/static".format(path=os.getcwd()),
    },
    "session": {
        "id": "autumn_session_id"
    },
    "config": {
        "path": "{path}/config".format(path=os.getcwd()),
        "name": "config"
    }
}
