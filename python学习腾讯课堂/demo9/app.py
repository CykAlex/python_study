#-*-coding;utf-8-*-
import web
urls = ('/','Index',#路由：/=用户访问的页面也就是首页，Index用来响应该请求的方法，不是数字就行
'/qiangzi','Qiangzi',
'/upload','Upload',
)
app = web.application(urls,globals())
render = web.template.render('templates')

class Index:
    def GET(self):#方法是用户请求的方式
        return render.index()
class Qiangzi:
    def GET(self):
        return 'Hello qiangzi'
class Upload:
    def POST(self):
        i = web.input(file={})
        filename = i.file.filename
        file = i.file.file.read()
        with open('static/%s' %filename,'wb') as fn:
            fn.write(file)
        return '<a href="static/%s">gaiwenjian</a>' %filename

if __name__=='__main__':
    app.run()