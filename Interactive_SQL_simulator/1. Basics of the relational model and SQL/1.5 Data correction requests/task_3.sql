/*Задание
Добавить из таблицы supply в таблицу book, все книги, кроме книг, написанных Булгаковым М.А. и Достоевским Ф.М.*/

INSERT INTO book (title, author, price, amount) 
SELECT title, author, price, amount
FROM supply
<<<<<<< HEAD
WHERE author NOT IN ('Булгаков М.А.', 'Достоевский Ф.М.'); 
=======
WHERE author NOT IN ('Булгаков М.А.', 'Достоевский Ф.М.');
>>>>>>> 7744352a3d982482660b9dfa2d809d7b4af5d963
