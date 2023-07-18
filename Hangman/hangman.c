#include <stdio.h>
#include <string.h>

#define MAX_WORD_LEN 20
#define MAX_TRIES 5

int main() {
    char word[MAX_WORD_LEN + 1];
    char guessed[MAX_WORD_LEN + 1];
    int len, i, j, tries = 0, found = 0;

    printf("Enter the word to be guessed (max length %d): ", MAX_WORD_LEN);
    scanf("%s", word);

    len = strlen(word);
    for (i = 0; i < len; i++) {
        guessed[i] = '_';
    }
    guessed[i] = '\0';

    while (tries < MAX_TRIES && !found) {
        char letter;
        printf("\nGuessed word: %s\n", guessed);
        printf("Enter a letter: ");
        scanf(" %c", &letter);

        for (i = 0; i < len; i++) {
            if (word[i] == letter) {
                guessed[i] = letter;
            }
        }

        if (strcmp(word, guessed) == 0) {
            found = 1;
        } else {
            tries++;
        }
    }

    if (found) {
        printf("You win! The word was %s.\n", word);
    } else {
        printf("You lose! The word was %s.\n", word);
    }

    return 0;
}
