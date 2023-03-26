--Знайти середній бал на потоці (по всій таблиці оцінок).--

SELECT ROUND(AVG(g.grade),2) as avg_grade
FROM grades g 
ORDER BY avg_grade DESC;