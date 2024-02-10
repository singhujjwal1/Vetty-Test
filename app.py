from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/read-file/<filename>', methods=['GET'])
def read_file(filename='file1.txt'):
    try:
        start_line = int(request.args.get('start_line', 1))
        end_line = int(request.args.get('end_line', -1))

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if 0 < start_line <= len(lines) and 0 < end_line <= len(lines):
            content = ''.join(lines[start_line-1:end_line])
        else:
            content = ''.join(lines)

        return render_template('file_content.html', content=content)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)