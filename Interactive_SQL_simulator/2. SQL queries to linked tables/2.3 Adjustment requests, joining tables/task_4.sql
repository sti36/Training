/*Задание
 Занести для книги «Стихотворения и поэмы» Лермонтова жанр «Поэзия», а для книги «Остров сокровищ» Стивенсона - «Приключения». (Использовать два запроса).*/

 UPDATE book b
INNER JOIN author a ON  a.author_id = b.author_id
SET b.genre_id = (
    SELECT g.genre_id
    FROM genre g
    WHERE g.name_genre = CASE
        WHEN b.title = 'Стихотворения и поэмы' AND a.name_author LIKE 'Лермонтов%' THEN 'Поэзия'
        WHEN b.title = 'Остров сокровищ' AND a.name_author LIKE 'Стивенсон%' THEN 'Приключения'
        END)
WHERE a.name_author LIKE 'Лермонтов%' OR a.name_author LIKE 'Стивенсон%';

SELECT * FROM book;