from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('input_info.html') ## (1)

@app.route('/result', methods = ['POST', 'GET']) ## (2)
def result():
    if request.method == 'POST': ## (3)
        result = dict()
        result['Name'] = request.form.get('Name')
        result['Student_Number'] = request.form.get('Student_Number')
        result['gender'] = request.form.get('gender')
        result['Major'] = request.form.get('Major')
        result['checkbox'] = ''
        result_list = []
        if request.form.get('python'):
             result_list.append('python')
        if request.form.get('java'):
             result_list.append('java')
        if request.form.get('C++'):
             result_list.append('C++')

        for x in result_list:
            result['checkbox'] +=  x 
            if x != result_list[-1]:
                result['checkbox'] +=  ', ' 


        return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)  포트변경시 사용
