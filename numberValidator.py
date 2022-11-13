import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import number_type
import csv
import codecs
from pathlib import Path
import uuid;
import os 

# making directories
try: 
    os.mkdir("./OutputFiles") 
except OSError as error: 
    print("Directory already exist!") 

try: 
    os.mkdir("./OutputFiles/Mobile") 
except OSError as error: 
    print("Directory already exist!") 

try: 
    os.mkdir("./OutputFiles/Landline") 
except OSError as error: 
    print("Directory already exist!") 


try: 
    os.mkdir("./OutputFiles/Invalid") 
except OSError as error: 
    print("Directory already exist!") 


# looping through files   
for xfile in Path("./Files").glob('*.csv'):
  print(xfile)
  # create files in folders
  mobileFile=open("./OutputFiles/Mobile/"+str(uuid.uuid4())+"-ValidMobile.csv","w",newline='')
  landlineFile =open("./OutputFiles/Landline/"+str(uuid.uuid4())+"-ValidLandline.csv","w",newline='')
  invalidFile =open("./OutputFiles/Invalid/"+str(uuid.uuid4())+"-Invalid.csv","w",newline='')

  # defining csv writer
  mobileFileWriter = csv.writer(mobileFile)
  landlineleFileWriter = csv.writer(landlineFile)
  invalidFileWriter = csv.writer(invalidFile)
    
  #  defining row array 
  landlineRow=[]
  mobileRow=[]
  invalidRow=[]
  csvReader = csv.reader(codecs.open(xfile, 'rU', 'utf-16'))

  try:
    with open(xfile, 'r') as xfile:
      csvreader = csv.reader( (line.replace('\0','') for line in xfile) )
      for row in csvreader:
        print("validating: ", row)
        
        # if the cell is not empty
        if(len(row)>0):
          for val in row:
              
              formattedValue = val if "+1" in val else "+1" + val
              
              if(not any(formattedValue.isalpha() for formattedValue in formattedValue)):
                  parsed = phonenumbers.parse(formattedValue)
                  if(phonenumbers.is_valid_number(parsed)):
                    isMobile = carrier._is_mobile(number_type(parsed))
                    if(isMobile):
                      if(len(mobileRow) == 25):
                        mobileRow.append(phonenumbers.format_number(phonenumbers.parse(val, 'US'), phonenumbers.PhoneNumberFormat.INTERNATIONAL))  
                        # print(mobileRow,'mobile row')
                        mobileFileWriter.writerow(mobileRow) 
                        mobileRow = []
                      else:
                        mobileRow.append(phonenumbers.format_number(phonenumbers.parse(val, 'US'), phonenumbers.PhoneNumberFormat.INTERNATIONAL))  
                    else:
                      if(len(landlineRow) == 25):
                        landlineRow.append(phonenumbers.format_number(phonenumbers.parse(val, 'US'), phonenumbers.PhoneNumberFormat.INTERNATIONAL))
                        # print(mobileRow,'landline row')
                        landlineleFileWriter.writerow(landlineRow)
                        landlineRow = []
                      else:
                        landlineRow.append(phonenumbers.format_number(phonenumbers.parse(val, 'US'), phonenumbers.PhoneNumberFormat.INTERNATIONAL))
                  else:
                      if(len(invalidRow) == 25):
                        invalidRow.append(phonenumbers.format_number(phonenumbers.parse(val, 'US'), phonenumbers.PhoneNumberFormat.INTERNATIONAL))
                        invalidFileWriter.writerow(invalidRow)
                        invalidRow = []
                      else:
                        # print(landlineRow)
                        invalidRow.append(phonenumbers.format_number(phonenumbers.parse(val, 'US'), phonenumbers.PhoneNumberFormat.INTERNATIONAL))
  except NameError as error:
      print("Due to any corrupt file script stopped!",error)
  
  # write the remaining data in file
  mobileFileWriter.writerow(mobileRow) if len(mobileRow) >0 else ""
  landlineleFileWriter.writerow(landlineRow) if len(landlineRow)>0 else ""
  invalidFileWriter.writerow(invalidRow) if len(invalidRow) >0 else ""
  # close files
  mobileFile.close()
  landlineFile.close()
  invalidFile.close()

  # reset values
  mobileFile=""
  landlineFile=""
  invalidFile=""
  mobileRow=[]
  landlineRow=[]
  invalidRow=[]

print("------- Thankyou for your patience, extraced successfully! ---------")
