/*Задание
Вывести номера всех оплаченных заказов и даты, когда они были оплачены.*/

SELECT buy_id, date_step_end 
FROM step
    INNER JOIN buy_step ON step.step_id = buy_step.step_id
WHERE buy_step.step_id = 1 and date_step_end IS NOT Null;