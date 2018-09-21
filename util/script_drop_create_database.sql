/***  drop / create database 
DROP DATABASE IF EXISTS abcmobile;

CREATE DATABASE abcmobile;
***/
/**************************************/
select * from abcmobile.auth_user;
select * from abcmobile.portal_pais;
select * from abcmobile.portal_estado;
select * from abcmobile.portal_cidade where 1=1 and estado_id = '33';
select * from abcmobile.portal_instituicao;
/***
select * from abcmobile.portal_periodoletivo;

select * from abcmobile.portal_responsavel r where 1=1 and r.registro_responsavel = 3;
select * from abcmobile.portal_aluno WHERE 1=1 AND REGISTRO_ALUNO = '3989';
select * from abcmobile.portal_professor;

select * 
-- delete
from abcmobile.portal_boletim
 where 1=1
   and aluno_id = 3989
 ;
select * from abcmobile.portal_boletim2;
**/
select * from abcmobile.portal_tabelaimportacao;
select * from abcmobile.portal_importacaoxls;