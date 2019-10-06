#include <stdio.h>

int main(void) {
  printf("#ifndef _ADASD_H\n");
  printf("#define _ADASD_H\n");
  printf("const char ctlPage[] = {");

  int c;
  int pos = 0;
  while((c = getchar()) != EOF) {
    if (pos % 100 == 0) {
      printf("\n");
    }
    printf("0x%02x,", c & 0x00FF);
    pos++;
  }

  printf("};\n");
  printf("#endif\n");
  return 0;
}
