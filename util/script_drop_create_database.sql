/***  drop / create database 
DROP DATABASE IF EXISTS abcmobile;

CREATE DATABASE abcmobile;
***/
/**************************************/
/* User */
select * from abcmobile.auth_user u 
 where 1=1
 --  and u.username = '2586809629.0' -- ; '0829.168.572-4'
   and u.is_superuser = 0
   ;
ALTER TABLE `abcmobile`.`auth_user` 
AUTO_INCREMENT = 1 ;


/* Periodo Letivo */
select * from abcmobile.portal_periodoletivo;

/* Aluno */
select * from abcmobile.portal_aluno;

/* Professor */
select * from abcmobile.portal_professor P 
 WHERE 1=1 
  AND P.nome = 'Josinês Luz Santos';

/* Boletim */
select * from abcmobile.portal_boletim b where 1=1 ;
-- delete from abcmobile.portal_boletim

ALTER TABLE `abcmobile`.`portal_boletim` 
AUTO_INCREMENT = 1 ;


