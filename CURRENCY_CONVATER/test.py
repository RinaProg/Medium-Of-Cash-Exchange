
from flask import Flask,request,render_template
import requests

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def test_home():
    try:
        if  request.method=='POST':
            new_cur=request.form.get('want')
            old_cur=request.form.get('have')
            old_amt=request.form.get('amount')

            api_url = (f'https://api.api-ninjas.com/v1/convertcurrency?want={new_cur}&have={old_cur}&amount={old_amt}')
            response = requests.get(api_url, headers={'X-Api-Key': 'XqiOYs7GvZPiVS94OmamJg==8mIK9ItYZoyV6HaX'})
            data=response.json()
            new_amt=(data['new_amount'])
            new_val=(f"{new_amt:.2f}")
            return render_template('home.html',new_val=new_val)
        return render_template('home.html')   
              
    except:
        return "<h1>Please fill the form properly! 😟</h1>"
   

if __name__=='__main__':
    app.run(debug=True)