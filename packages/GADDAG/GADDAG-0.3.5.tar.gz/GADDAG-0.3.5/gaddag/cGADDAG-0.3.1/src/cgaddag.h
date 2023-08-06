#ifndef GADDAG_H_INCLUDED
#define GADDAG_H_INCLUDED
/* Maximum number of edges (characters) a node can have */
extern const unsigned int GDG_MAX_CHARS;

typedef struct Result_Struct* Result;
typedef struct GADDAG_Struct* GADDAG;

struct Result_Struct {
    char* str;
    Result next;
    Result prev;
};

struct GADDAG_Struct {
    uint32_t cap;
    uint32_t num_words;
    uint32_t num_nodes;
    uint32_t num_edges;
    uint32_t *edges;
    uint32_t *letter_sets;
};

/* Create a new GADDAG */
GADDAG gdg_create(void);

/* Save a GADDAG to file */
_Bool gdg_save(GADDAG gdg, char *path);

/* Load a GADDAG from file */
GADDAG gdg_load(char *path);

/* Destroy a GADDAG */
void gdg_destroy(GADDAG gdg);

/* Add a word to a GADDAG */
/* Returns: */
/*     0 if the word was successfully added */
/*     1 if the word contains invalid characters */
/*     2 if the word could not be added to the GADDAG due to running */
/*         out of memory, leaving the GADDAG in an undefined state */
int gdg_add_word(GADDAG gdg, char *word);

/* Check if a GADDAG contains a word */
_Bool gdg_has(GADDAG gdg, char *word);

/* Get all words in a GADDAG which start with a prefix */
Result gdg_starts_with(GADDAG gdg, char *prefix);

/* Get all words in a GADDAG which contain a substring */
Result gdg_contains(GADDAG gdg, char *sub);

/* Get all words in a GADDAG which end with a suffix */
Result gdg_ends_with(GADDAG gdg, char *suffix);

/* Place the edges of a node into a buffer */
void gdg_edges(GADDAG gdg, uint32_t node, char *buffer);

/* Place the letter set of a node into a buffer */
void gdg_letter_set(GADDAG gdg, uint32_t node, char *buffer);

/* Check if a character is part of a node's letter set */
_Bool gdg_is_end(GADDAG gdg, uint32_t node, char ch);

/* Follow an edge from a node, returning 0 if no such edge exists */
uint32_t gdg_follow_edge(GADDAG gdg, uint32_t node, char ch);

/* Destroy a Result */
void gdg_destroy_result(Result res);
#endif

