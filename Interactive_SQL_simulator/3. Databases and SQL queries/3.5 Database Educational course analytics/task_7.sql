/*Задание
Для студента с именем student_61 вывести все его попытки: название шага, результат и дату отправки попытки (submission_time). Информацию отсортировать по дате отправки попытки и указать, сколько минут прошло между отправкой соседних попыток. Название шага ограничить 20 символами и добавить "...". Столбцы назвать Студент, Шаг, Результат, Дата_отправки, Разница.*/

SELECT student_name Студент, CONCAT(LEFT(step_name, 20), '...') Шаг, result Результат,
       FROM_UNIXTIME(submission_time) Дата_отправки,
       SEC_TO_TIME(-IFNULL(LAG(submission_time) 
              OVER (ORDER BY  submission_time) - submission_time, 
              0)) Разница  
FROM student JOIN step_student USING (student_id)
             JOIN step USING (step_id)
WHERE student_name = 'student_61';