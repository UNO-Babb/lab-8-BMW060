#ProcessData.py
#Name: Brennan Wood
#Date: 4/5/25 
#Assignment: Lab 8 Process Data

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file

  def userID(firstName,lastName,idnum):
    if len(lastName) < 5:
      id = firstName[0] + lastName + "x"*(5-len(lastName)) + idnum[len(idnum)-3:]
    else:
      id = firstName[0] + lastName + idnum[len(idnum)-3:]
    return id
  
  def schyear(yr):
    if yr == "Freshman":
      year = "FR"
    elif yr == "Sophomore":
      year = "SO"
    elif yr == "Junior":
      year = "JR"
    else:
      year = "SR"
    return year

  for line in inFile:
    data = line.split()
    firstName = data[0]
    lastName = data[1]
    idnum = data[3]
    yr = data[5]
    maj = data[6]
    student_id = userID(firstName,lastName,idnum)
    year = schyear(yr)
    
    output = lastName + "," + firstName + "," + student_id + "," + maj[:3] + "-" + year + "\n"
    outFile.write(output)





  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
