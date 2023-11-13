import logging
import os
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# No need to specify AWS credentials here

# Initialize the S3 client without explicit credentials
s3 = boto3.client('s3')

# Function to upload a file to S3
def upload_to_s3(local_file, bucket, s3_file):
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )

if __name__ == '__main__':
    logging.info("here again I am testing")

    # Specify the S3 bucket name through an environment variable
    # S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    S3_BUCKET_NAME = 'dimondpriceprediction_logs'

    if S3_BUCKET_NAME:
        # Upload log file to S3 bucket
        upload_to_s3(LOG_FILEPATH, S3_BUCKET_NAME, LOG_FILE)
    else:
        logging.warning("S3_BUCKET_NAME environment variable not set. Unable to upload to S3.")




# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# log_path=os.path.join(os.getcwd(),"logs")

# os.makedirs(log_path,exist_ok=True)

# LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


# logging.basicConfig(level=logging.INFO, 
#                     filename=LOG_FILEPATH,
#                     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
# )


# if __name__ == '__main__':
#     logging.info("here again i am tesitng")