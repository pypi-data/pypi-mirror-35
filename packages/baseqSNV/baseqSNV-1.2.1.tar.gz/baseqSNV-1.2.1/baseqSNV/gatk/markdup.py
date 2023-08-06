import os
from ..config import get_config
from ..process import run_cmd

markdup_cmd_script ="""
{java} -Djava.io.tmpdir={tmpdir} -Xmx{memory} -jar {picard} MarkDuplicates INPUT={bamfile} OUTPUT={markedbam} METRICS_FILE={markedbam}.metrics
{samtools} index {markedbam}
"""

def run_markdup(bamfile, markedbam, memory, tmpdir):
    """
    Run MarkDuplicates of Picard. this function tags duplicate reads with "markduplicate" in BAM file.
    See also MarkDuplicates_ in gatk.


    .. _MarkDuplicates: https://software.broadinstitute.org/gatk/documentation/tooldocs/current/picard_sam_markduplicates_MarkDuplicates.php

    Usage:
    ::
      baseq-SNV run_markdup -b Test.bam -m Test.marked.bam -d ./tmp

    Return:
    metrics file indicates the numbers of duplicates for both single- and paired-end reads
    ::
      Test.marked.bam
      Test.marked.bam.bai
      Test.marked.bam.metrics
    """
    java = get_config("SNV", "java")
    picard = get_config("SNV", "picard")
    samtools = get_config("RNA", "samtools")
    cmd = markdup_cmd_script.format(java=java, picard=picard, samtools=samtools, markedbam=markedbam, bamfile=bamfile, memory=memory,tmpdir=tmpdir)
    run_cmd("Mark duplicates","".join(cmd))
    return cmd