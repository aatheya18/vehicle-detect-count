# Vehicle Detection and Counting
This project is a web application designed for automated vehicle detection and classification from user-uploaded images. Leveraging computer vision techniques, it identifies and counts vehicles, distinguishing between cars and buses. The application provides an efficient and accurate solution to the time-consuming and error-prone manual process of vehicle analysis.

# Features
- Automated Detection and Classification: Processes uploaded images to identify and classify vehicles (cars and buses) using pre-trained classifiers.
- User-Friendly Interface: Built with Materialize CSS for a clean, responsive, and intuitive user experience, allowing for easy image uploads.
- Scalable Web Deployment: The application is deployed on Render Dashboard, ensuring it can handle multiple user requests and is globally accessible.
- Real-Time Processing: Images are processed immediately upon upload, with no data stored, providing instant results.
- Visual Feedback: Displays the processed image with bounding boxes around detected vehicles, making the results clear and easy to understand.

# Technical Overview
1) Architecture
The application follows a Model-View-Controller (MVC) architecture, with the backend handling all the core logic and the frontend providing the user interface.
- Frontend: Built with HTML, CSS, and JavaScript, using the Materialize CSS framework for a responsive and clean design.
- Backend: A Flask web framework handles HTTP requests, orchestrating the image processing workflow.
- Computer Vision: Utilizes OpenCV's image processing capabilities, specifically Haar cascades, for vehicle detection. PIL and NumPy are used for image manipulation and numerical operations.

2) Deployment
The system is hosted on Render Dashboard, which automates the deployment process directly from the project's GitHub repository. This ensures high availability and scalability.

3) Key Features Implemented
- Secure image upload validation to prevent malicious file injections.
- Efficient image processing through resizing to optimize performance.
- Clear display of results, with bounding boxes and counts for detected vehicles.

# Steps to run application:
- Step 1:	Create the copy of the project.
- Step 2: Open command prompt and change your current path to folder where you can find 'app.py' file.
- Step 3: Create environment by command given below-
    conda create -name <environment name>
- Step 4: Activate environment by command as follows-
    conda activate <environment name>
- Step 5: Use command below to install required dependencies-
    python -m pip install -r requirements.txt
- Step 6: Run application by command;
    python app.py
  You will get url copy it and paste in browser.
- Step 7: You have sample_data folder where you can get images to test.

# Future Enhancements
- Real-time Video Processing: Extend the system to support live video feeds for continuous detection and counting.
- Expanded Classification: Add more vehicle categories such as trucks, motorcycles, and bicycles.
- Database Integration: Implement a database to store and analyze historical detection data.
- Model Upgrade: Transition from traditional computer vision classifiers (Haar cascades) to more advanced deep learning models like YOLO or SSD for improved accuracy.

# Conclusion
This project successfully demonstrates an automated solution for vehicle detection and counting using Python, Flask, and OpenCV. It serves as a strong foundation for more complex computer vision applications, with a clear path for future enhancements, including real-time analysis and the adoption of deep learning technologies.
