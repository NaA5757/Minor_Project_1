# from flask import Flask, render_template, request
# import Tokenization
# import getUserTweets
# import Test
# app = Flask(__name__)
# #model,bow_Vectorization = Test.model_vect()
# # streamming_tweet = getUserTweets.public_tweets()
#
# @app.route('/', methods=["GET","POST"])
# def main():
#     if request.method=="POST":
#         inp=[request.form.get("inp")]
#         print((type(inp)))
#         print(inp)
#         check=Tokenization.clean_tweet(inp)
#         print(check)
#         check=bow_Vectorization.transform(check).toarray()
#         print(check)
#         y_pred = model.predict(check)
#         if y_pred ==1:
#             return render_template('home.html',message="😔💔🥺")
#         else:
#             return render_template('home.html',message="😃😍😝")
#     return render_template('home.html')
#
#
#
# @app.route('/home2', methods=["GET","POST"])
# def main_tweet():
#     if request.method=="POST":
#         inp1 = request.form.get("inp1")
#         streamming_tweet = getUserTweets.userTweets(inp1)
#         print(streamming_tweet)
#         inp2 = request.form.get("inp2")
#         print(type(inp2))
#         inp2=int(inp2)
#         print(type(inp2))
#         data = streamming_tweet[0]
#         # check = [data]
#         # check=Tokenization.clean_tweet(check)
#         # print(check)
#         # check=bow_Vectorization.transform(check).toarray()
#         # print(check)
#         # y_pred = model.predict(check)
#         y_pred=0
#         if y_pred ==1:
#             return render_template('home2.html',message="😔💔🥺",value=data,index=inp1)
#         else:
#             return render_template('home2.html',message="😃😍😝",value=data,index=inp1)
#     return render_template('home2.html')
#
# #set FLASK_APP=main.py
# #set FLASK_ENV=development
# #flask run

from flask import Flask, render_template, request
import Tokenization
import getUserTweets
import Performance
import Vectorization
import Test
app = Flask(__name__)
model,bow_Vectorization = Test.model_vect()
# streamming_tweet = getUserTweets.public_tweets()
# streamming_tweet.append("sad")
# import json
#
# data = {"Eleven": "Millie",
#         "Mike": "Finn",
#         "Will": "Noah"}
#
# with open('app.json', 'w') as f:
#     json.dump(data, f)
# i=-1

@app.route('/', methods=["GET","POST"])
def main():
    if request.method=="POST":
        # inp=[request.form.get("inp")]
        # print((type(inp)))
        # print(inp)
        # check=Tokenization.clean_tweet(inp)
        # print(check)
        # check=bow_Vectorization.transform(check).toarray()
        # print(check)
        # y_pred = model.predict(check)
        y_pred=1
        if y_pred ==1:
            return render_template('home.html',message="😔💔🥺")
        else:
            return render_template('home.html',message="😃😍😝")
    return render_template('home.html')



@app.route('/home2', methods=["GET","POST"])
def main_tweet():
    if request.method=="POST":
       # inp=request.form.get("inp")
        inp1 = request.form.get("inp1")

        streamming_tweet = getUserTweets.userTweets(inp1)
        print(streamming_tweet)
        # inp2 = request.form.get("inp2")
        # inp2=int(inp2)
        list1=[]
        for tweet in streamming_tweet :
            data = tweet
            # print(data)
            check = [data]
            check=Tokenization.clean_tweet(check)
            # print(check)
            check=bow_Vectorization.transform(check).toarray()
            # print(check)
            y_pred = model.predict(check)
            list1.append(y_pred)
        d=0
        nd=0
        for i in list1:
            if(i==1):
                d=d+1
            else:
                nd=nd+1
        print(d,nd)
        if d>nd:
            return render_template('home2.html',message="😔💔🥺")
        else:
            return render_template('home2.html',message="😃😍😝")
    return render_template('home2.html')
# if __name__ =='__main__':
#     app.run()
#set FLASK_APP=main.py
#set FLASK_ENV=development
#flask run



#heroku step

#git init
#heroku login
#heroku git:remote -a predictdepression
#pip install gunicorn
#pip freeze > requirements.txt
#git add .
#git commit -m "first commit"
#git push heroku master