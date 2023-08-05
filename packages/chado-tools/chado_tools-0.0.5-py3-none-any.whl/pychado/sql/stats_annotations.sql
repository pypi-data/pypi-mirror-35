/*
 * This query returns all changes in annotation/gene model since the latest release
 */
SELECT
    organism.abbreviation AS organism_name,
	feature1.uniquename AS transcript_id,
	feature2.uniquename AS gene_id,
	property2.value AS date,
	property1.value AS annotation
FROM
	feature_cvterm fcvt, feature_cvtermprop property1, feature_cvtermprop property2, feature_relationship relation1 , feature feature1, feature_relationship relation2, feature feature2, organism
WHERE
    fcvt.cvterm_id IN (SELECT cvterm_id FROM cvterm JOIN cv USING (cv_id) WHERE cv.name = 'annotation_change')		-- capture all changes in annotation
    and
    (fcvt.feature_cvterm_id = property1.feature_cvterm_id
    AND
	property1.type_id IN (SELECT cvterm_id FROM cvterm WHERE name = 'qualifier'))	-- get annotation description
	and
    (fcvt.feature_cvterm_id = property2.feature_cvterm_id
	AND
	property2.type_id IN (SELECT cvterm_id FROM cvterm WHERE name = 'date')			-- capture any commits since the latest release
	AND
	property2.value > '20180101')
	AND
	relation1.subject_id = fcvt.feature_id
	and
	relation1.object_id = feature1.feature_id
	and
	relation1.type_id IN (SELECT cvterm_id FROM cvterm WHERE name = 'derives_from')	-- gene product 'derives from' transcript
	and
	relation2.subject_id = feature1.feature_id
	and
	relation2.object_id = feature2.feature_id
	and
	relation2.type_id IN (SELECT cvterm_id FROM cvterm WHERE name = 'part_of')
	and
	feature1.organism_id = feature2.organism_id
	and
	feature2.organism_id = organism.organism_id
	AND
	TRUE	-- a specific organism
ORDER BY
	organism_name,
	transcript_id,
	date,
	annotation
