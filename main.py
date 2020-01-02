from flask import Flask, request, jsonify
import json
 
app = Flask(__name__)
app.debug = True
 
 
@app.route('/msg/sed/',methods=['post'])
def add_stu():
    if  not request.data:   #检测是否有数据
        return ('fail')
    r = request.data.decode('utf-8')
    #获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
    sed_json = json.loads(r)
    #把区获取到的数据转为JSON格式。
    return jsonify(sed_json)
    #返回JSON数据。
 
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8081)