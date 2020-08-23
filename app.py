from flask import Flask, request, render_template
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    if request.method == 'GET':
        return render_template('index.html')
    else:
        form_input = request.form['input']
        morph = nltk.word_tokenize(form_input)
        pos = nltk.pos_tag(morph)
        
        for i in pos:
            # if 'VB'or'VBD'or'VBG'or'VBN'or'VBP'or'VBZ' in i:
            if 'VB' in i:
                a.append(i)
            elif 'VBD' in i:
                b.append(i)
            elif 'VBG' in i:
                c.append(i)
            elif 'VBN' in i:
                d.append(i)
            elif 'VBP' in i:
                e.append(i)
            elif 'VBZ' in i:
                f.append(i)

        return render_template('index.html',pos_a=a, pos_b=b, pos_c=c, pos_d=d, pos_e=e, pos_f=f ,form_input=form_input)


if __name__ == '__main__':
    app.run(debug=True)

