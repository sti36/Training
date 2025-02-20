/*Задание
Вывести все жанры, которые не представлены в книгах на складе.*/

SELECT name_genre
FROM genre LEFT JOIN book 
    ON book.genre_id = genre.genre_id
WHERE book.genre_id is NULL