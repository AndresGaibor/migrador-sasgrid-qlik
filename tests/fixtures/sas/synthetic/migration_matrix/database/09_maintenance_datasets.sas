/* priority: P1 */
proc datasets library=work nolist; copy out=work_backup; delete scratch_one scratch_two; quit;
