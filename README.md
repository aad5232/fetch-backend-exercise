# fetch-backend-exercise
 Take home exercise for Backend Engineer role at Fetch

 The code is in Python. I have included a dockerized setup to run the code.

 Dockerfile contains the Python base image and dependencies.

 Dependencies are added in a text file called requirements.txt, so that once dependencies start adding up its easier to install them using this file.

 To run the docker image using Virtual Studio code,
 1. Install Docker Desktop
 2. Install VS Code
 3. Add Docker extension in VS Code.
 4. Open a terminal in the current directory and check docker version by using command,
    docker -v

 Once everything is setup, run the flask application using the following commands;

 Build:

  docker build -t <image-name> .

 Run:

  docker run -p 5000:5000 <image-name>


This will run the application, then you can verify the responses.

While verifying, use the path-prefix as http://localhost:5000 for the API endpoints.

 
