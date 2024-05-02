import mysql.connector

def init_queries():
    annotateTable = '''
    INSERT INTO annotation (impact, consequences, allele, variant_rs_id)
    VALUES ('HIGH', 'frameshift_variant', 'TA', '587781299'),
        ('HIGH', 'frameshift_variant', 'C', '180177102'),
        ('MODERATE', 'missense_variant', 'G', '80356993'),
        ('HIGH', 'splice_acceptor_variant&intron_variant', 'A', '80358158');
    '''

    variantTable = '''
    INSERT INTO variant (variant_rs_id, alt, variant_type)
    VALUES ('587781299', 'TA', 'Duplication'),
        ('180177102', 'C', 'Deletion'),
        ('80356993', 'G', 'single_nucleotide_variant'),
        ('80358158', 'A', 'single_nucleotide_variant');
    '''

    chromosomeSquenceTable = '''
    INSERT INTO ChromosomeSequence (chromosome, assembly)
    VALUES ('11', 'hg19'),
        ('16', 'hg19'),
        ('17', 'hg19');
    '''

    locationInfotable = '''
    INSERT INTO locationInfo (pos, ref, chr, variant_rs_id)
    VALUES (108198392, 'T', '11', '587781299'),
        (23646274, 'CA', '16', '180177102'),
        (41215954, 'A', '17', '80356993'),
        (41258551, 'C', '17', '80358158');
    '''

    hgvsTable = '''
    INSERT INTO HGVSExpresion (hgvs, variant_rs_id)
    VALUES ('NC_000011.9:g.108198393dup', '587781299'),
        ('NC_000016.9:g.23646278del', '180177102'),
        ('NC_000017.10:g.41215954A>G', '80356993'),
        ('NC_000017.10:g.41258551C>A', '80358158');
    '''


    diseaseTable = '''
    INSERT INTO disease (preferred_name)
    VALUES ('Ataxia-telangiectasia_syndrome'),
        ('Familial_cancer_of_breast'),
        ('not_provided'),
        ('Hereditary_cancer-predisposing_syndrome'),
        ('Breast_cancer,_susceptibility_to'),
        ('Hereditary_breast_ovarian_cancer_syndrome'),
        ('Malignant_tumor_of_breast'),
        ('Breast-ovarian_cancer,_familial,_susceptibility_to,_1'),
        ('Pancreatic_cancer,_susceptibility_to,_4'),
        ('Fanconi_anemia,_complementation_group_S');
    '''

    interpretationTable = '''
    INSERT INTO interpretation (clinical_significance, method, variant_origin, review_status, submitter, variant_rs_id, my_database)
    VALUES ('Pathogenic', 'snpSift', '1', 'reviewed_by_expert_panel', 'ClinGen', '587781299', 'ClinGen'),
        ('Pathogenic', 'snpSift', '1', 'reviewed_by_expert_panel', 'ClinGen', '180177102', 'ClinGen'),
        ('Pathogenic', 'snpSift', '1', 'reviewed_by_expert_panel', 'ClinGen', '80356993', 'ClinGen'),
        ('Pathogenic', 'snpSift', '1', 'reviewed_by_expert_panel', 'Breast_Cancer_Information_Core_(BIC)_(BRCA1)', '80358158', 'Breast_Cancer_Information_Core_(BIC)_(BRCA1)');
    '''

    databaseTable = '''
    INSERT INTO my_database (name, url)
    VALUES ('ClinGen', 'https://www.ncbi.nlm.nih.gov/clinvar/'),
        ('Breast_Cancer_Information_Core_(BIC)_(BRCA1)', 'https://www.ncbi.nlm.nih.gov/clinvar/');
    '''

    for_aTable = '''
    INSERT INTO for_a (preferred_name, id_interpretation)
    VALUES ('Ataxia-telangiectasia_syndrome', '587781299'),
        ('Familial_cancer_of_breast', '587781299'),
        ('Hereditary_cancer-predisposing_syndrome', '587781299'),
        ('not_provided', '587781299'),
        ('Hereditary_cancer-predisposing_syndrome', '180177102'),
        ('not_provided', '180177102'),
        ('Breast_cancer,_susceptibility_to', '180177102'),
        ('Hereditary_breast_ovarian_cancer_syndrome', '180177102'),
        ('Familial_cancer_of_breast', '180177102'),
        ('Hereditary_cancer-predisposing_syndrome', '80356993'),
        ('not_provided', '80356993'),
        ('Malignant_tumor_of_breast', '80356993'),
        ('Hereditary_breast_ovarian_cancer_syndrome', '80356993'),
        ('Breast-ovarian_cancer,_familial,_susceptibility_to,_1', '80356993'),
        ('Hereditary_cancer-predisposing_syndrome', '80358158'),
        ('Hereditary_breast_ovarian_cancer_syndrome', '80358158'),
        ('Malignant_tumor_of_breast', '80358158'),
        ('Familial_cancer_of_breast', '80358158'),
        ('Pancreatic_cancer,_susceptibility_to,_4', '80358158'),
        ('Fanconi_anemia,_complementation_group_S', '80358158'),
        ('Breast-ovarian_cancer,_familial,_susceptibility_to,_1', '80358158'),
        ('not_provided', '80358158');
    '''

    return [annotateTable, variantTable, hgvsTable, chromosomeSquenceTable, locationInfotable, diseaseTable, databaseTable, interpretationTable, for_aTable]

def init_connection():
    # Database credentials
    db_name = 'bembogzwheeytajy6wqi'
    user = 'ueegmnxqcoesneek'
    password = 'M90MAudryp09adcA7Yt0'
    host = 'bembogzwheeytajy6wqi-mysql.services.clever-cloud.com'

    # Establish the connection
    connection = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=db_name
    )

    # Create a cursor to execute queries
    cursor = connection.cursor()

    return connection, cursor

if __name__ == "__main__":
    #Establish the connection with the database
    connection, cursor = init_connection()

    # Initialize the queries to perform
    queries = init_queries()

    # Make a query
    for query in queries:
        cursor.execute(query)

    # Confirm the changes and close the connection
    connection.commit()
    connection.close()