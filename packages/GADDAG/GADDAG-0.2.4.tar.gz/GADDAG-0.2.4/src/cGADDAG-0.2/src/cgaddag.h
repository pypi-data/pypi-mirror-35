#ifndef GADDAG_H_INCLUDED
#define GADDAG_H_INCLUDED
extern uint8_t MAX_CHARS;
extern uint32_t DEFAULT_CAP;

typedef struct Result_Struct* Result;
typedef struct GADDAG_Struct* GADDAG;

struct Result_Struct {
    char* str;
    Result next;
    Result prev;
};

struct GADDAG_Struct {
    uint32_t *edges;
    uint32_t *letter_sets;
    uint32_t cap;
    uint32_t num_words;
    uint32_t num_nodes;
    uint32_t num_edges;
};

void destroy_result(Result res);

GADDAG newGADDAG(void);
void destroy_GADDAG(GADDAG gdg);
void add_word(GADDAG gdg, char *word);
_Bool has(GADDAG gdg, char *word);
Result starts_with(GADDAG gdg, char *prefix);
Result contains(GADDAG gdg, char *sub);
Result ends_with(GADDAG gdg, char *suffix);
void edges(GADDAG gdg, uint32_t node, char *buffer);
void letter_set(GADDAG gdg, uint32_t node, char *buffer);
_Bool is_end(GADDAG gdg, uint32_t node, char ch);
uint32_t follow_edge(GADDAG gdg, uint32_t node, char ch);
#endif
