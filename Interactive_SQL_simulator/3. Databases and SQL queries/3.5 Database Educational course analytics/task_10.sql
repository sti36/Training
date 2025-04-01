/*Задание
Проанализировать, в каком порядке и с каким интервалом пользователь отправлял последнее верно выполненное задание каждого урока. В базе занесены попытки студентов  для трех уроков курса, поэтому анализ проводить только для этих уроков.

Для студентов прошедших как минимум по одному шагу в каждом уроке, найти последний пройденный шаг каждого урока - крайний шаг, и указать:

имя студента;
номер урока, состоящий из номера модуля и через точку позиции каждого урока в модуле;
время отправки  - время подачи решения на проверку;
разницу во времени отправки между текущим и предыдущим крайним шагом в днях, при этом для первого шага поставить прочерк ("-"), а количество дней округлить до целого в большую сторону.
Столбцы назвать  Студент, Урок,  Макс_время_отправки и Интервал  соответственно. Отсортировать результаты по имени студента в алфавитном порядке, а потом по возрастанию времени отправки.*/

WITH students_3lessons
AS
(
    SELECT student_id
    FROM step_student JOIN step USING(step_id)
    WHERE result = "correct"
    GROUP BY student_id
    HAVING COUNT(DISTINCT lesson_id) = 3
),
max_time_step_students
AS
(
    SELECT student_id, CONCAT(module_id, ".", lesson_position) AS Урок, MAX(submission_time) AS max_time
    FROM lesson JOIN step USING(lesson_id)
    JOIN step_student USING(step_id)
    WHERE result = "correct"
    GROUP BY student_id, Урок
)
SELECT student_name AS Студент, Урок, FROM_UNIXTIME(max_time) AS Макс_время_отправки, IFNULL(CEIL((max_time - LAG(max_time) OVER (PARTITION BY student_name ORDER BY max_time))/86400), "-") AS Интервал
FROM students_3lessons JOIN max_time_step_students USING(student_id)
JOIN student USING(student_id)
ORDER BY student_name, max_time;