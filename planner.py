def check_marks(marks):
    if marks>=90:
        print("excellent!")
        return 1,"excellent" 
    elif marks>=75:
        print("good job:")
        return 1,"good job"
    else:
        print("keep going:")
        return 1,"keep going"
grades=[]#list of dictionaries
good_job_count = 0
total_marks= 0
times=int(input("how many subject?;"))
for i in range(times):
    subject=input("enter your subject:")
    marks=int(input("enter your marks:"))
    #check marks and get comment
    result , comment = check_marks(marks)
    good_job_count+=result
    total_marks+=marks
grades.append({
    "subjects": subject,
    "marks": marks,
    "comment": comment
})
#loop to all entry subject,marks,comment
print("\n---report---")
for entry in grades:
    print(entry["subjects"],"-",entry["marks"],"-",entry["comment"])
#calculate overall percentage
overall_percentage=total_marks / times
print("n/Total marks:",total_marks)
print("Overall percentage:",overall_percentage)
if overall_percentage>=90:
    print("Excellent!")
elif overall_percentage>=70:
    print("Good Job!")
else:
    print("Keep going!")
print("No. of subjects with Good Job/Excellent:",good_job_count)
