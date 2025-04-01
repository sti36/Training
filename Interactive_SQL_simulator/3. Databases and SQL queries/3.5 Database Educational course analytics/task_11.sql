/*Задание
Для студента с именем student_59 вывести следующую информацию по всем его попыткам:

информация о шаге: номер модуля, символ '.', позиция урока в модуле, символ '.', позиция шага в модуле;
порядковый номер попытки для каждого шага - определяется по возрастанию времени отправки попытки;
результат попытки;
время попытки (преобразованное к формату времени) - определяется как разность между временем отправки попытки и времени ее начала, в случае если попытка длилась более 1 часа, то время попытки заменить на среднее время всех попыток пользователя по всем шагам без учета тех, которые длились больше 1 часа;
относительное время попытки  - определяется как отношение времени попытки (с учетом замены времени попытки) к суммарному времени всех попыток  шага, округленное до двух знаков после запятой  .
Столбцы назвать  Студент,  Шаг, Номер_попытки, Результат, Время_попытки и Относительное_время. Информацию отсортировать сначала по возрастанию id шага, а затем по возрастанию номера попытки (определяется по времени отправки попытки).

Важно. Все вычисления производить в секундах, округлять и переводить во временной формат только для вывода результата.*/

/* Определение id студента с именем 'student_59'*/
SET @student_59_id := (SELECT student_id FROM student WHERE student_name = 'student_59');

/* Создание переменной, содержащей среднюю продолжительность попытки студента с именем 'student_59' */
SET @avg_attempt_duration := (
    SELECT ROUND(AVG(submission_time - attempt_time))
    FROM step_student
    WHERE (student_id = @student_59_id) AND ((submission_time - attempt_time) / 3600 < 1)
    );

/* Создание столбца <Время_попытки> в секундах */
WITH get_attempt_duration (step_student_id, attempt_duration) AS (
        SELECT
            step_student_id,
            IF((submission_time - attempt_time) / 3600 < 1,
            submission_time - attempt_time,
            @avg_attempt_duration)
        FROM step_student
        WHERE student_id = @student_59_id
        )

/* Основной запрос */
SELECT
    'student_59' AS Студент,
    CONCAT(module_id, '.', lesson_position, '.', step_position) AS Шаг,
    ROW_NUMBER() OVER (PARTITION BY step_id ORDER BY submission_time) AS Номер_попытки,
    result AS Результат,
    SEC_TO_TIME(attempt_duration) AS Время_попытки,
    ROUND((attempt_duration / (SUM(attempt_duration)
    OVER (PARTITION BY step_id))) * 100, 2) AS Относительное_время
FROM lesson
    JOIN step USING (lesson_id)
    JOIN step_student USING (step_id)
    JOIN get_attempt_duration USING (step_student_id)
WHERE student_id = @student_59_id
ORDER BY step_id, 3;