from flask import Flask, render_template, redirect, request, url_for
import c_main, main
import codecs

app = Flask(__name__)

@app.route('/')
@app.route('/<obj>')
def inputText(obj=None):
    animal = request.args.get('animal', None)
    pattern = request.args.get('pattern', None)
    print("IN INPUTTEXT() : ",animal,"&",pattern)
    return render_template('main.html',animal=animal, pattern=pattern, obj=obj)


@app.route('/translate', methods=['POST'])
def translate(animal=None, pattern=None, obj=None):
    if request.method == 'POST':
        temp = request.form['obj']
        fst_opt = request.form['animal']
        snd_opt = request.form['pattern']
        print("FIRST OPTIION : ", fst_opt)
        print("SECOND OPTION : ", snd_opt)
        if temp is not None:
            f = codecs.open(
                'C:/Users/LongLife_Hyun/PycharmProjects/flask_flask/GANda_ParkChangJo/data/birds/example_captions.txt',
                'w', 'utf-8')
            f.write(temp)
            f.close()
            if temp == "chicken":
                print("")
            elif temp == "bird":
                print("")
            elif temp == "붉은 털을 가진 여우":
                print("")
            else:
                print("START MACHINE RUNNING!")
                main.run_machine()
                print("AttnGAN MACHINE FINISHED")
                c_main.run_machine(snd_opt)
                print("CycleGAN MACHINE FINISHED")
    else:
        temp = None
    print("translate 나가기 직전 : ",fst_opt,"&",snd_opt)
    return redirect(url_for('inputText',animal=fst_opt, pattern=snd_opt, obj=temp))

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run()

