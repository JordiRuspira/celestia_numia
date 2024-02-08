SELECT  
  left(a.block_timestamp, 10) as transformed_date,
  JSON_EXTRACT_SCALAR(JSON_EXTRACT(a.message, '$.namespaces'), '$[0]') AS namespace_value,
  sum(fee_numeric) as total_fees,
  SUM(CAST(JSON_EXTRACT_SCALAR(JSON_EXTRACT(a.message, '$.blob_sizes'), '$[0]') AS INT64))/pow(10, 6) AS mb_posted
FROM 
  numia-data.celestia.celestia_tx_messages a 
  left join 
  (SELECT  tx_id,
    CAST(REGEXP_EXTRACT(fee, r'^(\d+)utia') AS INT64)/pow(10,6) AS fee_numeric
FROM 
  numia-data.celestia.celestia_transactions) b
  on a.tx_id = b.tx_id
WHERE 
  a.message_type = '/celestia.blob.v1.MsgPayForBlobs'
GROUP BY 
  transformed_date, namespace_value
