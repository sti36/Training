/*Задание
Сравнить ежемесячную выручку от продажи книг за текущий и предыдущий годы. Для этого вывести год, месяц, сумму выручки в отсортированном сначала по возрастанию месяцев, затем по возрастанию лет виде. Название столбцов: Год, Месяц, Сумма.*/

SELECT YEAR(date_payment) AS Год, MONTHNAME(date_payment) AS Месяц, SUM(price * amount) AS Сумма
FROM buy_archive
GROUP BY YEAR(date_payment), MONTHNAME(date_payment)
UNION
SELECT YEAR(date_step_end) AS Год, MONTHNAME(date_step_end) AS Месяц, SUM(price * buy_book.amount) AS Сумма
FROM book
    INNER JOIN buy_book ON book.book_id = buy_book.book_id
    INNER JOIN buy ON buy.buy_id = buy_book.buy_id
    INNER JOIN buy_step ON buy.buy_id = buy_step.buy_id
    INNER JOIN step ON buy_step.step_id = step.step_id
WHERE name_step = 'Оплата' AND
       date_step_end IS NOT NULL
GROUP BY YEAR(date_step_end), MONTHNAME(date_step_end)
ORDER BY Месяц, Год;