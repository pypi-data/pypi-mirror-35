#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#include "cgaddag.h"

uint8_t MAX_CHARS = 27;
uint32_t DEFAULT_CAP = 100;

uint8_t ch_to_idx(char ch) {
    ch = tolower(ch);
    if (ch == '+') return 0;
    if (ch == '?') return 31;
    else if (ch >= 97 && ch <= 122) return ch - 96;
    else {
        fprintf(stderr, "Invalid character '%c'\n", ch);
        exit(EXIT_FAILURE);
    }
}

char idx_to_ch(uint8_t idx) {
    if (idx == 0) return '+';
    else if (idx >= 1 && idx <= 27) return idx + 96;
    else {
        fprintf(stderr, "Invalid index '%d'\n", idx);
        exit(EXIT_FAILURE);
    }
}

Result newResult(char *str, Result next) {
    Result self = (Result)malloc(sizeof(struct Result_Struct));
    if (self == NULL) {
        fprintf(stderr, "Failed to create result, out of memory.\n");
        exit(EXIT_FAILURE);
    }

    if (next) next->prev = self;

    self->str = strdup(str);
    if (self->str == NULL) {
        fprintf(stderr, "Failed to duplicate string, out of memory.\n");
        exit(EXIT_FAILURE);
    }
    self->next = next;
    self->prev = NULL;


    return self;
}

void grow_GADDAG(GADDAG gdg) {
    uint32_t old_cap = gdg->cap;
    uint32_t new_cap = old_cap + DEFAULT_CAP;
    gdg->cap = new_cap;

    gdg->edges = realloc(gdg->edges, new_cap * MAX_CHARS * sizeof(uint32_t));
    if (gdg->edges == NULL) {
        fprintf(stderr, "Failed to grow the GADDAG, out of memory.\n");
        exit(EXIT_FAILURE);
    }
    memset(gdg->edges + old_cap * MAX_CHARS, 0, (new_cap - old_cap) * MAX_CHARS * sizeof(uint32_t));

    gdg->letter_sets = realloc(gdg->letter_sets, new_cap * sizeof(uint32_t));
    if (gdg->letter_sets == NULL) {
        fprintf(stderr, "Failed to grow the GADDAG, out of memory.\n");
        exit(EXIT_FAILURE);
    }
    memset(gdg->letter_sets + old_cap, 0, (new_cap - old_cap) * sizeof(uint32_t));
}

uint32_t follow_edge(GADDAG gdg, uint32_t node, char ch) {
    uint8_t ch_idx = ch_to_idx(ch);
    return gdg->edges[node * MAX_CHARS + ch_idx];
}

void set_edge(GADDAG gdg, uint32_t node, char ch, uint32_t dst) {
    uint8_t ch_idx = ch_to_idx(ch);
    gdg->edges[node * MAX_CHARS + ch_idx] = dst;
    gdg->num_edges++;
}

uint32_t add_edge(GADDAG gdg, uint32_t node, char ch) {
    uint32_t dst = follow_edge(gdg, node, ch);
    if (dst == 0) {
        dst = gdg->num_nodes++;
        if (gdg->num_nodes >= gdg->cap) grow_GADDAG(gdg);
        set_edge(gdg, node, ch, dst);
    }
    return dst;
}

void add_end(GADDAG gdg, uint32_t node, char ch) {
    uint8_t ch_idx = ch_to_idx(ch);
    gdg->letter_sets[node] |= (1 << ch_idx);
}

uint32_t add_final_edge(GADDAG gdg, uint32_t node, char ch, char end_ch) {
    uint32_t dst = add_edge(gdg, node, ch);
    add_end(gdg, dst, end_ch);
    return dst;
}

void force_edge(GADDAG gdg, uint32_t node, char ch, uint32_t dst) {
    uint32_t next_node = follow_edge(gdg, node, ch);
    if (next_node != dst) {
        if (next_node != 0) {
            fprintf(stderr, "Edge already exists for forced edge\n");
            exit(EXIT_FAILURE);
        }
        set_edge(gdg, node, ch, dst);
    }
}

Result _crawl(GADDAG gdg, uint32_t node, char *partial_word, bool wrapped,
              Result res) {
    size_t len = strlen(partial_word);
    uint32_t letter_set = gdg->letter_sets[node];
    char ch;
    uint32_t next_node;
    char *word;
    char *new_partial_word;
    uint8_t start_idx;

    if (wrapped) start_idx = 1;
    else start_idx = 0;

    for (uint32_t i = start_idx; i < MAX_CHARS; ++i) {
        ch = idx_to_ch(i);

        if (i > 0 && (letter_set >> i) & 1) {
            word = malloc(len + 2);
            if (word == NULL) {
                fprintf(stderr, "Failed to allocate 'word', out of memory.\n");
                exit(EXIT_FAILURE);
            }
            
            if (wrapped) {
                strcpy(word, partial_word);
                word[len] = ch;
                word[len + 1] = '\0';
            } else {
                word[0] = ch;
                strcpy(word + 1, partial_word);
            }
            
            if (!res) res = newResult(word, NULL);
            else res = newResult(word, res);
            free(word);
        }


        next_node = follow_edge(gdg, node, ch);
        if (next_node) {
            if (i == 0) res = _crawl(gdg, next_node, partial_word, 1, res);
            else {
                new_partial_word = malloc(len + 2);
                if (new_partial_word == NULL) {
                    fprintf(stderr, "Failed to allocate 'new_partial_word', out of memory.\n");
                    exit(EXIT_FAILURE);
                }

                if (wrapped) {
                    strcpy(new_partial_word, partial_word);
                    new_partial_word[len] = ch;
                    new_partial_word[len + 1] = '\0';
                } else {
                    new_partial_word[0] = ch;
                    strcpy(new_partial_word + 1, partial_word);
                }

                res = _crawl(gdg, next_node, new_partial_word, wrapped, res);
                free(new_partial_word);
            }
        }
    }

    return res;
}

Result _crawl_end(GADDAG gdg, uint32_t node, char *partial_word, Result res) {
    size_t len = strlen(partial_word);
    uint32_t letter_set = gdg->letter_sets[node];
    char ch;
    uint32_t next_node;
    char *word;
    char *new_partial_word;

    for (uint32_t i = 1; i < MAX_CHARS; ++i) {
        ch = idx_to_ch(i);

        if ((letter_set >> i) & 1) {
            word = malloc(len + 2);
            if (word == NULL) {
                fprintf(stderr, "Failed to allocate 'word', out of memory.\n");
                exit(EXIT_FAILURE);
            }
            word[0] = ch;
            strcpy(word + 1, partial_word);
            
            if (!res) res = newResult(word, NULL);
            else res = newResult(word, res);
            free(word);
        }

        next_node = follow_edge(gdg, node, ch);
        if (next_node) {
            new_partial_word = malloc(len + 2);
            if (new_partial_word == NULL) {
                fprintf(stderr, "Failed to allocate 'new_partial_word', out of memory.\n");
                exit(EXIT_FAILURE);
            }
            new_partial_word[0] = ch;
            strcpy(new_partial_word + 1, partial_word);

            res = _crawl_end(gdg, next_node, new_partial_word, res);
            free(new_partial_word);
        }
    }

    return res;
}


/* External interface */

GADDAG newGADDAG(void) {
    GADDAG gdg = (GADDAG)malloc(sizeof(struct GADDAG_Struct));

    gdg->cap = DEFAULT_CAP;
    gdg->edges = calloc(MAX_CHARS * gdg->cap, sizeof(uint32_t));
    gdg->letter_sets = calloc(gdg->cap, sizeof(uint32_t));
    gdg->num_words = 0;
    gdg->num_nodes = 1;
    gdg->num_edges = 0;

    return gdg;
}

void add_word(GADDAG gdg, char *word) {
    size_t l = strlen(word);

    gdg->num_words++;

    // Add path from last letter in word
    uint32_t node = 0;
    for (int i = l - 1; i >= 2; --i) {
        node = add_edge(gdg, node, word[i]);
    }
    node = add_final_edge(gdg, node, word[1], word[0]);

    if (l == 1) return;

    // Add path from penultimate letter in word
    node = 0;
    for (int i = l - 2; i >= 0; --i) {
        node = add_edge(gdg, node, word[i]);
    }
    node = add_final_edge(gdg, node, '+', word[l - 1]);

    // Create remaining paths
    for (int m = l - 3; m >= 0; --m) {
        uint32_t force_node = node;
        node = 0;
        for (int i = m; i >= 0; --i) {
            node = add_edge(gdg, node, word[i]);
        }
        node = add_edge(gdg, node, '+');
        force_edge(gdg, node, word[m + 1], force_node);
    }
}

void letter_set(GADDAG gdg, uint32_t node, char *buffer) {
    uint8_t offset = 1;
    uint8_t i = 0;
    while (offset < MAX_CHARS) {
        if ((gdg->letter_sets[node] >> offset) & 1) {
            buffer[i++] = idx_to_ch(offset);
        }
        offset++;
    }
}

void edges(GADDAG gdg, uint32_t node, char *buffer) {
    uint8_t offset = 0;
    uint8_t i = 0;
    uint32_t next_node;
    char ch;

    while (offset < MAX_CHARS) {
        ch = idx_to_ch(offset);
        next_node = follow_edge(gdg, node, ch);
        if (next_node) buffer[i++] = ch;
        offset++;
    }
}

bool is_end(GADDAG gdg, uint32_t node, char ch) {
    uint8_t ch_idx = ch_to_idx(ch);
    return gdg->letter_sets[node] & (1 << ch_idx);
}

bool has(GADDAG gdg, char *word) {
    size_t l = strlen(word);

    uint32_t node = 0;
    for (int i = l - 1; i > 0; --i) {
        node = follow_edge(gdg, node, word[i]);
        if (!node) return false;
    }

    return is_end(gdg, node, word[0]);
}

Result starts_with(GADDAG gdg, char *prefix) {
    size_t l = strlen(prefix);
    Result res = NULL;
    uint32_t node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && is_end(gdg, node, prefix[i])) {
            res = newResult(prefix, NULL);
        }
        node = follow_edge(gdg, node, prefix[i]);
        if (!node) return NULL;
    }

    node = follow_edge(gdg, node, '+');
    if (!node) return NULL;

    return _crawl(gdg, node, prefix, 1, res);
}

Result contains(GADDAG gdg, char *sub) {
    size_t l = strlen(sub);
    Result res = NULL;
    uint32_t node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && is_end(gdg, node, sub[i])) {
            res = newResult(sub, NULL);
        }
        node = follow_edge(gdg, node, sub[i]);
        if (!node) return NULL;
    }

    return _crawl(gdg, node, sub, 0, res);
}

Result ends_with(GADDAG gdg, char *suffix) {
    size_t l = strlen(suffix);
    Result res = NULL;
    uint32_t node = 0;

    for (int i = l - 1; i >= 0; --i) {
        if (i == 0 && is_end(gdg, node, suffix[i])) {
            res = newResult(suffix, NULL);
        }
        node = follow_edge(gdg, node, suffix[i]);
        if (!node) return NULL;
    }

    return _crawl_end(gdg, node, suffix, res);
}

void destroy_GADDAG(GADDAG gdg) {
    free(gdg->edges);
    free(gdg->letter_sets);
    free(gdg);
}

void destroy_result(Result res) {
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

