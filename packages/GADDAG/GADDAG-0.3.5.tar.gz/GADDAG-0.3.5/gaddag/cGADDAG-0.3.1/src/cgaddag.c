#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#include "cgaddag.h"

/* Maximum number of edges (characters) a node can have */
const unsigned int GDG_MAX_CHARS = 27;

/* Default node capacity of a GADDAG */
uint32_t GDG_DEFAULT_CAP = 100;

/* Internal functions */

Result gdg_create_result(char *str, Result next) {
    /* Create a new Result */
    Result self = (Result)malloc(sizeof(struct Result_Struct));
    if (self == NULL) return NULL;

    if (next) next->prev = self;

    self->str = strdup(str);
    if (self->str == NULL) return NULL;
    self->next = next;
    self->prev = NULL;

    return self;
}

int gdg_ch_to_idx(char ch) {
    /* Turn a character into a bitmask index */
    ch = tolower(ch);
    if (ch == '+') return 0;
    else if (ch == '?') return 31;
    else if (ch >= 97 && ch <= 122) return ch - 96;
    else return -1;
}

char gdg_idx_to_ch(uint8_t idx) {
    /* Turn a bitmask index into a character */
    if (idx == 0) return '+';
    else if (idx >= 1 && idx <= 27) return idx + 96;
    else return '\0';
}

bool gdg_grow(GADDAG gdg, uint32_t new_cap) {
    /* Increase the node capacity of a GADDAG */
    if (new_cap == gdg->cap) return true;
    uint32_t old_cap = gdg->cap;
    gdg->cap = new_cap;

    size_t new_node_size = new_cap * sizeof(uint32_t);
    size_t new_node_diff = (new_cap - old_cap) * sizeof(uint32_t);
    size_t new_edge_size = new_node_size * GDG_MAX_CHARS;
    size_t new_edge_diff = new_node_diff * GDG_MAX_CHARS;

    uint32_t *new_edges = realloc(gdg->edges, new_edge_size);
    if (new_edges == NULL) return false;
    else gdg->edges = new_edges;
    memset(gdg->edges + old_cap * GDG_MAX_CHARS, 0, new_edge_diff);

    uint32_t *new_letter_sets = realloc(gdg->letter_sets, new_node_size);
    if (new_letter_sets == NULL) return false;
    else gdg->letter_sets = new_letter_sets;
    memset(gdg->letter_sets + old_cap, 0, new_node_diff);

    return true;
}

void gdg_set_edge(GADDAG gdg, uint32_t node, char ch, uint32_t dst) {
    /* Create an edge from one node to another */
    int ch_idx = gdg_ch_to_idx(ch);
    gdg->edges[node * GDG_MAX_CHARS + ch_idx] = dst;
    gdg->num_edges++;
}

uint32_t gdg_add_edge(GADDAG gdg, uint32_t node, char ch) {
    /* Add an edge to a node (if it does not already exist), returning the */
    /* destination node */
    uint32_t dst = gdg_follow_edge(gdg, node, ch);
    if (dst == 0) {
        dst = gdg->num_nodes++;
        if (gdg->num_nodes >= gdg->cap) {
            if(!gdg_grow(gdg, gdg->cap + GDG_DEFAULT_CAP)) return 0;
        }
        gdg_set_edge(gdg, node, ch, dst);
    }
    return dst;
}

void gdg_add_end(GADDAG gdg, uint32_t node, char ch) {
    /* Add a letter to a node's letter set */
    int ch_idx = gdg_ch_to_idx(ch);
    gdg->letter_sets[node] |= (1 << ch_idx);
}

uint32_t gdg_add_final_edge(GADDAG gdg, uint32_t node, char ch, char end_ch) {
    /* Add an edge to a node (if it does not already exist) and add a letter */
    /* to the destination node's letter set */
    uint32_t dst = gdg_add_edge(gdg, node, ch);
    gdg_add_end(gdg, dst, end_ch);
    return dst;
}

bool gdg_force_edge(GADDAG gdg, uint32_t node, char ch, uint32_t dst) {
    uint32_t next_node = gdg_follow_edge(gdg, node, ch);
    if (next_node != dst) {
        if (next_node != 0) return false;
        gdg_set_edge(gdg, node, ch, dst);
    }
    return true;
}

Result gdg_crawl(GADDAG gdg, uint32_t node, char *partial_word, bool wrapped,
              Result res) {
    /* Find all possible words starting from a node */
    size_t len = strlen(partial_word);
    char *word = calloc(len + 2, sizeof(char));
    if (word == NULL) return NULL;
    char *new_partial_word = calloc(len + 2, sizeof(char));
    if (new_partial_word == NULL) return NULL;
    uint32_t letter_set = gdg->letter_sets[node];
    char ch;
    uint32_t next_node;
    uint8_t start_idx;

    if (wrapped) start_idx = 1;
    else start_idx = 0;

    for (uint32_t i = start_idx; i < GDG_MAX_CHARS; i++) {
        ch = gdg_idx_to_ch(i);

        if (i > 0 && (letter_set >> i) & 1) {
            if (wrapped) {
                memcpy(word, partial_word, len);
                word[len] = ch;
            } else {
                word[0] = ch;
                memcpy(word + 1, partial_word, len);
            }
            
            if (!res) res = gdg_create_result(word, NULL);
            else res = gdg_create_result(word, res);
        }

        next_node = gdg_follow_edge(gdg, node, ch);
        if (next_node) {
            if (i == 0) res = gdg_crawl(gdg, next_node, partial_word, 1, res);
            else {
                if (wrapped) {
                    memcpy(new_partial_word, partial_word, len);
                    new_partial_word[len] = ch;
                } else {
                    new_partial_word[0] = ch;
                    memcpy(new_partial_word + 1, partial_word, len);
                }

                res = gdg_crawl(gdg, next_node, new_partial_word, wrapped, res);
            }
        }
    }

    free(word);
    free(new_partial_word);
    return res;
}

Result gdg_crawl_end(GADDAG gdg, uint32_t node, char *partial_word,
                     Result res) {
    /* Find all possible words starting from a node only by appending */
    /* letters */
    size_t len = strlen(partial_word);
    char *word = calloc(len + 2, sizeof(char));
    if (word == NULL) return NULL;
    char *new_partial_word = calloc(len + 2, sizeof(char));
    if (new_partial_word == NULL) return NULL;
    uint32_t letter_set = gdg->letter_sets[node];
    char ch;
    uint32_t next_node;

    for (uint32_t i = 1; i < GDG_MAX_CHARS; i++) {
        ch = gdg_idx_to_ch(i);

        if ((letter_set >> i) & 1) {
            word[0] = ch;
            memcpy(word + 1, partial_word, len);
            
            if (!res) res = gdg_create_result(word, NULL);
            else res = gdg_create_result(word, res);
        }

        next_node = gdg_follow_edge(gdg, node, ch);
        if (next_node) {
            new_partial_word[0] = ch;
            memcpy(new_partial_word + 1, partial_word, len);

            res = gdg_crawl_end(gdg, next_node, new_partial_word, res);
        }
    }

    free(word);
    free(new_partial_word);
    return res;
}

/* External interface */

GADDAG gdg_create(void) {
    /* Create a new GADDAG */
    GADDAG gdg = (GADDAG)malloc(sizeof(struct GADDAG_Struct));

    gdg->cap = GDG_DEFAULT_CAP;
    gdg->edges = (uint32_t*)calloc(GDG_MAX_CHARS * gdg->cap, sizeof(uint32_t));
    gdg->letter_sets = (uint32_t*)calloc(gdg->cap, sizeof(uint32_t));
    gdg->num_words = 0;
    gdg->num_nodes = 1;
    gdg->num_edges = 0;

    return gdg;
}

bool gdg_save(GADDAG gdg, char *path) {
    /* Save a GADDAG to file */
    FILE *fp = fopen(path, "w");
    if (!fp) return false;

    fwrite(&gdg->cap, sizeof(uint32_t), 1, fp);
    fwrite(&gdg->num_words, sizeof(uint32_t), 1, fp);
    fwrite(&gdg->num_nodes, sizeof(uint32_t), 1, fp);
    fwrite(&gdg->num_edges, sizeof(uint32_t), 1, fp);
    fwrite(gdg->edges, sizeof(uint32_t), gdg->cap * GDG_MAX_CHARS, fp);
    fwrite(gdg->letter_sets, sizeof(uint32_t), gdg->cap, fp);

    fclose(fp);
    return true;
}

GADDAG gdg_load(char *path) {
    /* Load a GADDAG from file */
    FILE *fp = fopen(path, "r");
    if (!fp) return NULL;

    GADDAG gdg = gdg_create();

    uint32_t cap;
    fread(&cap, sizeof(uint32_t), 1, fp);
    gdg_grow(gdg, cap);

    fread(&gdg->num_words, sizeof(uint32_t), 1, fp);
    fread(&gdg->num_nodes, sizeof(uint32_t), 1, fp);
    fread(&gdg->num_edges, sizeof(uint32_t), 1, fp);
    fread(gdg->edges, sizeof(uint32_t), gdg->cap * GDG_MAX_CHARS, fp);
    fread(gdg->letter_sets, sizeof(uint32_t), gdg->cap, fp);

    fclose(fp);
    return gdg;
}

int gdg_add_word(GADDAG gdg, char *word) {
    /* Add a word to a GADDAG */
    /* Returns: */
    /*     0 if the word was successfully added */
    /*     1 if the word contains invalid characters */
    /*     2 if the word could not be added to the GADDAG due to running */
    /*         out of memory, leaving the GADDAG in an undefined state */
    size_t l = strlen(word);

    for (size_t i = 0; i < l; i++) {
        if (gdg_ch_to_idx(word[i]) == -1) return 1;
    }

    gdg->num_words++;

    // Add path from last letter in word
    uint32_t node = 0;
    for (int i = l - 1; i >= 2; --i) {
        node = gdg_add_edge(gdg, node, word[i]);
        if (!node) return 2;
    }
    node = gdg_add_final_edge(gdg, node, word[1], word[0]);
    if (!node) return 2;

    if (l == 1) return 0;

    // Add path from penultimate letter in word
    node = 0;
    for (int i = l - 2; i >= 0; --i) {
        node = gdg_add_edge(gdg, node, word[i]);
        if (!node) return 2;
    }
    node = gdg_add_final_edge(gdg, node, '+', word[l - 1]);
    if (!node) return 2;

    // Create remaining paths
    for (int m = l - 3; m >= 0; --m) {
        uint32_t force_node = node;
        node = 0;
        for (int i = m; i >= 0; --i) {
            node = gdg_add_edge(gdg, node, word[i]);
            if (!node) return 2;
        }
        node = gdg_add_edge(gdg, node, '+');
        if (!node) return 2;
        if (!gdg_force_edge(gdg, node, word[m + 1], force_node)) return 2;
    }
    
    return 0;
}

void gdg_letter_set(GADDAG gdg, uint32_t node, char *buffer) {
    /* Place the letter set of a node into a buffer */
    uint8_t offset = 1;
    uint8_t i = 0;
    while (offset < GDG_MAX_CHARS) {
        if ((gdg->letter_sets[node] >> offset) & 1) {
            buffer[i++] = gdg_idx_to_ch(offset);
        }
        offset++;
    }
}

void gdg_edges(GADDAG gdg, uint32_t node, char *buffer) {
    /* Place the edges of a node into a buffer */
    uint8_t offset = 0;
    uint8_t i = 0;
    uint32_t next_node;
    char ch;

    while (offset < GDG_MAX_CHARS) {
        ch = gdg_idx_to_ch(offset);
        next_node = gdg_follow_edge(gdg, node, ch);
        if (next_node) buffer[i++] = ch;
        offset++;
    }
}

bool gdg_is_end(GADDAG gdg, uint32_t node, char ch) {
    /* Check if a character is part of a node's letter set */
    int ch_idx = gdg_ch_to_idx(ch);
    if (ch_idx == -1) return false;
    return gdg->letter_sets[node] & (1 << ch_idx);
}

bool gdg_has(GADDAG gdg, char *word) {
    /* Check if a GADDAG contains a word */ 
    size_t l = strlen(word);

    uint32_t node = 0;
    for (int i = l - 1; i > 0; --i) {
        node = gdg_follow_edge(gdg, node, word[i]);
        if (!node) return false;
    }

    return gdg_is_end(gdg, node, word[0]);
}

Result gdg_starts_with(GADDAG gdg, char *prefix) {
    /* Get all words in a GADDAG which start with a prefix */
    size_t l = strlen(prefix);
    Result res = NULL;
    uint32_t node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && gdg_is_end(gdg, node, prefix[i])) {
            res = gdg_create_result(prefix, NULL);
        }
        node = gdg_follow_edge(gdg, node, prefix[i]);
        if (!node) return NULL;
    }

    node = gdg_follow_edge(gdg, node, '+');
    if (!node) return NULL;

    return gdg_crawl(gdg, node, prefix, 1, res);
}

Result gdg_contains(GADDAG gdg, char *sub) {
    /* Get all words in a GADDAG which contain a substring */
    size_t l = strlen(sub);
    Result res = NULL;
    uint32_t node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && gdg_is_end(gdg, node, sub[i])) {
            res = gdg_create_result(sub, NULL);
        }
        node = gdg_follow_edge(gdg, node, sub[i]);
        if (!node) return NULL;
    }

    return gdg_crawl(gdg, node, sub, 0, res);
}

Result gdg_ends_with(GADDAG gdg, char *suffix) {
    /* Get all words in a GADDAG which end with a suffix */
    size_t l = strlen(suffix);
    Result res = NULL;
    uint32_t node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && gdg_is_end(gdg, node, suffix[i])) {
            res = gdg_create_result(suffix, NULL);
        }
        node = gdg_follow_edge(gdg, node, suffix[i]);
        if (!node) return NULL;
    }

    return gdg_crawl_end(gdg, node, suffix, res);
}

uint32_t gdg_follow_edge(GADDAG gdg, uint32_t node, char ch) {
    /* Follow an edge from a node, returning 0 if no such edge exists */
    int ch_idx = gdg_ch_to_idx(ch);
    if (ch_idx == -1) return 0;
    return gdg->edges[node * GDG_MAX_CHARS + ch_idx];
}

void gdg_destroy(GADDAG gdg) {
    /* Destroy a GADDAG */
    free(gdg->edges);
    free(gdg->letter_sets);
    free(gdg);
}

void gdg_destroy_result(Result res) {
    /* Destroy a Result */
    Result last = NULL;
    while (res) {
        last = res;
        res = res->next;
    }

    Result prev;
    while (last) {
        prev = last->prev;
        free(last->str);
        free(last);
        last = prev;
    }
}

