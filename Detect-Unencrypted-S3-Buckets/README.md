

Created 2 s3 buckets one with encrypt and other with no-encrypted.

<img width="603" height="122" alt="image" src="https://github.com/user-attachments/assets/8368bcc9-4e53-4361-9774-a941398c777a" />

Created IAM role 

<img width="779" height="349" alt="image" src="https://github.com/user-attachments/assets/33aed8a1-1434-45f2-9ee3-4c06d3c71252" />

Created LAMBDA Fucntion with s3securityrole permission

<img width="775" height="230" alt="image" src="https://github.com/user-attachments/assets/3f8f152c-e06e-4cb1-b39b-98487ad8a1c0" />

Lamdba function code:-
<img width="695" height="265" alt="image" src="https://github.com/user-attachments/assets/16bd4434-5e5d-47d8-b405-48c9660ec244" />

Executing function: succeeded (logs )
Details

START RequestId: ca75673e-e2ee-4598-9c60-814571e35339 Version: $LATEST
Bucket: test-bucket-encryption-s3 → Encryption Type: AES256
Bucket: test-bucket-no-encryption-s3 → Encryption Type: AES256

