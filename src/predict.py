import pickle
with open("models/placement_model.pkl","rb") as file:
    model = pickle.load(file)

print("Model loaded sucessfully")


cgpa = float (input("Enter CGPA: "))
programming = int (input("Enter Programming score: "))
aptitude = int (input("Enter Aptitude score: "))
communication = int (input("Enter Communication score: "))
projects = int (input("Enter no. of Projects: "))
internship = int (input("Internship(1=Yes, 0=No): "))



student =[[
    cgpa,
    programming,
    aptitude,
    communication,
    projects,
    internship
]]
prediction = model.predict(student)

if prediction[0] ==1:
    print("\n Prediction: Student is likely to be PLACED")
else:
    print("/n Prediction: Student is likely to NOT be PLACED")
      