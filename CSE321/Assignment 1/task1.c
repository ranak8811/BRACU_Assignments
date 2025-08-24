#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdbool.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <filename_without_extension>\n", argv[0]);
        return 1;
    }

    char buffer[120];
    char filename[128];

    snprintf(filename, sizeof(filename), "%s.txt", argv[1]);

    int new_file = open(filename, O_CREAT | O_RDWR | O_APPEND, 0666);
    if (new_file == -1) {
        perror("Error opening/creating file");
        return 1;
    }

    printf("%s file has been created/opened\n", filename);
    printf("Write anything here!! -> To stop write -1\n");

    while (true) {
        memset(buffer, '\0', sizeof(buffer));
        read(0, buffer, sizeof(buffer));

        if (strcmp(buffer, "-1\n") == 0) {
            printf("\nStopping the program\n");
            break;
        }

        write(new_file, buffer, strlen(buffer));
    }

    close(new_file);
    return 0;
}

