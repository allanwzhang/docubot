# Use an AWS Lambda-compatible base image for Python 3.9
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory to Lambda's default
WORKDIR /var/task

# Copy requirements and source files to Lambda's default directory
COPY requirements.txt ./
COPY app.py controller.py llm.py ./
COPY templates ./templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the Lambda function handler
CMD ["app.lambda_handler"]
