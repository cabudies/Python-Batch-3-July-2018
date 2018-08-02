import matplotlib.pyplot as pyt

month = ['May', 'June', 'July', 'August']
# students = [60, 70, 40, 35]

graphicEraStudents = [30, 40, 20, 10]
ditStudents = [10, 50, 37, 28]
itgStudents = [3, 8, 20, 4]

# pyt.plot(month, students)

# pyt.plot(month, graphicEraStudents)
# pyt.plot(month, ditStudents)
# pyt.plot(month, itgStudents)
pyt.scatter(month, graphicEraStudents)
pyt.scatter(month, ditStudents)
pyt.scatter(month, itgStudents)


pyt.xlabel('Month')
pyt.ylabel('Students')
pyt.title('Numbers of students enrolled, month-wise')
# # pyt.yticks([0])
#
pyt.legend(['Graphic Era University',
            'DIT University',
            'IT Gopeshwar'], loc ='upper left')
#
# pyt.scatter(month, students)
pyt.show()
