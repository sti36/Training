/*Задание
Для книг, которые уже есть на складе (в таблице book), но по другой цене, чем в поставке (supply),  необходимо в таблице book увеличить количество на значение, указанное в поставке,  и пересчитать цену. А в таблице  supply обнулить количество этих книг. Формула для пересчета цены:
price=(p1∗k1+p2∗k2)/k1+k2
где  p1, p2 - цена книги в таблицах book и supply;
k1, k2 - количество книг в таблицах book и supply. */

UPDATE book b
    INNER JOIN author a USING(author_id)
    INNER JOIN supply s ON b.title=s.title
        AND a.name_author=s.author
SET b.amount=b.amount + s.amount,
    b.price=(b.price*b.amount + s.price*s.amount)/(b.amount+s.amount),
    s.amount=0
WHERE b.price <> s.price;