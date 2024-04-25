# from flask import Flask, render_template, request, redirect,url_for,session,jsonify
# from flask_restful import Resource, Api, reqparse
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# import PIL.Image
# load_dotenv(".env")
# gkey = os.getenv("GOOGLE_KEY")
# admincode = os.getenv("ADMIN_CODE")
# genai.configure(api_key=gkey)



# model1 = genai.GenerativeModel("gemini-pro")

# app = Flask(__name__,template_folder="templateFiles",static_folder="staticFiles")
# api = Api(app)
# @app.route("/")
# def index():
#     return render_template("index.html")


# # @app.route("/sendchat",methods=['POST','GET'])
# # def sendchat():
# #     receivedcode = request.form["admincode"]
# #     receivedmsg = request.form["chatsent"]
# #     if(receivedcode==admincode):
# #         responsex = model1.generate_content(receivedmsg)
# #         return responsex.text
    
    
# class Receivechat(Resource):
#     def post(self):
#         code = request.form["admincode"]
#         if(code==admincode):
#             msg = request.form["chatsent"]
# #     filename = request.form["filename"]
# #     filedata = request.form["filedata"]
#             responsex = model1.generate_content(str(msg))
#             return responsex.text
# api.add_resource(Receivechat,"/receivechat")


# class Receiveimage(Resource):
#     def post(self):
#         code = request.form["admincode"]
#         if(code==admincode):
#             msg = request.form["chatsent"]
#             # filename = request.form["filename"]
#             filedata = request.files['file']
#             filenamex = request.form["filename"]
#             filedata.save(os.path.join('staticFiles', filenamex))
#             return jsonify({'message': "successful"})
           
#             # hedgefile = open(str("{}.jpg".format(filename)),"w")
#             # hedgefile = open(str(filename),"w")
#             # hedgefile.write(filedata)
#             # hedgefile.close()
#          #   dir = os.getcwd()
#           #  foldername = "/staticFiles"
#           #  path = os.path.join(dir+foldername,filename)
#         #    os.mkdir(path)
#        #     filedata.save(os.path.join('staticFiles', filename))
#             # return msg
#             # img = PIL.Image.open(os.path.join('staticFiles', filename))
#             # model2 = genai.GenerativeModel("gemini-pro-vision")
#             # responsey = model2.generate_content([msg,img])
#             # # responsey = model1.generate_content(str(msg))
#             # return responsey.text

# api.add_resource(Receiveimage,"/receiveimage")

# # @app.route("/sendimage",methods=['POST','GET'])
# # def replyimage():
# #     receivedcode = request.form["admincode"]
# #     filedata = request.form["filedata"]
    
# #     if(admincode==admincode):
# #         pass
    
    
    
    
    
    
    


# # @app.route("/updateimgfile",methods=['POST','GET'])
# # def createfilerx():
# #     admincode = request.form["admincode"]
# #     filename = request.form["filename"]
# #     filedata = request.form["filedata"]
    
# #     if(admincode==admincode):

# #         hedgefile = open(str("{}.jpg".format(filename)),"w")
# #         hedgefile.write(filedata)
# #         hedgefile.close()
# #         return "Done"
    
# # @app.route("/signup")
# # def signup():
# #     return render_template("signup.html")

# # @app.route("/signin")
# # def signin():
# #     return render_template("signin.html")

# # @app.route("/panel")
# # def panel():
# #     return render_template("panel.html",userdata="HEXEBA HOME",userpass=admincode)


from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
import google.generativeai as genai
from dotenv import load_dotenv
import os
import PIL.Image
import pickle
from requests_oauthlib import OAuth1Session
import json
import telebot
from telebot import types


load_dotenv(".env")
gkey = os.getenv("GOOGLE_KEY")
admincode = os.getenv("ADMIN_CODE")
telegrambotapi = os.getenv("TELEGRAM_API")
bot = telebot.TeleBot(telegrambotapi)
genai.configure(api_key=gkey)

model1 = genai.GenerativeModel("gemini-pro")

app = Flask(__name__, template_folder="templateFiles", static_folder="staticFiles")
api = Api(app)


@app.route("/")
def index():
    return render_template("index.html")

class Receivechat(Resource):
    def post(self):
        code = request.form["admincode"]
        if code == admincode:
            msg = request.form["chatsent"]
            responsex = model1.generate_content(str(msg))
            return responsex.text
api.add_resource(Receivechat, "/receivechat")

class Sendtweet(Resource):
    def post(self):
        try:
            code = request.form["admincode"]
            if code == admincode:
                message = request.form["tweetmesage"]
            # if(state=="real"):
                load_dotenv()

                # Load the oauth variable from the saved file using pickle
                with open("oauth.pkl", "rb") as file:
                    oauth = pickle.load(file)
            
                tweet_text = message
                print(tweet_text)


                # Payload for the tweet
                payload = {"text": tweet_text}

                # Making the request
                response = oauth.post(
                    "https://api.twitter.com/2/tweets",
                    json=payload,
                )

                if response.status_code != 201:
                    raise Exception(
                        "Request returned an error: {} {}".format(response.status_code, response.text)
                    )

                print("Response code: {}".format(response.status_code))

                # Saving the response as JSON
                json_response = response.json()
                print(json.dumps(json_response, indent=4, sort_keys=True))
    
           # return "Successful"
            
                msg = "Successful"
                return jsonify({'message': "{}".format(msg)})
            else:
                return jsonify({'error': 'Invalid admin code'})
        except Exception as e:
            return jsonify({'error': str(e)})      
            # responsex = model1.generate_content(str(msg))
            # return responsex.text
api.add_resource(Sendtweet, "/sendtweet")


class Telegrammessage(Resource):
    def post(self):
        try:
            code = request.form["admincode"]
            if code == admincode:
                message = request.form["telegrammessage"]
                chatid = request.form["chatid"]
                bot.send_message(chatid,message)
                msg = "Successful"
                return jsonify({'message': "{}".format(msg)})
            else:
                return jsonify({'error': 'Invalid admin code'})
        except Exception as e:
            return jsonify({'error': str(e)})         

api.add_resource(Telegrammessage, "/telegrammessage")

class Receiveimage(Resource):
    def post(self):
        try:
            code = request.form["admincode"]
            if code == admincode:
                msg = request.form["chatsent"]
                filedata = request.files['file']
                filenamex = request.form["filename"]
                filedata.save(os.path.join('upload', filenamex))
                
                # img = PIL.Image.open(os.path.join('upload', filenamex))
                img = PIL.Image.open(('upload/{}'.format(filenamex)))
                model2 = genai.GenerativeModel("gemini-pro-vision")
                responsey = model2.generate_content([msg,img])
                # responsey = model1.generate_content(str(msg))
               # return responsey.text
                
                return jsonify({'message': "{}".format(responsey.text)})
            else:
                return jsonify({'error': 'Invalid admin code'})
        except Exception as e:
            return jsonify({'error': str(e)})
api.add_resource(Receiveimage, "/receiveimage")

# if __name__ == "__main__":
#     app.run(debug=True)
