/*Задание
Вывести жанр (или жанры), в котором было заказано больше всего экземпляров книг, указать это количество. Последний столбец назвать Количество.*/

SELECT name_genre, Количество
FROM (
  SELECT name_genre, SUM(buy_book.amount) as Количество,
      ROW_NUMBER() OVER (ORDER BY SUM(buy_book.amount) DESC) AS row_num
  FROM genre
  JOIN book USING(genre_id)
  JOIN buy_book USING(book_id)
  GROUP BY name_genre
) AS subquery
WHERE row_num = 1;