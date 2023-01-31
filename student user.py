total_users = 856
staff_users = 126

non_teaching_staff = staff_users // 3
student_users = total_users - staff_users - non_teaching_staff

print("Number of student users:", student_users)
print("Number of non-teaching staff:", non_teaching_staff)
