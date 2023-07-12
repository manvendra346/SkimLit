from flask import Flask, render_template, request
import tensorflow as tf
import os

app = Flask(__name__)
model = tf.keras.models.load_model(os.getcwd()+'\VS random'+'\skimlit_savedmodel')
def split_char(sentence):
    return " ".join(list(sentence))

@app.route('/', methods=['GET', 'POST'])
def process_text():
    flag=False
    if request.method == 'POST':
        # Get the input text from the form
        input_text = request.form['input_text']
        input_text = str(input_text)
        input_sentences = input_text.split('.')
        input_sentences = input_sentences[:-1]

        input_chars = [ split_char(sentence) for sentence in input_sentences ]
        input_chars = tf.convert_to_tensor(input_chars)
        input_chars = tf.reshape(input_chars, shape=(-1,1))
        input_sentences = tf.convert_to_tensor(input_sentences)
        input_sentences = tf.reshape(input_sentences,shape=(-1,1))

        total_line = []
        x = len(input_sentences)
        for i in range(x):
            total_line.append(x)
        input_tl = tf.one_hot(total_line, depth=20)
        line_no = list(range(1,x+1))
        input_ln = tf.one_hot(line_no,depth=15)


        predictions = model.predict((input_sentences,input_chars,input_ln, input_tl))
        predictions = tf.math.argmax(predictions, axis=1)
        input_sentences = input_text.split('.')
        output_list = ['BACKGROUND', 'CONCLUSIONS', 'METHODS', 'OBJECTIVE', 'RESULTS']
        output_dict = {'BACKGROUND':'', 'CONCLUSIONS':'', 'METHODS':'', 'OBJECTIVE':'', 'RESULTS':''}
        for label, sentence in zip(predictions, input_sentences):
            output_dict[output_list[label]] += '. '+sentence
        
        flag=True
        bac,con,met,obj,res = output_dict['BACKGROUND'],output_dict['CONCLUSIONS'],output_dict['METHODS'],output_dict['OBJECTIVE'],output_dict['RESULTS']
        
        # Render the template with the processed text
        return render_template('skimlit.html',flag=flag, BACKGROUND=bac, CONCLUSIONS=con, METHODS=met, OBJECTIVE=obj, RESULTS=res)
    
    # Render the template with no processed text
    return render_template('skimlit.html')

if __name__ == '__main__':
    app.run()
    # print(os.getcwd())