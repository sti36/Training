/*Задание
Занести в столбец str_id таблицы applicant_order нумерацию абитуриентов, которая начинается с 1 для каждой образовательной программы.*/

SET @str_id = 0;
SET @row_num = 1;
UPDATE applicant_order
SET str_id = IF (program_id = @str_id, @row_num := @row_num + 1, @row_num := 1 AND @str_id := program_id);

SELECT *FROM applicant_order;