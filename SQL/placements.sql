SELECT 
    name
FROM students
    LEFT JOIN friends ON students.id = friends.id
    LEFT JOIN packages student_packages ON students.id = student_packages.id
    LEFT JOIN packages friend_packages ON friends.friend_id = friend_packages.id
WHERE student_packages.salary < friend_packages.salary
ORDER by friend_packages.salary;
