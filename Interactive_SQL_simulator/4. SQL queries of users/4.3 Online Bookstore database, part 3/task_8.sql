/*Задание
автор - Лариса Фернандес

В последний заказ (таблица buy_book) клиента Баранов Павел добавить по одному экземпляру всех книг Достоевского, которые есть в таблице book.*/

INSERT INTO buy_book(buy_id, book_id, amount)
SELECT MAX(buy_id), book_id, 1
FROM author
    INNER JOIN book ON author.author_id = book.author_id AND name_author LIKE 'Достоевский%'
    CROSS JOIN buy
    INNER JOIN client ON buy.client_id = client.client_id AND name_client LIKE 'Баранов%'
GROUP BY book_id;
SELECT * FROM buy_book