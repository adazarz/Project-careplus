# Project-careplus
Training data engineering project with AWS

<img width="650" height="382" alt="image" src="https://github.com/user-attachments/assets/626ad1da-8141-40f5-ade2-6e33e312c2f6" />

This is a repository with a  project created on training data from codebasics as part of a data engineering bootcamp. The purpose of the project is to perform an ELT (extract-load-transform) process with AWS. I performed following steps:
1. Load data from support-log files and extract necessary information with python regex, placing them in Amazon S3.
<img width="1546" height="447" alt="image" src="https://github.com/user-attachments/assets/37c2e8bf-6345-4554-b1b0-a1865f4e7e40" />
2. Load data from support-tickets in MariaDB database into Amazon S3 bucket in .csv format
3. I performed transformations on logs (with lambda, automated based on events) and lodaed them into processed folder in S3 in .parquet file <br/>
4. I performed transformations on tickets with AWS glue (automated with lambda based on events), also loaded in .parquet format into S3
5. I performed ad hoc analysis on ticket data in AWS Athena

<img width="1551" height="635" alt="image" src="https://github.com/user-attachments/assets/b8732413-73ee-4d0c-8223-09f1605b80f6" />
