# PassGen: Python Flask with Docker Integration
 GENERATOR OF SECURE EASY-TO-REMEBER PASSWORDS 

Passgen Flask App
Build the Docker image:
Open a terminal and navigate to the directory containing your Dockerfile. Then use the following command to build the Docker image. You can name your image using the -t flag.

docker build -t passgen .

Where passgen is the name you want to assign to your image. The dot at the end indicates the current directory as the build context.

Run the container:
After the image has been built, you can run a container based on it. Use the following command:

docker run -p 5000:5000 passgen

Where passgen is the name of the image you want to run. This command maps port 5000 from the host to port 5000 in the container (as declared with EXPOSE 5000 in the Dockerfile).

Check the operation:
Once the container is running, the Flask application should be accessible at http://localhost:5000 in your web browser.

