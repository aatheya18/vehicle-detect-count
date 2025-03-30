# Important imports
from app import app
from flask import request, render_template, url_for, redirect, flash
import cv2
import numpy as np
from PIL import Image
import string
import random
import os

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

# Ensure upload directory exists
os.makedirs(app.config['INITIAL_FILE_UPLOADS'], exist_ok=True)

car_cascade_src = 'app/static/cascade/cars.xml'
bus_cascade_src = 'app/static/cascade/Bus_front.xml'

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():
    full_filename = 'images/white_bg.jpg'  # Default value

    if request.method == "POST":
        # Check if file was uploaded
        if 'image_upload' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
            
        image_upload = request.files['image_upload']
        
        # Check for empty filename
        if image_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)

        try:
            # Generate unique filename
            letters = string.ascii_lowercase
            name = ''.join(random.choice(letters) for i in range(10)) + '.png'
            full_filename = 'uploads/' + name
            save_path = os.path.join(app.config['INITIAL_FILE_UPLOADS'], name)

            # Process image
            image = Image.open(image_upload)
            image = image.resize((450, 250))
            image_arr = np.array(image)
            grey = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)

            # Cascade detection
            car_cascade = cv2.CascadeClassifier(car_cascade_src)
            cars = car_cascade.detectMultiScale(grey, 1.1, 1)

            bcnt = 0
            bus_cascade = cv2.CascadeClassifier(bus_cascade_src)
            bus = bus_cascade.detectMultiScale(grey, 1.1, 1)
            for (x, y, w, h) in bus:
                cv2.rectangle(image_arr, (x, y), (x+w, y+h), (0, 255, 0), 2)
                bcnt += 1

            ccnt = 0
            if bcnt == 0:
                for (x, y, w, h) in cars:
                    cv2.rectangle(image_arr, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    ccnt += 1

            # Save processed image
            img = Image.fromarray(image_arr, 'RGB')
            img.save(save_path)

            result = f'{ccnt} cars and {bcnt} buses found'
            return render_template('index.html', full_filename=full_filename, pred=result)

        except Exception as e:
            flash(f'Error processing image: {str(e)}')
            return redirect(request.url)

    # GET request handling
    return render_template("index.html", full_filename=full_filename)

# Main function
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'  # Needed for flashing messages
    app.run(debug=True)
