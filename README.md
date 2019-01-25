# flask-js-test
flask与js前后端同步的尝试：
前端输入一个值，与后端生成的随机数相加后，返回给前端。

前端'calculate'按钮调用'click'时间，在js中读取`/calculate`路径下的json回传。
后端接到`/calculate`下的请求json，计算完之后再通过json传到前端。

变量：
- 前端定义：calculate, input-a, result，作为前端html标签；b为json主键之一，由html定义后，js使用。
- 后端定义：result, in_a，用于flask框架的传递；request.args.get()用于取json中的主键。
