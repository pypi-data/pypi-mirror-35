#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cgaddag.h"

int main() {
    GADDAG gdg = gdg_create();

    gdg_add_word(gdg, "CARE");
    gdg_add_word(gdg, "CAR");
    gdg_add_word(gdg, "BAR");

    printf("Capacity: %u\n", gdg->cap);
    printf("Total words: %u\n", gdg->num_words);
    printf("Total nodes: %u\n", gdg->num_nodes);
    printf("Total edges: %u\n", gdg->num_edges);

    printf("\nContains CARE: %d\n", gdg_has(gdg, "CARE"));
    printf("Contains CAR: %d\n", gdg_has(gdg, "CAR"));
    printf("Contains FOO: %d\n", gdg_has(gdg, "FOO"));

    Result res;
    Result tmp;

    printf("\nFinding words ending with 'AR'\n");
    res = gdg_ends_with(gdg, "ar");
    if (res) {
        tmp = res;
        while (tmp) {
            printf("  %s\n", tmp->str);
            tmp = tmp->next;
        }
        gdg_destroy_result(res);
    } else printf("  No words found\n");

    printf("\nFinding words starting with 'CAR'\n");
    res = gdg_starts_with(gdg, "car");
    if (res) {
        tmp = res;
        while (tmp) {
            printf("  %s\n", tmp->str);
            tmp = tmp->next;
        }
        gdg_destroy_result(res);
    } else printf("  No words found\n");

    printf("\nFinding words containing 'AR'\n");
    res = gdg_contains(gdg, "ar");
    if (res) {
        tmp = res;
        while (tmp) {
            printf("  %s\n", tmp->str);
            tmp = tmp->next;
        }
        gdg_destroy_result(res);
    } else printf("  No words found\n");

    uint32_t r_st = gdg_follow_edge(gdg, 0, 'R');
    uint32_t ra_st = gdg_follow_edge(gdg, r_st, 'A');

    char edge_letters[GDG_MAX_CHARS];
    memset(edge_letters, '\0', GDG_MAX_CHARS);
    gdg_edges(gdg, 0, edge_letters);
    printf("\nEdges from root: %s\n", edge_letters);

    char end_letters[GDG_MAX_CHARS];
    memset(end_letters, '\0', GDG_MAX_CHARS);
    gdg_letter_set(gdg, ra_st, end_letters);
    printf("Letter set for root -> R -> A: %s\n", end_letters);

    printf("\nSaving GADDAG to 'example.gdg'\n");
    gdg_save(gdg, "example.gdg");

    gdg_destroy(gdg);
}

