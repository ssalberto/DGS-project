import io
import os
import pandas as pd

path ="./files/testAnnSift.vcf"
with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]

def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})

def vcf_variants():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        _, _, _, _, alt, _, _, info, *_ = fields
        rs_id = ''
        var_type = ''
        for field in info.split(';'):
            if field.startswith('RS='):
                rs_id = field.split('=')[1]
            elif field.startswith('CLNVC='):
                var_type = field.split('=')[1]
        data.append([rs_id, alt, var_type])

    return pd.DataFrame(data, columns=['RS_ID', 'ALT', 'VAR_TYPE'])

def vcf_location():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        chr, pos, _, ref, _, _, _, info, *_ = fields
        rs_id = ''
        for field in info.split(';'):
            if field.startswith('RS='):
                rs_id = field.split('=')[1]
        data.append([pos, ref, chr, rs_id])

    return pd.DataFrame(data, columns=['POS', 'REF', 'CHR', 'RS_ID'])

def vcf_annotation():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        _, _, _, _, _, _, _, info, *_ = fields

        impact = ''
        consequences = ''
        allele = ''
        rs_id = ''

        for field in info.split(';'):
            if field.startswith('ANN='):
                ann_info = field.split('=')[1]
                ann_fields = ann_info.split('|')
                impact = ann_fields[2]
                consequences = ann_fields[1]
                allele = ann_fields[0]
            if field.startswith('RS='):
                rs_id = field.split('=')[1]

        data.append([impact, consequences, allele, rs_id])

    return pd.DataFrame(data, columns=['IMPACT', 'CONSEQUENCES', 'ALLELE', 'RS_ID'])

def vcf_interpretation():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        _, _, _, _, _, _, _, info, *_ = fields
        clinical_significance = ''
        method = 'snpSift'
        variant_origin = ''
        review_status = ''
        submitter = ''
        rs_id = ''
        namedb = ''
        for field in info.split(';'):
            if field.startswith('CLNSIG='):
                clinical_significance = field.split('=')[1]
            if field.startswith('ORIGIN='):
                variant_origin = field.split('=')[1]
            if field.startswith('CLNREVSTAT='):
                review_status = field.split('=')[1]
            if field.startswith('CLNVI='):
                submitter = field.split('=')[1].split(':')[0]
            if field.startswith('RS='):
                rs_id = field.split('=')[1]
            if field.startswith('CLNVI='):
                namedb = field.split('=')[1].split(':')[0]

        data.append([clinical_significance, method, variant_origin, review_status, submitter, rs_id, namedb])

    return pd.DataFrame(data, columns=['CLINICAL_SIGNIFICANCE', 'METHOD', 'VARIANT_ORIGIN', 'REVIEW_STATUS', 'SUBMITTER', 'RS_ID', 'NAME_DB'])

def vcf_chromSeq():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        chr, *_ = fields
        assembly = 'hg19'
        data.append([chr, assembly])

    return pd.DataFrame(data, columns=['CHR', 'ASSEMBLY'])

def vcf_disease():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        _, _, _, _, _, _, _, info, *_ = fields
        preferred_name = ''
        for field in info.split(';'):
            if field.startswith('CLNDN='):
                preferred_names = field.split('=')[1]
                preferred_names = preferred_names.split('|')
                for preferred_name in preferred_names:
                    data.append([preferred_name])

    return pd.DataFrame(data, columns=['PREFERRED_NAME'])

def vcf_database():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        _, _, _, _, _, _, _, info, *_ = fields
        name = ''
        url = 'https://www.ncbi.nlm.nih.gov/clinvar/'
        for field in info.split(';'):
            if field.startswith('CLNVI='):
                name = field.split('=')[1].split(':')[0]

        data.append([name, url])

    return pd.DataFrame(data, columns=['NAME', 'URL'])

def vcf_HGVSExpression():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        _, _, _, _, _, _, _, info, *_ = fields
        hgvs = ''
        rs_id = ''
        for field in info.split(';'):
            if field.startswith('CLNHGVS='):
                hgvs = field.split('=')[1]
            if field.startswith('RS='):
                rs_id = field.split('=')[1]
        data.append([hgvs, rs_id])

    return pd.DataFrame(data, columns=['HGVS', 'RS_ID'])

def vcf_interpretation_for_a_disease():
    data = []
    for line in lines:
        if line.startswith('#'):  # Skip header lines
            continue
        fields = line.strip().split('\t')
        _, _, _, _, _, _, _, info, *_ = fields
        for field in info.split(';'):
            if field.startswith('RS='):
                rs_id = field.split('=')[1]
                for field in info.split(';'):
                    if field.startswith('CLNDN='):
                        preferred_names = field.split('=')[1]
                        preferred_names = preferred_names.split('|')
                        for preferred_name in preferred_names:
                            data.append([preferred_name, rs_id])
    return pd.DataFrame(data, columns=['PREFERRED_NAME', 'RS_ID'])

if __name__ == "__main__":
    ## interpretation for_a Disease
    df_interpretation_for_a_disease = vcf_interpretation_for_a_disease()
    df_interpretation_for_a_disease.to_csv('./files/csvfiles/interpretation_for_a_disease.csv', sep=';', index=False, encoding='utf-8-sig')

    ## HGSVExpression
    df_HGVSExpression = vcf_HGVSExpression()
    df_HGVSExpression.to_csv('./files/csvfiles/HGVSExpression.csv', sep=';', index=False, encoding='utf-8-sig')

    ## Database
    df_database = vcf_database()
    df_database.to_csv('./files/csvfiles/database.csv', sep=';', index=False, encoding='utf-8-sig')

    ## Disease
    df_disease = vcf_disease()
    df_disease.to_csv('./files/csvfiles/disease.csv', sep=';', index=False, encoding='utf-8-sig')

    ## Chromosome Sequence
    df_chromSeq = vcf_chromSeq()
    df_chromSeq.to_csv('./files/csvfiles/chromSeq.csv', sep=';', index=False, encoding='utf-8-sig')

    ## Interpretation
    df_interpretation = vcf_interpretation()
    df_interpretation.to_csv('./files/csvfiles/interpretation.csv', sep=';', index=False, encoding='utf-8-sig')

    ## Annotation
    df_annotation = vcf_annotation()
    df_annotation.to_csv('./files/csvfiles/annotation.csv', sep=';', index=False, encoding='utf-8-sig')

    ## Location
    df_location = vcf_location()
    df_location.to_csv('./files/csvfiles/location.csv', sep=';', index=False, encoding='utf-8-sig')

    ## Variants
    df_variants = vcf_variants()
    df_variants.to_csv('./files/csvfiles/variants.csv', sep=';', index=False, encoding='utf-8-sig')