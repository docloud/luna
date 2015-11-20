# 手册

## 容器

每一个由Luna运行起来的项目都会被视作一个容器，这个容器包括，

### 运行时的配置管理

``` python
from luna import config # 从当前目录加载配置文件app.yaml
```

### 容器内 Debug 环境

``` bash
> luna shell
```

会启动一个IPython交互式解释器，这个解释器默认载入了一些有用的函数和变量。

| 函数/变量名 | 类             | 描述                        |
| ------ | ------------- | ------------------------- |
| app    | Flask         | Flask Application类        |
| config | DefaultConfig | 配置项管理类                    |
| logger | DebugLogger   | Flask Application Logger类 |
| http   | HTTPClient    | 访问应用API的HTTP客户端           |