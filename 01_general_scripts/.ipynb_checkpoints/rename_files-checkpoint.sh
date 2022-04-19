#!/bin/bash
DATAFILE=data/
rename ${DATAFILE}GCF_000001635.27_GRCm39_genomic ${DATAFILE}Mus_musculus ${DATAFILE}GCF_000001635.27_GRCm39_genomic*
rename ${DATAFILE}GCF_000003025.6_Sscrofa11.1_genomic ${DATAFILE}Sus_scrofa ${DATAFILE}GCF_000003025.6_Sscrofa11.1_genomic*
rename ${DATAFILE}GCF_000181335.3_Felis_catus_9.0_genomic ${DATAFILE}Felis_catus ${DATAFILE}GCF_000181335.3_Felis_catus_9.0_genomic*
rename ${DATAFILE}GCF_002263795.1_ARS-UCD1.2_genomic ${DATAFILE}Bos_taurus	 ${DATAFILE}GCF_002263795.1_ARS-UCD1.2_genomic*
rename ${DATAFILE}GCF_002863925.1_EquCab3.0_genomic ${DATAFILE}Equus_caballus ${DATAFILE}GCF_002863925.1_EquCab3.0_genomic*
rename ${DATAFILE}GCF_014441545.1_ROS_Cfam_1.0_genomic ${DATAFILE}Canis_lupus_familiaris ${DATAFILE}GCF_014441545.1_ROS_Cfam_1.0_genomic*
rename ${DATAFILE}GCF_015227675.2_mRatBN7.2_genomic ${DATAFILE}Rattus_norvegicus ${DATAFILE}GCF_015227675.2_mRatBN7.2_genomic*
rename ${DATAFILE}GCF_016772045.1_ARS-UI_Ramb_v2.0_genomic ${DATAFILE}Ovis_aries	 ${DATAFILE}GCF_016772045.1_ARS-UI_Ramb_v2.0_genomic*
rename ${DATAFILE}GCF_004115215.2_mOrnAna1.pri.v4_genomic ${DATAFILE}Ornitohoryhynchus_anatinus ${DATAFILE}GCF_004115215.2_mOrnAna1.pri.v4_genomic.*
rename ${DATAFILE}GCF_000002295.2_MonDom5_genomic ${DATAFILE}Monodelphis_domestica ${DATAFILE}GCF_000002295.2_MonDom5_genomic.*

cd ${DATAFILE}
gunzip *.gz