import requests
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from ImageScrapperUtils.ImageScrapperUtils import ImageScrapperUtils
from ImageScrapper.ImageScrapper import ImageScrapper



app = Flask(__name__) # initialising the flask app with the name 'app'


@app.route('/')  # route for redirecting to the home page

@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages') # route to show the images on a webpage
@cross_origin()
def show_images():
    utils = ImageScrapperUtils() #Instantiating the object of class ImageScrapper
    list_of_jpg_files=utils.list_only_jpg_files('images') # obtaining the list of image files from the static folder
    print(list_of_jpg_files)
    try:
        if(len(list_of_jpg_files)>0): # if there are images present, show them on a wen UI
            return render_template('showImage.html',user_images = list_of_jpg_files)
        else:
            return "Please try with a different string" # show this error message if no images are present in the static folder
    except Exception as e:
        print('no Images found ', e)
        return "Please try with a different string"


@app.route('/searchImages', methods=['GET','POST'])
def searchImages():
    if request.method == 'POST':
        print("entered post")
        keyWord = request.form['keyword'] # assigning the value of the input keyword to the variable keyword

    else:
        print("did not enter post")
    print('printing = ' + keyWord)

    # keyWord= "Dogs"
    DRIVER_PATH = './chromedriver'
    utils = ImageScrapperUtils
    utils.search_and_download(search_term=keyWord, driver_path=DRIVER_PATH)

    return show_images()  # redirect the control to the show images method




if __name__ == '__main__':
    app.run(debug=True)


