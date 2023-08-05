#ifndef CHEMFP_INTERNAL_H
#define CHEMFP_INTERNAL_H

#define ALIGNMENT(POINTER, BYTE_COUNT) \
  (((uintptr_t)(const void *)(POINTER)) % (BYTE_COUNT))


/* Macro to use for variable names which exist as a */
/* function parameter but otherwise aren't used */
/* This is to prevent compiler warnings on msvc /W4 */
#define UNUSED(x) (void)(x);


int chemfp_get_option_report_popcount(void);
int chemfp_set_option_report_popcount(int);

int chemfp_get_option_report_intersect_popcount(void);
int chemfp_set_option_report_intersect_popcount(int);

int chemfp_get_option_report_algorithm(void);
int chemfp_set_option_report_algorithm(int);

int chemfp_get_option_use_specialized_algorithms(void);
int chemfp_set_option_use_specialized_algorithms(int);

int chemfp_get_option_num_column_threads(void);
int chemfp_set_option_num_column_threads(int);


int chemfp_add_hit(chemfp_search_result *result, int target_index, double score);

/* Scaling factor to convert floats and doubles into integers */
#define CHEMFP_FLOAT_SCALE 10000

#endif
