from flask import Flask, render_template, request
#from camera import Camera

app = Flask(__name__ ,static_folder='./templates/videoes')


@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/index2')
def index2():
    return render_template('index2.html')
@app.route('/index3')
def index3():
    return render_template('index3.html')
@app.route('/index4')
def index4():
    return render_template('index4.html')
@app.route('/index5')
def index5():
    return render_template('index5.html')

# 入力値の表示ページ
@app.route('/', methods=['GET', 'POST'])
def result():
    # index.htmlのinputタグ内にあるname属性itemを取得し、textに格納した
    text = request.form.get('item')
    if text == '1':
        url="videoes/fa_part1.mp4"
        times="381"
    elif text == '3':
        url="videoes/fa_part2.mp4"
        times="377"
    elif text == '4':
        url="videoes/fa_enchou.mp4"
        times="62a"
    elif text == '5':
        url="videoes/fa_part3_1.mp4"
        times="596"
    elif text == '7':
        url="videoes/fa_part3_2.mp4"
        times="332"
    elif text == '6':
        url="videoes/fa_enchou.mp4"
        times="62b"
    elif text == '9':
        url="videoes/fa_part4.mp4"
        times="277"
    elif text == '10':
        url="videoes/fa_enchou.mp4"
        times="62c"


    if request.method == 'POST':
        print("post")
        # return render_template('base.html')
        return render_template('result.html', url = url,times=times)

    # POSTメソッド以外なら、index.htmlに飛ばす
    else:
        print("else")

if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True)#並列処理