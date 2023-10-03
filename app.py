from flask import Flask, render_template
from datetime import datetime
import classes

app = Flask(__name__, template_folder='templates')


@app.route('/home')
def index():
    return render_template('index.html', timestamp={'hora': datetime.now()})


@app.route('/onoff')
def onoff():
    cpc_list = [
        {'swmdl': '743', 'cpcName': 'Z45FA8', 'cpcStatus': 'OPERATING'},
        {'swmdl': '700', 'cpcName': 'Z12345', 'cpcStatus': 'OPERATING'},
        {'swmdl': '755', 'cpcName': 'ZABCDE', 'cpcStatus': 'OPERATING'},
    ]

    cpc_profile_dic = {
        'Z45FA8': [{'swmdl_pico': '843', 'swmdl_cruzeiro': '743'}],
        'Z12345': [{'swmdl_pico': '800', 'swmdl_cruzeiro': '700'}],
        'ZABCDE': [{'swmdl_pico': '855', 'swmdl_cruzeiro': '755'}],
    }

    cec_lpar_dic = {
        'Z45FA8':
            [
                {
                    'SQCC': {'lpcrwgt': '160', 'lplcpon': '16'},
                    'SMCC': {'lpcrwgt': '100', 'lplcpon': '10'},
                    'SLCC': {'lpcrwgt': '180', 'lplcpon': '18'},
                }
            ],
        'Z12345':
            [
                {
                    'CPUL': {'lpcrwgt': '30', 'lplcpon': '10'},
                    'CPUF': {'lpcrwgt': '49', 'lplcpon': '7'},
                    'CPUA': {'lpcrwgt': '250', 'lplcpon': '25'},
                    'CPK2': {'lpcrwgt': '21', 'lplcpon': '3'},
                    'CPUJ': {'lpcrwgt': '40', 'lplcpon': '4'},

                }
            ],
        'ZABCDE':
            [
                {
                    'SJCC': {'lpcrwgt': '190', 'lplcpon': '19'},
                    'SCCC': {'lpcrwgt': '200', 'lplcpon': '20'},
                }
            ],

    }



    context = classes.junta1(cpc_profile_dic, cec_lpar_dic, cpc_list)

    return render_template('onoff.html', timestamp={'hora': datetime.now()}, context={'cpc_operations': context})


if __name__ == '__main__':
    app.run(debug=True)
