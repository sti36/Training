/*Задание
Повысить итоговые баллы абитуриентов в таблице applicant на значения дополнительных баллов (использовать запрос из предыдущего урока).*/

UPDATE applicant        
SET itog = itog + (SELECT IFNULL(SUM(bonus), 0)
                    FROM enrollee_achievement
                            JOIN achievement USING(achievement_id)
                    WHERE enrollee_id = applicant.enrollee_id);
 
 SELECT * FROM applicant;