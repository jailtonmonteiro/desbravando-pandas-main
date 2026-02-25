SELECT IdTransacao,
    sum(t1.QtdeProduto) AS totalproduct,
    count(DISTINCT t1.IdProduto) AS qtdTransacoes

FROM transacao_produto AS t1

GROUP BY IdProduto