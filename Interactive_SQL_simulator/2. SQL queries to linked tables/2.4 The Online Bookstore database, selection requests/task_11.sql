/*Задание
Для каждой отдельной книги необходимо вывести информацию о количестве проданных экземпляров и их стоимости за 2020 и 2019 год . За 2020 год проданными считать те экземпляры, которые уже оплачены. Вычисляемые столбцы назвать Количество и Сумма. Информацию отсортировать по убыванию стоимости.*/

SELECT title, SUM(kol) AS Количество, SUM(summ) AS Сумма 
FROM book 
  INNER JOIN (
    SELECT book_id, SUM(amount) AS kol, SUM(amount * price) AS summ 
    FROM buy_archive 
    GROUP BY book_id 
    UNION 
    SELECT book_id, SUM(buy_book.amount), SUM(buy_book.amount * book.price) 
    FROM buy_book 
      INNER JOIN book USING(book_id) 
      INNER JOIN buy_step USING(buy_id) 
    WHERE step_id = 1 AND date_step_end IS NOT Null 
    GROUP BY book_id
    ) 
    query_1 USING(book_id) 
GROUP BY title 
ORDER BY Сумма DESC