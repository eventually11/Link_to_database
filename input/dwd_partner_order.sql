--INSERT INTO dwd_saas_partner_order 
with ri as
(select DISTINCT address,latitude,longitude from route_info) 

select a.*, ri.latitude end_lat, ri.longitude end_lag 

FROM
	(select ospo.*,ri.latitude start_lat,ri.longitude start_lag from ods_saas_partner_order ospo
	left join  ri
	on ospo.start= ri.address
) a
left join route_info  ri on a.`end` = ri.address