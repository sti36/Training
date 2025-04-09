/*Задание
Автор - Лариса Фернандес

Найти вопрос, с самой большой успешностью выполнения - "самый легкий" и вопрос, с самой маленькой успешностью выполнения - "самый сложный".  (Подробно про успешность на этом шаге). Вывести предмет, эти два вопроса и указание - самый сложный или самый легкий это вопрос. Сначала вывести самый легкий запроса, потом самый сложный.*/

SELECT name_subject, name_question,
       IF(MAX(is_correct) = false, "самый сложный", "самый легкий")  AS Сложность
FROM subject INNER JOIN question USING (subject_id)
             INNER JOIN testing USING (question_id)
             INNER JOIN answer USING (answer_id)
GROUP BY name_subject, name_question
HAVING MAX(is_correct) = false OR MIN(is_correct) = true
ORDER BY Сложность;