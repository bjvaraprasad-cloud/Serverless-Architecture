AWS Lambda Project: S3 Old File Cleanup
🧠 Objective

This project automates the deletion of files older than 30 days in an S3 bucket using AWS Lambda and Boto3. It helps in optimizing storage and reducing unnecessary costs.

🏗️ Architecture
<img width="215" height="274" alt="image" src="https://github.com/user-attachments/assets/7d4a08d7-34cd-4d91-893a-8af2d041a61b" />

🛠️ AWS Services Used
Amazon S3
AWS Lambda
AWS IAM (Identity and Access Management)
Amazon CloudWatch (for logs)

⚙️ Setup Steps
1. Create S3 Bucket
<img width="934" height="354" alt="image" src="https://github.com/user-attachments/assets/ec3fc2b6-fd6a-43a8-9c2c-726d27673083" />


Upload test files
<img width="940" height="346" alt="image" src="https://github.com/user-attachments/assets/ed0c7e3f-ca6c-4092-88ca-809377fb6f68" />

/>
2. Create IAM Role
Go to IAM → Roles → Create Role
Select Lambda as trusted entity
Attach policy:
AmazonS3FullAccess

<img width="940" height="412" alt="image" src="https://github.com/user-attachments/assets/562bccb0-377f-430f-92e7-2365a85f2521" />

<img width="940" height="367" alt="image" src="https://github.com/user-attachments/assets/7db8b773-c3f3-4f05-aaa6-04cc06d34abe" />


<img width="940" height="298" alt="image" src="https://github.com/user-attachments/assets/cbd9084d-a9cb-4a3b-a8b2-4e0fd506fee6" 
3. Create Lambda Function
Go to Lambda → Create Function
Runtime: Python 3.x
Assign the IAM role
4. Add Lambda Code
i
🧪 Testing
Upload files to the S3 bucket

<img width="940" height="399" alt="image" src="https://github.com/user-attachments/assets/71b47161-eeb6-4a6f-8d8c-7e5396c226a3" />


Modify code temporarily to:

timedelta(minutes=1)
Wait 2–3 minutes
Run Lambda test
✅ Sample Output (CloudWatch Logs)
Deleted: test.txt
Kept: newfile.jpg
<img width="867" height="229" alt="image" src="https://github.com/user-attachments/assets/3c75bc5d-0b93-4063-9e49-2c3c1d03d14a" />

<img width="940" height="241" alt="image" src="https://github.com/user-attachments/assets/70b7afd4-1999-4d39-8868-64c8e9d5f8c2" />
⚠️ Notes
Ensure correct bucket name is used
Lambda must have proper IAM permissions
Region consistency is recommended
📌 Conclusion

This project demonstrates how AWS Lambda can be used to automate storage management tasks efficiently using Boto3.






