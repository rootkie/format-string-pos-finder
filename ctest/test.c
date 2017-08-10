#include <stdio.h>
#include <string.h>

#define BUFFERSIZE 100

int main(){
    char buffer[BUFFERSIZE];
    while(fgets(buffer, BUFFERSIZE, stdin) != NULL){
        printf(buffer);
    }
    return 0;
}
