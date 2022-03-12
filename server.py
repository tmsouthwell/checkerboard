from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/<int:row>/<int:col>')          
def checkerboard(row,col):
    return render_template("index.html", row=row, col=col)




if __name__=="__main__":  
    app.run(debug=True)  