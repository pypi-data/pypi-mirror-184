# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:56:58 2022

@author: franc
"""


from flask import Flask, redirect, request, render_template, send_from_directory
from datetime import datetime
import pickle
import os
import webbrowser

cwd = os.getcwd()

app = Flask(__name__)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/menu')
def index():
    html_code = "<style>a:hover{cursor:pointer;}</style><ul>"
    for folder in [x[0] for x in os.walk(cwd)]:
        if folder != ".":
            try:
                r = open(folder+"\\index.html")
                ft = folder.split("\\")[-1].replace(".","")
                html_code = html_code + f"""
                    <li><a onclick="urlc('interface/{ft}')" >{ft}</a></li>
                """
            except:
                0
    
    html_code = html_code + """
    </ul>
    <script>
        function urlc(url){
            rdn_nb = Math.floor(Math.random() * 10000001);
            document.location.href = (url + "?uid=" + rdn_nb);
        }
    </script>
    """
    
    return html_code


@app.route('/f/<path:path_file>')
def send_asset(path_file):
    print("passed")
    print(path_file)
    return open( path_file, "r").read() 


@app.route('/input_data/<folder>', methods=["POST"])
def input_data(folder):
    data = {}
    for key in request.form.keys():
        data[key] = request.form.get(key)
    print(data)
    
    # Save file
    file = open(cwd+"\\"+folder+"\\input_data.pkl","wb")
    pickle.dump(data,file)
    file.close()
    
    ts = str(datetime.timestamp(datetime.now()))
    file = open(cwd+"\\"+folder+"\\lastuitime.txt","w")
    file.write(ts)
    file.close()
    
    return "0"
    

@app.route('/interface/<folder>')
def interface(folder):
    
    uid = request.url.split("?uid=")[-1]
    html = send_asset(cwd+"\\"+folder+"\\index.html")
    
    # Check if file exist
    if os.path.exists(cwd+"\\"+folder+"\\input_data.pkl"):
        file = open(cwd+"\\"+folder+"\\input_data.pkl","rb")
        data = pickle.load(file)
        if(int(data["uid"]) != int(uid)):
            # Check time
            ti_c = os.path.getmtime(cwd+"\\"+folder+"\\input_data.pkl")
            print(datetime.timestamp(datetime.now()))
            print(ti_c)
            if (ti_c+10) > datetime.timestamp(datetime.now()):
                html = "Instance already running. If just closed, wait at least 10 seconds."

    print(html)
    return html
    

if __name__ == "__main__":
    webbrowser.open_new("http://localhost:20000/menu")
    app.run(host="0.0.0.0",port=20000)

def main_m():
    webbrowser.open_new("http://localhost:20000/menu")
    app.run(host="0.0.0.0",port=20000)