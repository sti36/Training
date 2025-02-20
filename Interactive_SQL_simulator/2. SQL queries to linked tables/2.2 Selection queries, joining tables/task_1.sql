/*Задание
Вывести название, жанр и цену тех книг, количество которых больше 8, в отсортированном по убыванию цены виде.*/

SELECT title, name_genre, price
FROM genre INNER JOIN book
    ON genre.genre_id = book.genre_id
WHERE book.amount > 8
ORDER BY price DESC