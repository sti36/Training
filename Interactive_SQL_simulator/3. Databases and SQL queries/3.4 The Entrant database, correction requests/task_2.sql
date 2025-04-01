/*Задание
Из таблицы applicant, созданной на предыдущем шаге, удалить записи, если абитуриент на выбранную образовательную программу не набрал минимального балла хотя бы по одному предмету (использовать запрос из предыдущего урока).*/

DELETE FROM applicant
USING applicant JOIN program_subject USING(program_id)
                JOIN enrollee_subject USING(enrollee_id, subject_id)
WHERE result < min_result;