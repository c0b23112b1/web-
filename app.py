from flask import Flask, render_template, request, jsonify
import psycopg2

def get_connection():
    try:
        con = psycopg2.connect(
            host="localhost",       # 接続先ホスト
            port=5432,              # PostgreSQLのデフォルトポート
            database="mydb",        # データベース名
            user="postgres",          # ユーザー名
            password="yourpassword"   # パスワード
        )
        print("接続に成功しました")
        return con
    except Exception as e:
        print("接続に失敗しました:", e)
        return None

app = Flask(__name__)
con = get_connection()



@app.route('/')
def home():
    return render_template('menu.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)