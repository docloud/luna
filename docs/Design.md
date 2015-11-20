# Design Pattern

## Singleton

### 项目中应用
```python
# luna/__init__.py
config = DefaultConfig.load()
app = Flask(config["name"])
app.config.update(config["app"])
logger = app.logger
```
`config`, `app`, `logger`全局唯一实例

## Decorator
Flask装饰器
- `@app.route()` 函数绑定到URL
- `@app.before_request` 函数在请求前调用
- `@app.after_request` 函数在请求结束后调用
- `@app.teardown_request` 函数在请求结束后调用，即使遇到了异常。

框架内自定义装饰器
- `jsonify`
- `route`
- `use_args`
- `use_kwargs`


## 拓展阅读
[IBM Document-设计模式第一部分: 单例模式](https://www.ibm.com/developerworks/cn/java/j-lo-Singleton/)
[维基百科-单例模式](https://zh.wikipedia.org/wiki/单例模式)
[维基百科-Decorator Pattern](https://zh.wikipedia.org/zh/修饰模式)
