# Serverless-Architecture
Added all 4 tasks under this repo in different sub folders
Assignment 1: Auto Stop EC2 Instances using Lambda

Objective: Automatically stop idle EC2 instances to save cost.

Overview:

Used AWS Lambda with CloudWatch EventBridge.
Lambda checks running EC2 instances and stops them based on criteria (e.g., idle time or specific tags).
Automated scheduling ensures cost optimization without manual monitoring.

Outcome:

EC2 instances tagged as “Idle” are automatically stopped.
Reduced manual management and AWS cost.
Assignment 2: Auto Start EC2 Instances using Lambda

Objective: Automatically start EC2 instances at scheduled times.

Overview:

Lambda function triggers at scheduled times via CloudWatch EventBridge rules.
Targeted EC2 instances are started automatically.
Useful for instances required only during working hours.

Outcome:

EC2 instances start automatically at the desired schedule.
Ensures resources are available when needed without manual intervention.
Assignment 3: Automated EC2 Cleanup (Terminate) using Lambda

Objective: Automatically terminate EC2 instances after a specific duration or based on tags.

Overview:

Lambda scans all running instances.
Filters instances based on tags or creation time.
Calls terminate_instances via Boto3 to clean up unused resources.

Outcome:

Unnecessary EC2 instances are terminated automatically.
Helps maintain a clean environment and reduces AWS cost.
Assignment 4 (Assignment 5 from your notes): Auto-Tag EC2 Instances on Launch

Objective: Automatically tag newly launched EC2 instances with metadata like current date and owner.

Overview:

Uses AWS Lambda triggered by EventBridge EC2 state-change event.
Lambda code in Python (Boto3):
Reads instance ID from EventBridge event.
Tags instance with:
Owner → Custom value (e.g., Vara)
LaunchedOn → Current date (YYYY-MM-DD)
Handles manual test events safely.

Outcome:

Every new EC2 instance is automatically tagged without manual effort.
Improves tracking, management, and accountability for AWS resources.
