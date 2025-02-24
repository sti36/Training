/*Задание
В таблицу buy_book добавить заказ с номером 5. Этот заказ должен содержать книгу Пастернака «Лирика» в количестве двух экземпляров и книгу Булгакова «Белая гвардия» в одном экземпляре.*/

INSERT INTO buy_book(buy_id, book_id, amount)
VALUES
    (5, (SELECT book_id FROM book WHERE title = 'Лирика'), 2),
    (5, (SELECT book_id FROM book WHERE title = 'Белая гвардия'), 1);

SELECT * FROM buy_book;