import subprocess

def run_commands():
    # snpEff Command
    effCommand = [
        "java",
        "-jar",
        "./snpEff/snpEff.jar",
        "GRCh37.75",
        "./files/test.vcf",
        ">", "./files/testAnnEff.vcf"
    ]
    
    # snpSift Command
    siftCommand = [
        "java",
        "-jar",
        "./snpEff/SnpSift.jar",
        "annotate",
        "./files/clinvar.vcf",
        "./files/testAnnEff.vcf",
        ">", "./files/testAnnSift.vcf"
    ]
    
    # Run Commands
    subprocess.run(effCommand, shell=True)
    subprocess.run(siftCommand, shell=True)

if __name__ == "__main__":
    run_commands()
