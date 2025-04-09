/*Задание
автор -Лариса Фернандес

Для клиентов у которых сумма заказов выше средней по суммам заказов клиентов (общей стоимости всех заказов клиентов), вывести имя, общую сумму всех заказов, количество заказов, количество заказанных книг. Этим клиентам мы предложим специальную программу лояльности! Информацию отсортировать по имени клиентов ( в алфавитном порядке).*/

WITH a AS(SELECT name_client, SUM(buy_book.amount * book.price) Общая_сумма_заказов, 
          COUNT(distinct buy.buy_id) Заказов_всего, SUM(buy_book.amount) Книг_всего 
FROM book 
     JOIN buy_book ON book.book_id = buy_book.book_id
     JOIN buy ON buy_book.buy_id = buy.buy_id
     JOIN client ON buy.client_id = client.client_id
GROUP BY name_client
ORDER BY name_client)

SELECT name_client, Общая_сумма_заказов, 
       Заказов_всего, Книг_всего 
FROM a
WHERE Общая_сумма_заказов > (SELECT AVG(Общая_сумма_заказов) 
                                FROM a)