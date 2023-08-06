import os
from baseq.mgt import get_config, run_cmd

bqsr_cmd_script = """
{gatk} BaseRecalibrator -R {index} -L {interval} -I {markedbam} --known-sites {dbsnp} --known-sites {snp} --known-sites {indel} -O {markedbam}.table
{gatk} ApplyBQSR -R {index} -L {interval} -I {markedbam} -bqsr {markedbam}.table -O {bqsrbam}
"""

bqsr_cmd_script_DRF = """
{gatk} BaseRecalibrator -R {index} -L {interval} -I {markedbam} --known-sites {dbsnp} --known-sites {snp} --known-sites {indel} --disable-read-filter NotDuplicateReadFilter -O {markedbam}.table
{gatk} ApplyBQSR -R {index} -L {interval} -I {markedbam} -bqsr {markedbam}.table --disable-read-filter NotDuplicateReadFilter -O {bqsrbam}
"""

def bqsr(markedbam, bqsrbam, genome, disable_dup_filter=False):
    """
    Run BQSR_. This function performs the two-steps process called base quality score recalibration. the first
    ster generates a recalibration table based on various covariates which is recruited to the second step to
    correct the systematic bias in input BAM file. More details about BaseRecalibrator_ and ApplyBQSR_ .


    .. _BQSR: https://gatkforums.broadinstitute.org/gatk/discussion/44/base-quality-score-recalibration-bqsr
    .. _BaseRecalibrator: https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_BaseRecalibrator.php
    .. _ApplyBQSR: https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_ApplyBQSR.php

    Usage:

    * Default mode filters duplicate reads (reads with "markduplicate" tags) before applying BQSR
      ::
         baseq-SNV run_bqsr -m Test.marked.bam -g hg38 -q Test.marked.bqsr.bam

    * Disable reads filter before analysis.
      ::
        baseq-SNV run_bqsr -m Test.marked.bam -g hg38 -q Test.marked.bqsr.bam -f Yes

    Return:
    ::
      Test.marked.bam.table
      Test.marked.bqsr.bai
      Test.marked.bqsr.bam
    """
    gatk = get_config("SNV", "GATK")
    index = get_config("SNV_ref_"+genome,"bwa_index")
    DBSNP = get_config("SNV_ref_"+genome,"DBSNP")
    SNP = get_config("SNV_ref_"+genome,"SNP")
    INDEL = get_config("SNV_ref_"+genome,"INDEL")
    interval = get_config("SNV_ref_"+genome,"interval")


    #Default, we use the read filter...
    if not disable_dup_filter:
        bqsr_cmd = bqsr_cmd_script.format(gatk=gatk, index=index, interval=interval, markedbam=markedbam,
                                          bqsrbam=bqsrbam, dbsnp=DBSNP, snp=SNP, indel=INDEL)
    #We can also disable the read filter...
    else:
        bqsr_cmd = bqsr_cmd_script_DRF.format(gatk=gatk, index=index, interval=interval, markedbam=markedbam,
                                          bqsrbam=bqsrbam, dbsnp=DBSNP, snp=SNP, indel=INDEL)
    run_cmd("BaseRecalibrator","".join(bqsr_cmd))
