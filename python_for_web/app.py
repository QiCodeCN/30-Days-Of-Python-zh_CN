# 导入框架模块 flask
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # 停止缓存静态文件

@app.route('/') # 通过这个装饰器创建主(跟)路由
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '挑战30天学完Python'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '挑战30天学完Python'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = '文本分析'
    if request.method == 'GET': # 请求方法为GET的处理逻辑
         return render_template('post.html', name = name, title = name)
    if request.method =='POST': # 请求方法为POST时候获取请求数据并指向结果页面
        content = request.form['content']
        print(content)
        return render_template('result.html', result = content)

if __name__ == '__main__':
    # 部署运行
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)