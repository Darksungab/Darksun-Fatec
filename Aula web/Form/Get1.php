<?php

$Email = addcslashes($_GET'email');
$Nome = addcslashes ($_GET'Nome');
$Setor = $_GET('Setor');
$Data_de_Incidente = $_GET('Data de Incidente');
$Desc_incidente = $_GET('$Desc_incidente')

$Destino = "gabriel.ribeiro77@fatec.sp.gov.br";
$Assunto = "Solicitação de Suporte";

$Estrutura_Email = "Email: " .$Email. "\n"."Nome: " .$Nome. "\n"."Setor: " .$Setor. "\n"."Data do Incidente" .$Data_de_Incidente. "\n". "Descrição do Incidente" .$Desc_incidente. "\n".


?>