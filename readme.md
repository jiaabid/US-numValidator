# US Number Validator
Its a phonenumber parsing script, it parse phonenumbers in the provided csv and validate is it a US number or not, then check if its a mobile number or landline number.


## Pre-requisites
- Python
- Files directory in root folder


## Flow
- It extract all the csv extension files from the Files folder.
- Iterate over each file and extract data.
- Use google's "phonenumber" lib to validate and format numbers.
- Write it down to new file in OutputFiles folder (output files are divided by the type of number)

## Run
You can run the script with following command: **py -3 numberValidator.py**  

