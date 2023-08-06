import os
from ..config import get_config
from ..process import run_cmd

bwa_cmd_script_p = r"""{bwa} mem -t {thread} -M -R "@RG\tID:{sample}\tSM:{sample}\tLB:WES\tPL:Illumina" {genome} {fq1} {fq2}  1>{samfile}"""
bwa_cmd_script_s = r"""{bwa} mem -t {thread} -M -R "@RG\tID:{sample}\tSM:{sample}\tLB:WES\tPL:Illumina" {genome} {fq1} 1>{samfile}"""

sort_index_cmd_script = """
{samtools} view -b -u -S {samfile}>{viewedbam}
{samtools} sort -@ 8 {viewedbam} {sample}
{samtools} index {sample}.bam
rm {samfile} {viewedbam}
"""

def alignment(fq1, fq2, sample, genome, thread=8):
    """
    Map fastq sequences against reference genome using BWA for GATK analysis.
    
    Add ReadGroup(more details about ReadGroup_ )to bamfile using the input sample name.
    Outfile is in BAM format and indexed for the downstream analysis.

    .. _ReadGroup: https://software.broadinstitute.org/gatk/documentation/article.php?id=6472

    Usage:
    ::
      #Commandline
      baseqSNV run_bwa -1 Reads.1.fq.gz -2 Read.2.fq.gz -g hg38 -n TestSample
      #
      from baseqSNV import alignment
      alignment("sample.1.fq.gz", "sample.2.fq.gz", "Sample", "hg19")

    Return:
    ::
      Sample.bam
      Sample.bam.bai
    """
    bwa = get_config("SNV", "bwa")
    samtools = get_config("SNV", "samtools")
    genome = get_config("SNV_ref_"+genome, "bwa_index")
    viewedbam = sample + ".view.bam"
    samfile = sample + ".sam"
    
    if fq1 and fq2 and os.path.exists(fq1) and os.path.exists(fq2):
        bwa_cmd = bwa_cmd_script_p.format(bwa=bwa, sample=sample, genome=genome, fq1=fq1, fq2=fq2, samfile=samfile, thread=thread)
    elif fq1 and os.path.exists(fq1):
        bwa_cmd = bwa_cmd_script_s.format(bwa=bwa, sample=sample, genome=genome, fq1=fq1, samfile=samfile, thread=thread)
    sort_index_cmd=sort_index_cmd_script.format(samtools=samtools, sample=sample, samfile=samfile,viewedbam=viewedbam)
    run_cmd("bwa alignment", "".join(bwa_cmd))
    run_cmd("samtools sort", "".join(sort_index_cmd))
    return bwa_cmd+"\n"+sort_index_cmd