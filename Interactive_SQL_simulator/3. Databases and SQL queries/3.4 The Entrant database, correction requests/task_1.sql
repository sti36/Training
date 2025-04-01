/*Задание
Создать вспомогательную таблицу applicant,  куда включить id образовательной программы, id абитуриента, сумму баллов абитуриентов (столбец itog) в отсортированном сначала по id образовательной программы, а потом по убыванию суммы баллов виде (использовать запрос из предыдущего урока).*/

CREATE TABLE applicant
SELECT program_id, enrollee_id, SUM(result) itog
FROM program_enrollee
     JOIN program_subject USING (program_id)
     JOIN enrollee_subject USING (subject_id, enrollee_id)
GROUP BY  enrollee_id, program_id
ORDER BY program_id, itog DESC;