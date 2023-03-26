--Знайти список курсів, які відвідує студент.--

SELECT d.name
FROM grades g
JOIN disciplines d ON d.id = g.discipline_id
JOIN students s  ON s.id = g.student_id 
WHERE s.id = 4
GROUP BY d.name;