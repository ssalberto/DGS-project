import mysql.connector


def init_queries():
    annotateTable = '''
    CREATE TABLE annotation (
        id INT AUTO_INCREMENT PRIMARY KEY,
        impact TEXT,
        consequences TEXT,
        allele TEXT,
        variant_rs_id VARCHAR(16),
        FOREIGN KEY (variant_rs_id) REFERENCES variant(variant_rs_id)
    )
    '''

    variantTable = '''
    CREATE TABLE variant (
        variant_rs_id VARCHAR(16) PRIMARY KEY,
        alt TEXT,
        variant_type TEXT
    )
    '''

    chromosomeSquenceTable = '''
    CREATE TABLE ChromosomeSequence (
        chromosome VARCHAR(16) PRIMARY KEY,
        assembly TEXT
    )
    '''

    locationInfotable = '''
    CREATE TABLE locationInfo (
        pos INTEGER,
        ref TEXT,
        variant_rs_id VARCHAR(16),
        chr VARCHAR(16) NOT NULL,
        PRIMARY KEY (chr, variant_rs_id, pos),
        FOREIGN KEY (variant_rs_id) REFERENCES variant(variant_rs_id),
        FOREIGN KEY (chr) REFERENCES ChromosomeSequence(chromosome)
    )
    '''

    hgvsTable = '''
    CREATE TABLE HGVSExpresion (
        hgvs VARCHAR(32) PRIMARY KEY,
        variant_rs_id VARCHAR(16),
        FOREIGN KEY (variant_rs_id) REFERENCES variant(variant_rs_id)
    )
    '''


    diseaseTable = '''
    CREATE TABLE disease (
        preferred_name VARCHAR(300) PRIMARY KEY
    )
    '''

    interpretationTable = '''
    CREATE TABLE interpretation (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        clinical_significance TEXT,
        method TEXT,
        variant_origin TEXT,
        review_status TEXT,
        submitter TEXT,
        my_database VARCHAR(60) NOT NULL,
        variant_rs_id VARCHAR(16) NOT NULL,
        FOREIGN KEY (my_database) REFERENCES my_database(name),
        FOREIGN KEY (variant_rs_id) REFERENCES variant(variant_rs_id)
    )
    '''

    databaseTable = '''
    CREATE TABLE my_database (
        name VARCHAR(60) PRIMARY KEY,
        url TEXT
    )
    '''

    for_aTable = '''
    CREATE TABLE for_a (
        id_interpretation VARCHAR(16),
        preferred_name VARCHAR(300),
        PRIMARY KEY (id_interpretation, preferred_name),
        FOREIGN KEY (id_interpretation) REFERENCES interpretation(variant_rs_id),
        FOREIGN KEY (preferred_name) REFERENCES disease(preferred_name)
    )
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
