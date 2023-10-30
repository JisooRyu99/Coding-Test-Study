-- https://school.programmers.co.kr/learn/courses/30/lessons/132201

SELECT PT_NAME,PT_NO,GEND_CD,AGE,IFNULL(TLNO,'NONE') FROM PATIENT
WHERE GEND_CD='W' AND AGE<=12
order by AGE DESC, PT_NAME ASC