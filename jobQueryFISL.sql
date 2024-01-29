/*CANCELADO=A, TERMINADO=F, LIBERADO=S, PLANEADO=P, LISTO=Y, ACTIVO=R, DESCONOCIDO=X*/
SELECT JOBNAME as JOB,SDLUNAME as USUARIO,STRTDATE as F_Inicio,STRTTIME as H_Inicio,ENDDATE as F_FINAL,ENDTIME as H_FINAL,CASE WHEN STATUS = 'F' THEN 'FINALIZADO' END as ESTADO  FROM SAPABAP1.TBTCO WHERE STATUS = 'F' AND SDLSTRTDT = ADD_DAYS(CURRENT_DATE,-1) AND JOBNAME LIKE '%FISL%'