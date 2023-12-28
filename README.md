# Online Calculator

This is a simple HTML and Python code for an online calculator that performs arithmetic operations based on user input.
Scroll to bottom for Docker information. 

## How it Works

The HTML code provides a basic user interface for the calculator. It includes input fields for the two numbers to be operated on and a dropdown list for selecting the operation to be performed. When the user clicks the "Calculate" button, the form is submitted to the Python code running on the server.

The Python code, implemented using Flask, handles the user input and performs the selected operation. It then returns the result to the HTML code, which displays it on the page. Make sure python is installed on your machine. Run `pip install flask`. Run `python ebs-calc.py`. Open your browser and navigate to http://127.0.0.1:5000. Do some calculations :]

## How to Use it

1. **Run the Python code on a server by executing it in a terminal or command prompt.**
2. **Once the server is running, open a web browser and navigate to the server's URL to access the calculator. (see above)**

## Logic Behind it

The Python code uses Flask to create a web application with a single route ("/") that handles both GET and POST requests. When a GET request is received, the code returns the HTML file, which is rendered using Jinja2 templates. When a POST request is received, the code retrieves the user input from the form and performs the selected operation. The result is then returned to the HTML file, which displays it on the page using Jinja2 templating.

The code performs basic error checking to ensure that the user input is valid and that division by zero does not occur.

## Deployment on Elastic Beanstalk

To deploy this web application on Elastic Beanstalk, follow these steps:

1. **Create a virtual environment with Flask installed. Make sure that your application is called "application.py". You can then pull up AWS and launch EBS.**
2. **Once there, create a new environment. Select Web server environment, add the name of your application, select the Python platform with the latest version. Then, click next. Skip the rest of the steps and click on skip to review. Wait a little bit and then your environment will be up and running.**
3. **Once everything is running, go to CodePipeline. Connect using GitHub. Make sure your Github account is connected to AWS. Follow the prompts on CodePipline. Skip build and go to deploy. Deploy provider-> AWS EBS, select your region, choose your application name/environment name. Create the pipeline. When done, click on your application and then click on the domain. There is your webapp! This is a live address that can be used and you can add a custom domain using Route53. Any changes made will also reflect on your webapp (CI/CD).**

## Technologies Used Overview

![HTML](./images/HTML.png)
![CSS](./images/CSS.png)
![Python](./images/Python.png)
![Flask](./images/Flask.png)
![EBS](./images/ebs.png)
![GitHub](./images/GitHub.png)
![CodePipeline](./images/CodePipeline.png)

## Deployment using Docker to AWS ECS

**AWS account needs the following permissions for this project:**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ecr:*",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor01",
            "Effect": "Allow",
            "Action": "ecr:GetAuthorizationToken",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor02",
            "Effect": "Allow",
            "Action": "ecr:InitiateLayerUpload",
            "Resource": "*"
        }
    ]
}

1. Create the Dockerfile for your web app.
2. Build the Docker image using the following commands. Follow the steps for Amazon ECR and push the image.
docker build -t your-image-name .
docker tag your-image-name:latest your-ecr-repository-uri/your-image-name:latest
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-ecr-repository-uri
docker push your-ecr-repository-uri/your-image-name:latest
# Replace your-image-name, your-ecr-repository-uri, and your-region with your actual image name, ECR repository URI, and AWS region.
3. Create a task definition for your Docker image. Specify the required resources.
4. Create an ECS cluster if you don't have one already.
5. Define the task in ECS, referencing the task definition and specifying the desired resources.
6. Run the task. Once it's running, click on the task name to open the public address using port 5000.

