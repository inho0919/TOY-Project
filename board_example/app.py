from flask import Flask, render_template, request, redirect
from API import korea

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/board_list')
def board_list():
  return render_template('boards.html')

#Korea Server =============================

@app.route('/board_kr')
def korean():
  b = korea.read()
  for i in range(0, len(b)):
    for j in range(0, len(b)):
      if(i < j):
        temp = b[i]
        b[i] = b[j]
        b[j] = temp
  return render_template('korea.html', b=b)

@app.route('/write_kr')
def write():
  return render_template('kor_write.html')

@app.route('/post1', methods=['POST'])
def post1():
  ids = request.form['ids']
  title = request.form['title']
  content = request.form['content']
  korea.create(ids, title , content)
  return redirect('/board_kr')

@app.route('/text_kr', methods=['GET'])
def text_kr():
  no = request.args.get('no')
  total = korea.datas(str(no))
  return render_template('text_kor.html', total = total)

@app.route('/update', methods=['GET'])
def update():
  ups = request.args.get('no')
  total = korea.datas(str(ups))
  return render_template('update.html', total= total)

@app.route('/posts1', methods=['POST'])
def posts1():
  no = request.form['no']
  num = str(no)
  ids = request.form['ids']
  title = request.form['title']
  content = request.form['content']
  a = korea.update(num, ids, title, content)
  print(num)
  print(ids)
  print(title)
  print(content)
  return redirect('/board_kr')

@app.route('/delete')
def delete():
  dels = request.args.get('no')
  korea.delete(str(dels))
  return redirect('/board_kr')
  
#English Server ============================= 

@app.route('/board_en')
def english():
  return render_template('english.html')


#Deutsch Server =============================

@app.route('/board_de')
def deutsch():
  return render_template('deutsch.html')

#Developer's Note =============================
@app.route('/developenote')
def develop():
  return render_template('develops.html')

@app.route('/passwd', methods=['POST'])
def passwd():
  pwd = request.form['pwd']
  if pwd == 'godwjd!':
    return redirect('/note')
  else:
    return redirect('/')

@app.route('/note')
def note():
  return render_template('corner.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)
