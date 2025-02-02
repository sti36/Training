/*Задание
Удалить из таблицы supply книги тех авторов, общее количество экземпляров книг которых в таблице book превышает 10.*/

DELETE FROM supply
WHERE author IN (
    SELECT author
    FROM book
    GROUP BY author
    HAVING SUM(amount) > 10
);
<<<<<<< HEAD
SELECT * FROM supply  
=======
SELECT * FROM supply
>>>>>>> 7744352a3d982482660b9dfa2d809d7b4af5d963
