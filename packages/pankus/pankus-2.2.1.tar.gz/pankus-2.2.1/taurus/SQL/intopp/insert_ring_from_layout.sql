INSERT INTO ring
SELECT DISTINCT
    p1p2w.p1id,
    p1p2w.p2id,
    (SELECT
        ring_number
    FROM
        ring_layout as rl
    WHERE
        rl.od_id=p1 AND
        rl.prior_rings_size <= p1p2w.weight AND
        rl.prior_rings_size + rl.ring_size > p1p2w.weight
    LIMIT 1)
FROM
    (SELECT
        p1.od_id, as p1id
        p2_od_id, as p2id
        (SELECT
            weight
        FROM
            distance as d
        WHERE
            d.start_id=p1.id AND
            d.end_id=p2.id
        LIMIT 1) as weight
    FROM
        point as p1,
        point as p2
    WHERE
        p1.od_id NOT NULL AND
        p2.od_id NOT NULL) as p1p2w;
