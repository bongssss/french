from flask import Flask, render_template, request

from deep_translator import GoogleTranslator

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    direction = request.form['direction']
    
    try:
        if direction == 'E2F':
            translator = GoogleTranslator(source='en', target='fr')
            translated_text = translator.translate(text)
            return render_template('result.html', translated_text=translated_text, direction='French')
        elif direction == 'F2E':
            translator = GoogleTranslator(source='fr', target='en')
            translated_text = translator.translate(text)
            return render_template('result.html', translated_text=translated_text, direction='English')
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template('error.html', error_message=error_message)
    
@app.route('/result')
def result():
    # This route is for displaying the result.html template
    # It's not explicitly called in the provided code but required for rendering the result template
    return render_template('result.html')  # Provide a valid response

@app.route('/error')
def error():
    # This route is for displaying the error.html template
    # It's not explicitly called in the provided code but required for rendering the error template
    return render_template('error.html')  # Provide a valid response

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True)
